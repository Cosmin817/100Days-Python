#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from pprint import pprint
from flight_data import FlightData

sheet_data_manager = DataManager()
sheet_data = sheet_data_manager.get_sheet_data()

flight_data_manager = FlightData()

print(sheet_data)

for city in sheet_data:
    if len(city['iataCode']) == 0:
        city_iata_code = flight_data_manager.get_city_iata_code(city['city'])
        city['iataCode'] = city_iata_code
        rowid = city['id']
        sheet_data_manager.set_city_iata_code(rowid, city_iata_code)

print(sheet_data)
