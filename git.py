account = {
    "name": "joy chepngeno",
    "age": 20,
    "balance": "5000",
    "registration_number": "1234",
    "university": "Kirinyaga university"
}
print("welcome to your school mini ATM")
registration_number = input("please enter your registration number: ")
if registration_number == account["registration_number"]:
    while True:
        print("***ATM MENU***")
        print("1.check balance ")
        print("2.withdraw cash ")
        print("3.deposit cash ")
        print("4.view balance")
        print("5.go back")
choice = input("enter your choice: ")
if choice == "1.":
    print("your balance is:", account["balance"])
