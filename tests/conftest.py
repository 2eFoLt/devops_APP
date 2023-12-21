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
def client():
    app_obj = app.test_client()
    yield app_obj

    # clean up / reset resources here
