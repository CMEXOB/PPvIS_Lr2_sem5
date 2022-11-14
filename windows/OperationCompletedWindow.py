import time

from kivy.uix.button import Button
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel

from windows.Window import Window


class OperationCompletedWindow(Window):
    def __init__(self, controller, **kw):
        super(OperationCompletedWindow, self).__init__(controller, **kw)


        completed_label = MDLabel(text="Операция завершена успешно!", font_size=200, halign="center")
        self.controlled_layout.add_widget(completed_label)

    def on_enter(self, *args):
        time.sleep(1)
        self.controller.set_present_screen_name("ContinuationWindow")