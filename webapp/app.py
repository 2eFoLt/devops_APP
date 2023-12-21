from flask import Flask, request, render_template, redirect, url_for
from connection_tools import ConnectorDB
from misc import _time

app = Flask(__name__)
connector_object = ConnectorDB()


@app.route('/', methods=['GET'])
def index():
    current_heights = connector_object.select(['*'], 'heights')
    return render_template('index.html', heights=current_heights)


@app.route('/view_height/<int:height_id>', methods=['GET'])
def view_height(height_id):
    height = connector_object.select(['*'], 'heights', where=f'id={height_id}')
    print(height)
    return redirect(url_for('index'))


@app.route('/create_height', methods=['GET', 'POST'])
def create_height():
    task2 = connector_object.select(['*'], 'heights')
    if request.method == 'POST':
        print(connector_object.insert('heights', ['name', 'height', 'country'], list(request.form.values())))
        return redirect(url_for('create_height'))
    else:
        return render_template('create_height.html', task2=task2)


@app.route('/edit_height/<int:height_id>', methods=['GET', 'POST'])
def edit_height(height_id):
    task3 = connector_object.select(['*'], 'heights')
    if request.method == 'POST':
        print(connector_object.update('heights', ['name', 'height', 'country'], list(request.form.values()),
                                      where=f'id={height_id}'))
        return redirect(url_for('index'))
    else:
        return render_template('edit_height.html', task3=task3, id=height_id)


@app.route('/date_time', methods=['GET', 'POST'])
def date_time():
    if request.method == 'POST':
        date_start, time_start = request.form.get('date_start'), request.form.get('time_start')
        date_end, time_end = request.form.get('date_end'), request.form.get('time_end')
        result = connector_object.select(['users.username', 'ascend_groups.ascend_start_time'], 'ascend_groups',
                                         joins=['group_to_user on ascend_groups.id = group_to_user.group_id',
                                                'users on group_to_user.user_id = users.id'],
                                         where='ascend_groups.ascend_start_time',
                                         between=(f"{_time(date_start, time_start)}", f"{_time(date_end, time_end)}"))
        return render_template('groups/date_time.html', task4=result)
    return render_template('groups/date_time.html')


@app.route('/groups', methods=['GET', 'POST'])
def groups():
    return render_template('groups/index.html')


@app.route('/date_time_group', methods=['GET', 'POST'])
def date_time_group():
    if request.method == 'POST':
        date_start, time_start = request.form.get('date_start'), request.form.get('time_start')
        date_end, time_end = request.form.get('date_end'), request.form.get('time_end')
        result = connector_object.select(['ascend_groups.group_name', 'ascend_groups.ascend_start_time'],
                                         'ascend_groups',
                                         where='ascend_groups.ascend_start_time',
                                         between=(f"{_time(date_start, time_start)}", f"{_time(date_end, time_end)}"))
        return render_template('groups/date_time_group.html', task7=result)
    return render_template('groups/date_time_group.html')


@app.route('/ascend_height_group', methods=['GET', 'POST'])
def ascend_height_group():
    result_users = connector_object.select(['*'], 'users')
    if request.method == 'POST':
        user_id = request.form.get('form_select')
        result_ascend = connector_object.select(['heights.id', 'name', 'height', 'country', 'ascend_counter'],
                                                'heights',
                                                joins=['ascend_stat on heights.id = ascend_stat.height_id',
                                                       'group_to_user on ascend_stat.group_id = group_to_user.group_id'],
                                                where=f'group_to_user.user_id = {user_id}')
        result_heights = connector_object.select(['*'], 'heights')
        es1 = [i for i in result_heights if i not in result_ascend]
        es2 = set(result_ascend)
        height_2_count = {}
        for item in es2:
            height_2_count[item[1]] = result_ascend.count(item)
        for item in es1:
            height_2_count[item[1]] = 0
        return render_template('groups/ascend_height_group.html', task6=height_2_count, users=result_users)
    else:
        return render_template('groups/ascend_height_group.html', users=result_users)


@app.route('/group_per_height', methods=['GET'])  # TASK 1
def group_per_height():
    heights = connector_object.select(['*'], 'heights')
    height_ids = [item[0] for item in connector_object.select(['id'], 'heights')]
    results = [connector_object.select(['group_name', 'ascend_start_time'], 'ascend_groups',
                                       joins=['ascend_stat on ascend_groups.id = ascend_stat.group_id',
                                              'heights on ascend_stat.height_id = heights.id'],
                                       where=f'heights.id = {h_id}',
                                       order_by='ascend_start_time') for h_id in height_ids]
    return render_template('group_per_height.html', heights=heights, results=results)


@app.route('/new_group', methods=['GET', 'POST'])  # TASK 8
# TODO: более удобный способ работы с базой, пересмотр структуры базы?
def new_group():
    if request.method == 'POST':
        group_name, height_target, start_date, start_time = list(request.form.values())
        start_time += ':00'
        connector_object.insert('ascend_groups', ['group_name', 'ascend_start_time'],
                                [f'{group_name}', f"{start_date} {start_time}"])
        group_id = connector_object.select(['ascend_groups.id'], 'ascend_groups',
                                           where=f'group_name="{group_name}"')[0][0]
        connector_object.insert('ascend_stat', ['height_id', 'group_id'], [height_target, group_id])
        return redirect(url_for('new_group'))
    else:
        heights = connector_object.select(['*'], 'heights')
        return render_template('groups/create_group.html', heights=heights)


@app.route('/add_to_group', methods=['GET', 'POST'])  # TASK 5
# TODO: большие вопросы к логике: существующий ли пользователь, корректная структура базы, триггеры?
def add_to_group():
    if request.method == 'POST':
        group_id = request.form.get('form_select')
        name, email, pswd = request.form.get('username'), request.form.get('email'), request.form.get('pswd')
        connector_object.insert('users', ['username', 'email', 'password'], [name, email, pswd])
        user_id = connector_object.select(['users.id'], 'users', where=f'username="{name}"')[0][0]
        connector_object.insert('group_to_user', ['group_id', 'user_id'], [group_id, user_id])
        return redirect(url_for('add_to_group'))
    else:
        pass
        all_groups = connector_object.select(['*'], 'ascend_groups')
        return render_template('groups/add_to_group.html', groups=all_groups)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
