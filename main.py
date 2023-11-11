#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from data_manager import DataManager
from pprint import pprint
from flight_data import FlightData
from notification_manager import NotificationManager

FLY_FROM_CITY = 'BUH'

sheet_data_manager = DataManager()
sheet_data = sheet_data_manager.get_sheet_data()

flight_data_manager = FlightData()
notification_manager = NotificationManager()

print(sheet_data)

for city in sheet_data:
    if len(city['iataCode']) == 0:
        city_iata_code = flight_data_manager.get_city_iata_code(city['city'])
        city['iataCode'] = city_iata_code
        rowid = city['id']
        sheet_data_manager.set_city_iata_code(rowid, city_iata_code)

for city in sheet_data:
    city_iata_code = city['iataCode']
    city_requested_price = city['lowestPrice']
    get_lowest_price = flight_data_manager.get_flight(FLY_FROM_CITY, city_iata_code)
    if get_lowest_price == "None":
        pass
    elif get_lowest_price['lowest_price_flight'] <= city_requested_price:
        # print(f"{get_lowest_price['city_to']} €{get_lowest_price['lowest_price_flight']}")
        message_body = (f"Low price alert! Only €{get_lowest_price['lowest_price_flight']} to fly from "
                        f"{get_lowest_price['city_from']}-{get_lowest_price['airpot_iata_code_from']} "
                        f"to {get_lowest_price['city_to']}-{get_lowest_price['airpot_iata_code_to']}, "
                        f"from {get_lowest_price['outbound_date']} to {get_lowest_price['inbound_date']}")

        notification_manager.send_sms(message_body)

        print(message_body)