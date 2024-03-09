
shoppingCart = []

item = input('Enter the name of the product: ')
shoppingCart.append(item)

item = input('Enter the name of the product: ')
shoppingCart.append(item)

item = input('Enter the name of the product: ')
shoppingCart.append(item)

print('Shopping cart: ', shoppingCart)
print(len(shoppingCart))

shoppingCart.remove('salam')

print('Shopping cart: ', shoppingCart)

shoppingCart.pop(0)

print('Shopping cart: ', shoppingCart)

shoppingCart.clear()

if len(shoppingCart) == 0:
    print('Shopping list is empty')