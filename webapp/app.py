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
        return render_template('index.html', task4=result)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
