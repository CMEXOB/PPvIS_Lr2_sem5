from kivy.uix.button import Button
from kivymd.uix.label import MDLabel

from windows.Window import Window


class ContinuationWindow(Window):
    def __init__(self, controller, **kw):
        super(ContinuationWindow, self).__init__(controller, **kw)

        proceed_label = MDLabel(text="Продолжить ?", halign="center")
        yes_button = Button(text="1. Да", background_color=(0.53, 0.71, .53, .6),
                            on_press=lambda x: controller.set_present_screen_name("Menu"))
        no_button = Button(text="2. Нет", background_color=(0.53, 0.71, .53, .6),
                           on_press=lambda x: controller.set_present_screen_name("ExitWindow"))
        self.controlled_layout.add_widget(proceed_label)
        self.controlled_layout.add_widget(yes_button)
        self.controlled_layout.add_widget(no_button)