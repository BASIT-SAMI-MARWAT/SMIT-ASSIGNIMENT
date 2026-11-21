products = {
"Milk": 250,
"Bread": 150,
"Eggs": 400,
"Rice": 1200
}


def calculate_discount(total_bill: int):
    if total_bill >= 5000:
        discount = (10/100) * total_bill 
        return discount
    else:
        return 0



bill = 0

for product , price in products.items():
    print(product,price)
while True:

    customer_choice = input("Buy product: ")
    if customer_choice == "done":
        break
    if customer_choice == "Milk":
        bill += 250
    elif customer_choice == "Bread":
        bill += 150
    elif customer_choice == "Eggs":
        bill += 400
    elif customer_choice == "Rice":
        bill += 1200
    else:
        print("invalid choice")

discount = calculate_discount(bill)

final = bill-discount

print(f'total_bill:{bill}, discount:{discount}, final_bill:{final}')

    


