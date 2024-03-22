total_price = 0
DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.1
item_quantity = int(input("Number of items: "))
while item_quantity < 0:
    print("Invalid number of items!")
    item_quantity = int(input("Number of items: "))
for i in range(item_quantity):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > DISCOUNT_THRESHOLD:
    discount = DISCOUNT_RATE * total_price
    total_price -= discount
print(f"Total price for {item_quantity} items is ${total_price:.2f}")
