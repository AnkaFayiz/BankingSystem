import sys
class Bank:
    def __init__(self, accNo, name):
        self.accno = accNo
        self.name = name
        self.balance = 0

    def display_information(self):
        print(f"Account Number : {self.accno}")
        print(f"Account Name : {self.name}")
        print(f"Balance : {self.balance}")

    def check_balance(self):
        if self.balance != 0:
            return self.balance
        else:
            self.run()

    def deposit(self):
        print(f"Balance : {self.balance}")
        addingBalance = int(input("Enter the amount (minimum $100) : "))
        
        self.balance += addingBalance
        return self.balance
            
    def withdraw(self):
        print(f"Balance : {self.balance}")
        if self.balance != 0:
            draw = int(input("Enter the amount you want to draw : "))
            
            # Check if the amount to withdraw is not bigger than 
            # balance itself
            if draw < self.balance:
                self.balance = self.balance -  draw
                
                print(f"Balance : {self.balance}")
            else:
                print("You have insufficient amount on your account!")
                self.withdraw()
        else:
            print("Insufficient amount on your account!")
            print("Please deposit to your account! ")
            self.run()
    
    def change_information(self):
        self.display_information()

        askUserForChange = input("\nYou want to change information of your account(y/n) : ")
        
        if str.lower(askUserForChange) == 'y':
            print("You can only change the name of the account holder " )
            print(f"Account Number : {self.accno} ")
            print(f"Account holder name : {self.name} ")

            changeName = input("Enter the holder card name : " )
            
            self.name = changeName
            return self.name
        
        else:
            self.run()

    def banner(self):
        print("         Menu        ")
        print("1. Display Information ")
        print("2. Withdraw ")
        print("3. Deposit ")
        print("4. Change Information " )
        print("5. Exit")

    def exit(self):
        print("Thank you for using our service")
        sys.exit(0)

    def run(self):
        while True:
            self.banner()
            ch = int(input("Choose 1-8 : "))

            if ch == 1:
                self.display_information()
            elif ch == 2:
                self.withdraw()
            elif ch == 3:
                self.deposit()
            elif ch == 4:
                self.change_information()
            else:
                self.exit()

# Creating class object
while True:

    accno = int(input("Enter the account number : " ))
    name = input("Enter the holder card name : ")

    if len(str(accno)) == 8:
        obj = Bank(accno, name)
        obj.run()
    else:
         print("Account number is not sufficient!")
# Created By Anka
