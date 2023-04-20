class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, price, dac, dc, stop_overseas=0, via_city="", **kwargs):
        self.price = price
        self.departure_airport_code = dac
        self.departure_city = dc
        self.duration = kwargs["duration"]
        self.destination_city = kwargs["destination_city"]
        self.destination_code = kwargs["destination_code"]
        self.link = kwargs["link"]
        self.from_date = kwargs["from_date"]
        self.to_date = kwargs["to_date"]
        self.night_in_dest = kwargs["night_in_dest"]
        self.stop_overseas = stop_overseas
        self.via_city = via_city

    def print_flight_data(self):
        message = [self.price, (
            f"price: {self.price} EUR\nFROM: {self.departure_city}\nTO: {self.destination_city}\nnights in dest:"
            f" {self.night_in_dest}\nlink: {self.link}\nFrom:{self.from_date.split('T')[0]}\n"
            f"To:{self.to_date.split('T')[0]}\n" + f"stop via {self.via_city}\n" if self.stop_overseas != 0 else "\n")]
        print(message[1])
        return message
