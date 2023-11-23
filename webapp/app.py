from flask import Flask, request, render_template, redirect, url_for
from connection_tools import ConnectorDB

app = Flask(__name__)
connector_object = ConnectorDB()


@app.route('/', methods=['GET'])
def index():
    # TODO: на базе поменять название таблицы с groups -> ascend_groups, конфликт с служебными командами MYSQL
    current_heights = connector_object.select(['*'], 'heights')
    return render_template('index.html', heights=current_heights)


@app.route('/view_height/<int:height_id>', methods=['GET'])
def view_height(height_id):
    task1 = connector_object.select(['ascend_groups.group_name', 'ascend_groups.ascend_start_time'], 'ascend_stat',
                                    joins=['ascend_groups on ascend_stat.group_id = ascend_groups.id'],
                                    where=f'height_id = {height_id}',
                                    order_by='ascend_groups.ascend_start_time')
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
        heights = connector_object.select(['*'], 'heights')
        print(heights)
    return render_template('create_height.html', task2=task2)


@app.route('/edit_height/<int:height_id>', methods=['GET', 'POST'])
def edit_height(height_id):
    task3 = connector_object.select(['*'], 'heights')
    if request.method == 'POST':
        print(connector_object.update('heights', ['name', 'height', 'country'], list(request.form.values()),
                                      where=f'id={height_id}'))
        return redirect(url_for('index'))
    else:
        heights = connector_object.select(['*'], 'heights')
        print(heights)
        return render_template('edit_height.html', task3=task3, id=height_id)


@app.route('/date_time', methods=['GET', 'POST'])
def date_time():
    if request.method == 'POST':
        date_start, time_start = request.form.get('date_start'), request.form.get('time_start')
        date_end, time_end = request.form.get('date_end'), request.form.get('time_end')
        time_start += ':00'
        time_end += ':00'
        print(date_start, time_start)
        print(date_end, time_end)
        result = connector_object.select(['users.username', 'ascend_groups.ascend_start_time'], 'ascend_groups',
                                         joins=['group_to_user on ascend_groups.id = group_to_user.group_id',
                                                'users on group_to_user.user_id = users.id'],
                                         where='ascend_groups.ascend_start_time',
                                         between=(f"'{date_start} {time_start}'", f"'{date_end} {time_end}'"))
        print(result)
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
        time_start += ':00'
        time_end += ':00'
        print(date_start, time_start)
        print(date_end, time_end)
        result = connector_object.select(['ascend_groups.group_name', 'ascend_groups.ascend_start_time'],
                                         'ascend_groups',
                                         where='ascend_groups.ascend_start_time',
                                         between=(f"'{date_start} {time_start}'", f"'{date_end} {time_end}'"))
        print(result)
        return render_template('groups/date_time_group.html', task7=result)
    return render_template('groups/date_time_group.html')


@app.route('/ascend_height_group', methods=['GET', 'POST'])
def ascend_height_group():
    result_ascend = connector_object.select(['heights.id', 'name', 'height', 'country', 'ascend_counter'], 'heights',
                                            joins=['ascend_stat on heights.id = ascend_stat.height_id',
                                                   'group_to_user on ascend_stat.group_id = group_to_user.group_id'],
                                            where='group_to_user.user_id = 1')
    result_heights = connector_object.select(['*'], 'heights')
    es1 = [i for i in result_heights if i not in result_ascend]
    print(result_ascend)
    print(es1)
    es2 = set(result_ascend)
    height_2_count = {}
    for item in es2:
        height_2_count[item[1]] = result_ascend.count(item)
    for item in es1:
        height_2_count[item[1]] = 0
    user = connector_object.select(['username'], 'users')
    print(user)
    print(height_2_count)
    return render_template('groups/ascend_height_group.html', task6=height_2_count)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
