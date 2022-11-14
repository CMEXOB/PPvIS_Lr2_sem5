from MoneyField import MoneyField


class Model:
    def __init__(self):
        self.money_fields = []

        self.money_fields.append(MoneyField(500, 10))
        self.money_fields.append(MoneyField(200, 10))
        self.money_fields.append(MoneyField(100, 10))
        self.money_fields.append(MoneyField(50, 10))
        self.money_fields.append(MoneyField(20, 10))
        self.money_fields.append(MoneyField(10, 10))
        self.money_fields.append(MoneyField(5, 10))

        self.money_fields.sort(key=lambda x: x.get_denomination(), reverse=True)

        self.worked_card = None

    def insert_card(self, card):
        pass

    def return_card(self):
        pass

    def get_pin_code(self):
        pass

    def get_balance(self):
        return 256

    def phone_payment(self, phone_number, needed_sum):
        pass

    def utility_services_payment(self, utility_bill, needed_sum):
        pass

    def money_transaction(self, beneficiary_account, needed_sum):
        pass

    def withdraw_money(self, needed_sum):
        pass

    def is_enough_money_on_card(self, needed_sum):
        pass

    def is_enough_money_in_atm(self, needed_sum):
        pass
