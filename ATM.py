class ATM:
    def __init__(self, model, controller, view):
        self.model = model
        self.controller = controller
        self.view = view

    def work(self):
        # while self.view.get_present_screen_name() != "Stop":
        self.view.run()
