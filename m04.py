class Commission():
    def __init__(self, no, amount1, amount2):
        self.no = no
        self.amount1 = amount1
        self.amount2 = amount2

    def total(self):
        if self.amount1 >= 300000:
            bonus1 = self.amount1 * 0.25
        elif self.amount1 >= 200000 and self.amount1 < 300000:
            bonus1 = self.amount1 * 0.2
        elif self.amount1 >= 100000 and self.amount1 < 200000:
            bonus1 = self.amount1 * 0.17
        else:
            bonus1 = self.amount1 * 0.12
        
        if self.amount2 >= 500000:
            bonus2 = self.amount2 * 0.35
        else:
            bonus2 = self.amount2 * 0.28
            
        return bonus1 + bonus2