import requests
from flight_data import FlightData
import datetime as dt

# Airport settings
FLY_FROM = "LBA"

KIWI_LOCATION_ENDPOINT = "https://tequila-api.kiwi.com/locations/query"
KIWI_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
MY_API_KEY = "-"


# This class is responsible for talking to the Flight Search API.
class FlightSearch:

    def __init__(self):
        self.header = {"apikey": MY_API_KEY}

    def get_iata_code(self, name: str) -> str:
        data = {"term": name, "location_types": "city"}

        loc_iata = requests.get(url=KIWI_LOCATION_ENDPOINT, params=data, headers=self.header).json()
        return loc_iata["locations"][0]["code"]

    def search_cheap_flight(self, fly_to):
        future_date = dt.datetime.now().date() + dt.timedelta(days=30 * 6)
        date_7_days = dt.datetime.now().date() + dt.timedelta(days=7)
        date_28_days = dt.datetime.now().date() + dt.timedelta(days=28)

        parameters = {
            "fly_from": FLY_FROM,
            "fly_to": fly_to,
            "return_from": date_7_days.strftime("%d/%m/%Y"),
            "return_to": date_28_days.strftime("%d/%m/%Y"),
            "date-from": dt.datetime.now().date().strftime("%d/%m/%Y"),
            "date-to": future_date.strftime("%d/%m/%Y"),
            "flight_type": "round",
            "max_stopovers": "1"
        }

        response = requests.get(url=KIWI_SEARCH_ENDPOINT, params=parameters, headers=self.header).json()["data"]

        if response[0] is not None:
            data = response[0]
            # pprint(data)
            routes = data["route"]

            cheapest_flight = FlightData(
                price=data["conversion"]["EUR"],
                dac=data["cityCodeFrom"],
                dc=data["cityFrom"],
                duration=data["duration"]["total"],
                destination_city=data["cityTo"],
                destination_code=data["cityCodeTo"],
                link=data["deep_link"],
                from_date=data["route"][0]["utc_departure"],
                to_date=data["route"][len(routes)-1]["utc_departure"],
                night_in_dest=data["nightsInDest"],
                stop_overseas="1" if len(routes) > 2 else "0",
                via_city=data["route"][1]["cityTo"] if data["route"][1]["return"] == "1" else data["route"][1]
                ["cityFrom"]
            )
            return cheapest_flight.print_flight_data()

