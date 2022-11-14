from ATM import ATM
from Card import Card
from Controller import Controller
from Model import Model
from User import User
from View import View

if __name__ == '__main__':
    egor = User()
    card1 = Card(13545214, 1478, 265, False)
    card2 = Card(43141140, 8741, 9915, False)
    model = Model()
    controller = Controller(model)
    view = View(model, controller)
    controller.set_view(view)
    atm = ATM(model, controller, view)
    atm.work()
