
import pytest
from typing import Any

from unittest.mock import MagicMock, patch

from weather import WeatherService

def test_get_temperature_with_monkeypatch(monkeypatch: pytest.MonkeyPatch)-> None:
    def fake_get(url: str, params:dict[str, Any])-> Any:
        class FakeResponse:
            def raise_for_status(self)-> None:
                pass
            def json(self)-> dict[str, Any]:
                return {"current":{"temp_c": 19}}

        return FakeResponse()

    monkeypatch.setattr("httpx.get", fake_get)

    service = WeatherService(api_key="fake_key")    
    temp = service.get_temperature("Amsterdam")

    assert temp==19

def test_get_temperature_with_mock_monkeypatch(monkeypatch: pytest.MonkeyPatch)-> None:
    def fake_get(url: str, params:dict[str, Any])-> Any:
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"current":{"temp_c": 19}}

        return mock_response


    monkeypatch.setattr("httpx.get", fake_get)

    service = WeatherService(api_key="fake_key")    
    temp = service.get_temperature("Amsterdam")

    assert temp==19

def test_get_temperature_with_mock_patch()-> None:
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = {"current":{"temp_c": 19}}

    with patch("httpx.get", return_value=mock_response) as mock_get:
        service = WeatherService(api_key="fake_key")    
        temp = service.get_temperature("Amsterdam")

        assert temp == 19
        mock_get.assert_called_once()


@pytest.fixture
def weather_service(monkeypatch: pytest.MonkeyPatch) -> WeatherService:
    def fake_get(url: str, params: dict[str, Any]) -> Any:
        mock_response = MagicMock()
        mock_response.raise_for_status.return_value = None
        mock_response.json.return_value = {"current":{"temp_c": 19}}   

        return mock_response

    monkeypatch.setattr("httpx.get", fake_get)  
    return WeatherService(api_key="fake_key")  

def test_get_temperature_with_fixture(weather_service: WeatherService) -> None:
    temp = weather_service.get_temperature("Amsterdam")
    assert temp == 19



