from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from windows.Window import Window


class CashWithdrawalWindow(Window):
    def __init__(self, controller, **kw):
        super(CashWithdrawalWindow, self).__init__(controller, **kw)

        self.title_label._set_text("Выберите сумму")

        button_layout = GridLayout(cols=2)
        choice_button_1 = Button(text="1. 10", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.5),
                                 on_press=lambda x: controller.set_present_screen_name("OperationCompletedWindow"))
        choice_button_2 = Button(text="2. 20", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.5),
                                 on_press=lambda x: controller.set_present_screen_name("OperationCompletedWindow"))
        choice_button_3 = Button(text="3. 50", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.5),
                                 on_press=lambda x: controller.set_present_screen_name("OperationCompletedWindow"))
        choice_button_4 = Button(text="4. 100", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.5),
                                 on_press=lambda x: controller.set_present_screen_name("OperationCompletedWindow"))
        choice_button_5 = Button(text="5. 200", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.5),
                                 on_press=lambda x: controller.set_present_screen_name("OperationCompletedWindow"))
        choice_button_6 = Button(text="6. 500", background_color=(0.53, 0.71, .53, .6), size_hint=(0.9, 0.5),
                                 on_press=lambda x: controller.set_present_screen_name("OperationCompletedWindow"))

        choice_button_1_layout = AnchorLayout(anchor_x='left', anchor_y='center')
        choice_button_1_layout.add_widget(choice_button_1)

        choice_button_5_layout = AnchorLayout(anchor_x='right', anchor_y='center')
        choice_button_5_layout.add_widget(choice_button_5)

        choice_button_2_layout = AnchorLayout(anchor_x='left', anchor_y='center')
        choice_button_2_layout.add_widget(choice_button_2)

        choice_button_6_layout = AnchorLayout(anchor_x='right', anchor_y='center')
        choice_button_6_layout.add_widget(choice_button_6)

        choice_button_3_layout = AnchorLayout(anchor_x='left', anchor_y='center')
        choice_button_3_layout.add_widget(choice_button_3)

        choice_button_4_layout = AnchorLayout(anchor_x='right', anchor_y='center')
        choice_button_4_layout.add_widget(choice_button_4)

        button_layout.add_widget(choice_button_1_layout)
        button_layout.add_widget(choice_button_5_layout)
        button_layout.add_widget(choice_button_2_layout)
        button_layout.add_widget(choice_button_6_layout)
        button_layout.add_widget(choice_button_3_layout)
        button_layout.add_widget(choice_button_4_layout)
        self.controlled_layout.add_widget(button_layout)