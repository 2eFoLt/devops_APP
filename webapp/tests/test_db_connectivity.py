import mysql.connector as sql_connector


def test_db_is_alive(get_db_config):
    connection_object = sql_connector.connect(**get_db_config)
    assert isinstance(connection_object, sql_connector.CMySQLConnection)


def test_db_is_set_up(get_db_connection):
    select_results = get_db_connection.select(['*'], 'heights')
    assert len(select_results) != 0
