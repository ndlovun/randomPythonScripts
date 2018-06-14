#Write a function that takes two arguments, an amount in dollars and a tax percentage.
#Return an array with the tax amount in cents.

def calTaxes(Amnt, tax):
    arr = []
    arr = (Amnt * (tax / 100))*100
    return arr


my_taxes = calTaxes(100, 5)
print(my_taxes)
