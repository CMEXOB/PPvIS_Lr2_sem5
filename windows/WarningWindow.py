import time

from kivymd.uix.label import MDLabel

from windows.Window import Window


class WarningWindow(Window):

    def __init__(self, controller, **kw):
        super(WarningWindow, self).__init__(controller, **kw)

        completed_label = MDLabel(text="Карта заблокирована!", font_size=200, halign="center")
        self.controlled_layout.add_widget(completed_label)

    def on_enter(self, *args):
        time.sleep(1)
        self.controller.set_present_screen_name("StartWindow")