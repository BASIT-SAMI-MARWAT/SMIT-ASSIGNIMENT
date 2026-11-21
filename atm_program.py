account = {
"name": "Ali",
"pin": 1234,
"balance": 10000
}


def withdraw(balance, amount):
  if amount < balance or amount % 500 == 0:
    curent_balance = balance - amount
    return curent_balance
  else:
    return 0



attempts = 0
while attempts < 3:
  
  pin = int(input("Enter your PIN: "))
  if pin == account["pin"]:
    amount = int(input("Enter the amount of money you want to withdraw: "))
    result = withdraw(account['balance'],amount)
    if result != 0:
      print(f"You sucessfully withdrawed money:{amount}/-")
      print(f"Your current balance is:{result}/-")
      print("Thanks for using our ATM.")
      break
  else:
    attempts += 1
    if attempts >= 3:
      print("Your card is being captured because of to many tries.")
      continue
