class Controller:
    def __init__(self, model):
        self.model = model
        self.view = None

    def set_view(self, view):
        self.view = view

    def insert_card(self, card):
        pass

    def return_card(self):
        pass

    def show_balance(self):
        pass

    def get_balance(self):
        return self.model.get_balance()

    def phone_payment(self, phone_number, needed_sum):
        pass

    def utility_services_payment(self, utility_bill, needed_sum):
        pass

    def money_transaction(self, beneficiary_account, needed_sum):
        pass

    def withdraw_money(self, needed_sum):
        pass

    def input_pin_code(self, pin_code):
        pass

    def set_present_screen_name(self, present_screen_name):
        self.view.set_present_screen_name(present_screen_name)

    def is_correct_phone_number(self, phone_number):
        pass

    def is_correct_utility_bill(self, utility_bill):
        pass

    def is_correct_beneficiary_account(self, beneficiary_account):
        pass

    def block_card(self):
        pass

    def verification_money_on_card(self, needed_sum):
        pass

    def verification_money_in_atm(self, needed_sum):
        pass
