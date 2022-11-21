import time

from kivy.config import Config
from kivy.lang import Builder


Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '480')
Config.set('graphics', 'height', '720')


from windows.Window import Window
from windows.StartWindow import StartWindow
from windows.LoginWindow import LoginWindow
from windows.BalanceWindow import BalanceWindow
from windows.Menu import Menu
from windows.ContinuationWindow import ContinuationWindow
from windows.CashWithdrawalWindow import CashWithdrawalWindow
from windows.PhonePaymantWindow import PhonePaymantWindow
from windows.UtilityServicesPaymentWindow import UtilityServicesPaymentWindow
from windows.MoneyTransactionWindow import MoneyTransactionWindow
from windows.OperationCompletedWindow import OperationCompletedWindow
from windows.ExitWindow import ExitWindow
from windows.InsufficientATMFundsWindow import InsufficientCardFundsWindow
from windows.InsufficientCardFundsWindow import InsufficientATMFundsWindow
from windows.WarningWindow import WarningWindow

from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp


class View(MDApp):
    def __init__(self, model, controller, **kw):
        super(View, self).__init__()
        self.model = model
        self.controller = controller
        self.controller.set_view(self)
        self.screens = ScreenManager()
        self.screens.add_widget(Window(name="Window", controller=self.controller))
        self.screens.add_widget(StartWindow(name="StartWindow", controller=self.controller))
        self.screens.add_widget(LoginWindow(name="LoginWindow", controller=self.controller))
        self.screens.add_widget(BalanceWindow(name="BalanceWindow", controller=self.controller))
        self.screens.add_widget(
            InsufficientATMFundsWindow(name="InsufficientATMFundsWindow", controller=self.controller))
        self.screens.add_widget(
            InsufficientCardFundsWindow(name="InsufficientCardFundsWindow", controller=self.controller))
        self.screens.add_widget(Menu(name="Menu", controller=self.controller))
        self.screens.add_widget(OperationCompletedWindow(name="OperationCompletedWindow", controller=self.controller))
        self.screens.add_widget(CashWithdrawalWindow(name="CashWithdrawalWindow", controller=self.controller))
        self.screens.add_widget(ContinuationWindow(name="ContinuationWindow", controller=self.controller))
        self.screens.add_widget(PhonePaymantWindow(name="PhonePaymantWindow", controller=self.controller))
        self.screens.add_widget(UtilityServicesPaymentWindow(name="UtilityServicesPaymentWindow", controller=self.controller))
        self.screens.add_widget(MoneyTransactionWindow(name="MoneyTransactionWindow", controller=self.controller))

        self.screens.add_widget(WarningWindow(name="WarningWindow", controller=self.controller))
        self.screens.add_widget(ExitWindow(name="ExitWindow", controller=self.controller))

        self.screens.current = "StartWindow"

    def set_present_screen_name(self, present_screen_name):
        if present_screen_name == "Stop":
            self.stop()
        else:
            self.screens.current = present_screen_name

    def get_present_screen_name(self):
        return self.screens.current

    def build(self):
        return self.screens

    def view_work(self):
        self.run()
