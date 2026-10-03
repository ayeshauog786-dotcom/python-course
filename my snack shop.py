snack_name = "chips"
price = 1.50
quantity = 10
is_available = True
print(snack_name)
print(price)
print(quantity)
print(is_available)
print(type(snack_name))
print(type(price))
print(type(quantity))
print(type(is_available))
total_value = price * quantity
print("Total price is: ",total_value)
sale_price = price - 0.25
print("sale price is: ",sale_price)
print("double stock: ",quantity * 2)
print("price under 2$: ",price < 2)
print("more than 5 snacks: ",quantity > 5)
print("price is exactly $1.50: ",price == 1.50)
shop_name = "My " + "Snack " + "Shop"
print(shop_name)
print(len(snack_name))
print(snack_name[0])
price1 = 1.50
price2 = 3.00
print("before swap")
print("price1 = ",price1)
print("price2 = ",price2)
temp = price1
price1 = price2
price2 = temp
print("after swap")
print("price1 = ",price1)
print("price2 = ",price2)
