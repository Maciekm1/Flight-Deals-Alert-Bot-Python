import requests

SHEETY_GET_ENDPOINT = "-"


class DataManager:

    def __init__(self):
        self.sheet_row = []

    # This class is responsible for talking to the Google Sheet.
    def get_all_data(self):

        try:
            response = requests.get(url=SHEETY_GET_ENDPOINT)
            self.sheet_row = response.json()["prices"]
            return self.sheet_row
        except KeyError:
            requests.get(url=SHEETY_GET_ENDPOINT).raise_for_status()

    def write_iata_codes(self, iata_code, row_number):

        body = {"price": {"iataCode": iata_code}}
        requests.put(url=SHEETY_GET_ENDPOINT + f"/{row_number}", json=body)
