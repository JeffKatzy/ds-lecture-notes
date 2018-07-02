class Airline:
    _all = []

    def __init__(self):
        Airline._all.append(self)

    @classmethod
    def all(cls):
        return cls._all
