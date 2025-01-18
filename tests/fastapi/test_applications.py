from unittest import mock

import pytest
from fastapi.testclient import TestClient

from services.fastapi.main import app  
from services.fastapi.models.applications import Application 
from services.fastapi.schemas.applications_schemas import ApplicationCreate



@pytest.fixture
def mock_db_session():
    db_mock = mock.MagicMock()
    db_mock.add = mock.MagicMock()
    db_mock.commit = mock.MagicMock()
    db_mock.refresh = mock.MagicMock()
    return db_mock


@pytest.fixture
def client():
    client = TestClient(app)
    return client


def test_create_application(mock_db_session, client):

    application_data = ApplicationCreate(user_name="test_user", description="Test description")
    
    mock_db_session.add.return_value = None
    mock_db_session.commit.return_value = None
    mock_db_session.refresh.return_value = None


    response = client.post(
        "/applications/", 
        json=application_data.dict()
    )

    assert response.status_code == 201
    response_data = response.json()
    assert response_data["user_name"] == "test_user"
    assert response_data["description"] == "Test description"
    assert "id" in response_data 

    mock_db_session.add.assert_called_once()
    mock_db_session.commit.assert_called_once()
    mock_db_session.refresh.assert_called_once()
