# this is my 1st project
account = {
    "name": "Joy_chepngeno",
    "balance": "50500",
    "pin": "1234",
    "type": "businessaccount"
}
print("===MINI ATM===")
pin = input("enter your pin:")
if pin == account["pin"]:
    while True:
        print("***ATM MENU***")
        print("1.Check balance")
        print("2.deposit money")
        print("3.withdraw money")
        print("4.account details")
        print("5.exit")
        choice = input("enter your choice:")
        if choice == "1":
            print("your balance is:", account["balance"])
        elif choice == "2":
            amount = input("enter your amount:")
            if amount >= "0":
                account["balance"] = account["balance"] + amount
                print("money deposited successfully")
                print("collect your cash.")
                print("new balance", account["balance"])
        elif choice == "4":
            print("\nAccount name", account["name"])
            print("\nAccount balance", account["balance"])
            print("\nAccount type", account["type"])
        elif choice == "5":
            print("thank you")
            break
        else:
            print("invalid choice")
    else:
        print("invalid pin")
print("access denied")
