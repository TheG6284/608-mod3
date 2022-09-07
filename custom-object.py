class Purchase(object):
    def __init__(self, amount):
        self.amount = amount

    def calcTax(self, taxPercent):
        return self.amount * taxPercent/100.00

    def calcTip(self, tipPercent):
        return self.amount * tipPercent/100.00

    def calcTotal(self, taxPercent, tipPercent):
        return self.amount*(1 + taxPercent/100.00 +tipPercent/100.00)

purchase = Purchase(100.00)

taxPercent = 8.0
tipPercent = 15.0

print('Tax: ' + str(purchase.calcTax(taxPercent)))
print('Tip: ' + str(purchase.calcTip(tipPercent)))
print('Total: ' + str(purchase.calcTotal(taxPercent, tipPercent)))

