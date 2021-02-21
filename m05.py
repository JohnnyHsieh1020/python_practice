class Commission():
    def __init__(self, no, amount, division):
        self.no = no
        self.amount = amount
        self.division = division

    def total(self):
        if self.division == '北區':
            if self.amount >= 500000:
                bonus1 = self.amount * 0.28
            elif self.amount >= 300000 and self.amount < 500000:
                bonus1 = self.amount * 0.23
            elif self.amount >= 100000 and self.amount < 300000:
                bonus1 = self.amount * 0.17
            else:
                bonus1 = self.amount * 0.12
            return bonus1
        else:
            if self.amount >= 300000:
                bonus2 = self.amount * 0.22
            else:
                bonus2 = self.amount * 0.17
            return bonus2
