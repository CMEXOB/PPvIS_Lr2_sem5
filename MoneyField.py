class MoneyField:
    def __init__(self, denomination, count):
        self.denomination = denomination
        self.count = count

    def get_count(self):
        return self.count

    def get_denomination(self):
        return self.denomination

    def set_count(self, count):
        self.count = count
