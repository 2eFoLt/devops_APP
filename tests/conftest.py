import pytest
from webapp.app import app
from webapp.db_config import db_config
import webapp.connection_tools as tools


@pytest.fixture()
def get_db_config():
    return db_config


@pytest.fixture()
def get_db_connection():
    return tools.ConnectorDB()


@pytest.fixture()
def get_routes():
    return [
        '/', '/create_height', '/date_time', '/groups', '/date_time_group',
        '/ascend_height_group', '/group_per_height', '/new_group', '/add_to_group'
    ]


@pytest.fixture()
def client():
    app_obj = app.test_client()
    yield app_obj

    # clean up / reset resources here
