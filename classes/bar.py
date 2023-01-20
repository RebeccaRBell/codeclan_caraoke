class Bar:
    def __init__(self, cash, drinks):
        self.cash = cash
        self.drinks = drinks

    def sell_a_drink(self, drink):
        self.cash += self.drinks[drink]["price"]
        return self.cash

    