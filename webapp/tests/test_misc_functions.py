from webapp import connection_tools, misc


def test_time():
    date = '23.11.12'
    time = '13:45'
    assert misc._time(date, time) == "'23.11.12 13:45:00'"


def test_wrap_in_quotes():
    itr = ['a', 'b', 1, 'c']
    res = connection_tools.wrap_in_quotes(itr)
    expected = ["'a'", "'b'", "'1'", "'c'"]
    assert res == expected


def test_columns_to_values():
    columns = ['col1', 'col2', 'col3']
    values_set = [['a', 'b', 'c'], ['a', '2', 'c']]
    expected_set = ["col1 = 'a',col2 = 'b',col3 = 'c'",
                    "col1 = 'a',col2 = 2,col3 = 'c'"]
    for i in range(len(expected_set)):
        assert connection_tools.columns_to_values(columns, values_set[i]) == expected_set[i]
