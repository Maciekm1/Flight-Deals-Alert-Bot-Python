from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

# prices_sheet_data = data_manager.get_all_data()

# # Adding Iata codes if empty
# i = 1
# for row in prices_sheet_data:
#     i += 1
#     if row["iataCode"] == "":
#
#         # Get Iata from flight search
#         row["iataCode"] = flight_search.get_iata_code(row["city"])
#
#         # Write Iata to google sheet
#         data_manager.write_iata_codes(row["iataCode"], i)
#
#         # Search for flights
#         flight_info = flight_search.search_cheap_flight(row["iataCode"])
#
#         # Send flight info SMS
#         if flight_info[0] < row["lowestPrice"]:
#             notification_manager.send_message(flight_info)

flight_info = flight_search.search_cheap_flight("KRK")
# notification_manager.send_message(flight_info[1])
notification_manager.send_email(flight_info[1], "-")
