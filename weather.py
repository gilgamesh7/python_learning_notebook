import httpx

class WeatherService:
    def __init__(self, api_key:str)-> None:
        self.api_key: str = api_key

    def get_temperature(self, city:str)-> float:
        response = httpx.get("http://api.weatherapi.com/v1/current.json", params={"key": self.api_key , "q": city})

        response.raise_for_status()

        data = response.json()

        return data["current"]["temp_c"]
