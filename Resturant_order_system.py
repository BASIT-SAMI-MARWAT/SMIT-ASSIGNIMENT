menu = {
"Biryani": 350,
"Karahi": 1200,
"Naan": 50,
"Tea": 100
}




def calculate_item_total(price, quantity):
  return price * quantity



total = 0

for item,price in menu.items():
  print(item,price)

while True:

 item = input("Enter item name or done: ").title()

 if item == "Done":
  break
 
 elif item in menu:
  quantity = int(input("Enter the quantity of item you selected: "))
  price = menu[item]
  total += calculate_item_total(price,quantity)

 else:
  print("Item not available in menu")


print("Total bill:", total)