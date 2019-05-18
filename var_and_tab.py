name = "Никита"
print(name)

x = 0
while x < 10:
    print(x)
    x += 1



price = 100
discount = 5
price_with_discount = (price * discount/100)
# price(price_with_discount)

def discounted(price, discount):
    price_with_discount = price - (price * discount / 100)
    print(price_with_discount)



def get_summ(one, two, delimiter='&'):

    return '{} {}{}!'.format(one, delimiter, two)
   


 
    
two = "python"

print(get_summ("Learn", 2, '-'))