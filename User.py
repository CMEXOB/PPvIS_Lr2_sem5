from Card import Card


class User:

    def __init__(self):
        self.cards = []

    def add_card(self, added_card):
        if not added_card in self.cards:
            self.cards.append(added_card)

    def get_cards(self):
        return self.cards
