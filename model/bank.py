class Bank:
    def __init__(self: str, name, number_of_clients: int, number_of_loans: int):
        self.name = str(name)
        self.number_of_clients = int(number_of_clients)
        self.number_of_loans = int(number_of_loans)

    def __repr__(self):
        return "{} (clients = {}, loans = {})".format(repr(self.name), repr(self.number_of_clients), repr(self.number_of_loans))

