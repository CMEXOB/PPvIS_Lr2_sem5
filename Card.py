class Card:
    def __init__(self, card_number, pin_code, check, is_blocked):
        self.card_number = card_number
        self.pin_code = pin_code
        self.check = check
        self.is_blocked = is_blocked

    def get_is_blocked(self):
        return self.is_blocked

    def get_pin_code(self):
        return self.pin_code

    def get_check(self):
        return self.check

    def get_card_number(self):
        return self.card_number

    def set_check(self, check):
        self.check = check

    def set_is_blocked(self, is_blocked):
        self.is_blocked = is_blocked
