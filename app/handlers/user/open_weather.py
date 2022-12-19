from aiogram.types import Message, CallbackQuery
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from requests import get
from datetime import datetime
from app.config import WEATHER_API_KEY


async def _parse_wind_direction(weather_dict: dict) -> str:
    wind_direction = {
        '0': 'Северный',
        '45': 'Северо-восточный',
        '90': 'Восточный',
        '135': 'Юго-восточный',
        '180': 'Южный',
        '225': 'Юго-западный',
        '270': 'Западный',
        '315': 'Северо-западный',
    }
    degrees = weather_dict['wind']['deg']
    degrees = round(degrees / 45) * 45
    if degrees == 360:
        degrees = 0
    return wind_direction[str(degrees)]


class CityName(StatesGroup):
    city = State()

# async def get_coordinates() -> Coordinates:
#     """Returns current coordinates using geolocation telegram"""
#     latitude = float
#     longitude = float
#     return Coordinates(latitude=latitude, longitude=longitude)


# async def get_weather_location(coordinates=Coordinates) -> dict:
#     """Requests the weather in OpenWeather API"""
#     latitude, longitude = coordinates
#     url = 'https://api.openweathermap.org/data/2.5/weather'
#     openweather_response = get(url,
#                                params={'lat': latitude, 'lon': longitude, 'units': 'metric',
#                                        'APPID': WEATHER_API_KEY}).json()
#     return await _parse_openweather_response(openweather_response)


async def get_weather_city(city) -> dict:
    """Requests the weather in OpenWeather API"""
    url = 'https://api.openweathermap.org/data/2.5/weather'
    openweather_response = get(url,
                               params={'q': city, 'lang': 'ru', 'units': 'metric', 'APPID': WEATHER_API_KEY}).json()
    if openweather_response['cod'] == '404':
        return openweather_response
    return await _parse_openweather_response(openweather_response)


async def _parse_openweather_response(openweather_response: dict) -> dict:
    if openweather_response['cod'] == '404':
        return openweather_response
    openweather_dict = openweather_response
    return {
        'cod': openweather_dict['cod'],
        'city': openweather_dict["name"],
        'temp': openweather_dict['main']['temp'],
        'temp_feeling': openweather_dict['main']['feels_like'],
        'description': openweather_dict['weather'][0]['description'].capitalize(),
        'sunrise': datetime.fromtimestamp(openweather_dict['sys']['sunrise']),
        'sunset': datetime.fromtimestamp(openweather_dict['sys']['sunset']),
        'wind_speed': openweather_dict['wind']['speed'],
        'wind_dir': await _parse_wind_direction(openweather_dict),
    }


async def answer_city_weather(msg: Message, state: FSMContext):  # Входная точка для команды /weather
    await msg.answer('Напишите название Города для просмотра погоды:')
    await state.set_state(CityName.city.state)


async def send_weather(msg: Message, state: FSMContext):
    weather_out = await get_weather_city(msg.text)
    if weather_out['cod'] == '404':
        await msg.reply(weather_out['message'])
        await state.finish()
        return
    weather_message = f'📌 Погода в <b>{weather_out["city"]}</b>,\n👀 На улице <b>{weather_out["description"]}</b>\n' \
                      f'🌡 Температура: <b>{weather_out["temp"]}°C</b>,\n' \
                      f'🌡 Ощущается: <b>{weather_out["temp_feeling"]}°C</b>\n' \
                      f'💨 <i>{weather_out["wind_dir"]}</i> Ветер: <b>{weather_out["wind_speed"]} м/с</b>\n' \
                      f'🌄 Восход в: <b>{weather_out["sunrise"].strftime("%H:%M")}</b>\n' \
                      f'🌅 Закат в: <b>{weather_out["sunset"].strftime("%H:%M")}</b>\n'
    await msg.reply(weather_message)
    await state.finish()
