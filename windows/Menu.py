from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.label import MDLabel

from windows.Window import Window


class Menu(Window):
    def __init__(self, controller, **kw):
        super(Menu, self).__init__(controller, **kw)

        self.title_label._set_text("Меню")

        button_layout = GridLayout(cols=2)

        cash_withdrawal_button = Button(text="Cнятие налички", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.5),
                                        on_press=lambda x: controller.set_present_screen_name("CashWithdrawalWindow"))
        balance_button = Button(text="Баланс", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.5),
                                on_press=lambda x: controller.set_present_screen_name("BalanceWindow"))
        phone_paymant_button = Button(text="Оплата телефона", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.5),
                                      on_press=lambda x: controller.set_present_screen_name("PhonePaymantWindow"))
        utility_services_payment_button = Button(text="Оплата коммунальных услуг", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.5),
                                      on_press=lambda x: controller.set_present_screen_name("UtilityServicesPaymentWindow"))
        money_transaction = Button(text="Перевод средств", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.5),
                                      on_press=lambda x: controller.set_present_screen_name("MoneyTransactionWindow"))
        exit_button = Button(text="Выход", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.5),
                             on_press=lambda x: controller.set_present_screen_name("ExitWindow"))

        cash_withdrawal_button_layout = AnchorLayout(anchor_x='left', anchor_y='center')
        cash_withdrawal_button_layout.add_widget(cash_withdrawal_button)

        balance_button_layout = AnchorLayout(anchor_x='right', anchor_y='center')
        balance_button_layout.add_widget(balance_button)

        phone_paymant_button_layout = AnchorLayout(anchor_x='left', anchor_y='center')
        phone_paymant_button_layout.add_widget(phone_paymant_button)

        utility_services_payment_button_layout = AnchorLayout(anchor_x='right', anchor_y='center')
        utility_services_payment_button_layout.add_widget(utility_services_payment_button)

        money_transaction_layout = AnchorLayout(anchor_x='left', anchor_y='center')
        money_transaction_layout.add_widget(money_transaction)

        exit_button_layout = AnchorLayout(anchor_x='right', anchor_y='center')
        exit_button_layout.add_widget(exit_button)

        button_layout.add_widget(cash_withdrawal_button_layout)
        button_layout.add_widget(balance_button_layout)
        button_layout.add_widget(phone_paymant_button_layout)
        button_layout.add_widget(utility_services_payment_button_layout)
        button_layout.add_widget(money_transaction_layout)
        button_layout.add_widget(exit_button_layout)
        self.controlled_layout.add_widget(button_layout)
