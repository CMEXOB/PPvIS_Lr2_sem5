from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

from Card import Card
from windows.Window import Window


class StartWindow(Window):
    def __init__(self, controller, **kw):
        super(StartWindow, self).__init__(controller, **kw)

        self.title_label._set_text("Вставьте карту")
        cards_buttons = GridLayout(cols=4)
        index_of_card = 1
        self.controlled_layout.add_widget(cards_buttons)
        cards = []
        cards.append(Card(13545214, 1478, 265, False))
        for card in cards:
            name = str.format("{0}. Карта:\n{1}", index_of_card,card.card_number)
            cards_buttons.add_widget(
                Button(text=name, on_press=lambda x: controller.set_present_screen_name("LoginWindow")))
            index_of_card += 1
        while index_of_card < 20:
            cards_buttons.add_widget(Widget())
            index_of_card += 1

