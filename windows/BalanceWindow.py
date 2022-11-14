from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivymd.uix.label import MDLabel

from windows.Window import Window


class BalanceWindow(Window):
    def __init__(self, controller, **kw):
        super(BalanceWindow, self).__init__(controller, **kw)
        self.controller = controller

        self.title_label._set_text("Баланс")
        balance_amount_layout = AnchorLayout(anchor_x='center', anchor_y='center')
        self.balance_amount_label = MDLabel(text="", halign="center", font_size=200, md_bg_color=(1, 1, 1, 1),
                                            size_hint_y=None, height=144,
                                            size_hint_x=None, width=380,
                                            line_color=(.10, .44, .10, 1),
                                            max_lines=30)
        continuation_button = Button(text="Продолжить", background_color=(0.53, 0.71, .53, .6), size_hint=(0.45, 0.2),
                            on_press=lambda x: controller.set_present_screen_name("ContinuationWindow"))

        balance_amount_layout.add_widget(self.balance_amount_label)
        self.controlled_layout.add_widget(balance_amount_layout)

        continuation_button_layout = AnchorLayout(anchor_x='right', anchor_y='center')
        continuation_button_layout.add_widget(continuation_button)

        self.controlled_layout.add_widget(continuation_button_layout)

    def on_enter(self, *args):
        self.balance_amount_label.text = str(self.controller.get_balance())