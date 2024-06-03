class UPI:
    def __init__(self):
        self.name = ""
        self.account = 0
        self.upi_pin = 0
        self.new_upi_pin = 0
        self.bank_account = 0
        self.acc_balance = 0
        self.attempts = 0
        self.transfer_amount = 0
        self.deposit_amount = 0
        self.transaction_history = []
     
    def register(self):
        print("Enter you Name :")
        self.name = input()
        print("Enter your UPI account number : ")
        self.account = int(input())
        print("Enter your UPI PIN : ")
        self.upi_pin = int(input())
        print("Enter your bank account number : ")
        self.bank_account = int(input())
        print("Enter your bank balance : ")
        self.acc_balance = int(input())
        with open('data.txt', 'w') as f:
            f.write(f'Name: {self.name}\n')
            f.write(f'UPI Account Number: {self.account}\n')
            f.write(f'UPI PIN: {self.upi_pin}\n')
            f.write(f'Bank Account Number: {self.bank_account}\n')
            f.write(f'Bank Balance: {self.balance}\n')
        self.menu()
        print()
        print()
        print()
       
    def login(self):
        print("Enter your UPI account number : ")
        self.account = int(input())
        print("Enter your UPI PIN : ")
        self.upi_pin = int(input())
        print("Enter your bank account number : ")
        self.bank_account = int(input())
        print("Enter your bank balance : ")
        self.acc_balance = int(input())
        with open('data.txt', 'a') as f:
            f.write(f'\nLogin Data:\n')
            f.write(f'UPI Account Number: {self.account}\n')
            f.write(f'UPI PIN: {self.upi_pin}\n')
            f.write(f'Bank Account Number: {self.bank_account}\n')
            f.write(f'Bank Balance: {self.balance}\n')
        self.menu()
        print()
        print()
        print()
    
        
    def menu(self):
        print("1. Transfer\n2. Deposit\n3. Balance\n4. Change UPI PIN\n5. Transactions\n6. Exit")
        option = int(input())
        if option == 1:
            self.transfer()
        elif option == 2:
            self.deposit()
        elif option == 3:
            self.balance()
        elif option == 4:
            self.change_upi_pin()
        elif option == 5:
            self.transactions()
        elif option == 6:
            print("Exit")
        else:
            print("Invalid option")
            self.menu()
    
    def transfer(self):
        print("Enter the amount to transfer : ")
        self.transfer_amount = int(input())
        print("Enter the UPI account number to transfer : ")
        account = int(input())
        print("Enter the UPI PIN to transfer : ")
        upi_pin = int(input())
        if self.upi_pin == upi_pin and self.balance >= self.transfer_amount:
            self.balance -= self.transfer_amount
            self.transaction_history.append("Transfered " + str(self.transfer_amount) + " to " + str(account))
            print("Transfer successful")
        else:
            print("Transfer failed")
        self.menu()
        print()
        print()
        print()
    
    def deposit(self):
        print("Enter the amount to deposit : ")
        deposit_amount = int(input())
        print("Enter the UPI PIN to deposit : ")
        upi_pin = int(input())
        if self.upi_pin == upi_pin:
            self.balance += deposit_amount
            print("Deposit successl")
        else:
            print("Deposit failed")
        self.menu()
        print()
        print()
        print()
    
    def balance(self):
        print("Your balance is : ", self.acc_balance)
        self.menu()
        print()
        print()
        print()
    
    def change_upi_pin(self):
        print("Enter the new UPI PIN : ")
        new_upi_pin = int(input())
        print("Re-enter the new UPI PIN : ")
        re_new_upi_pin = int(input())
        if new_upi_pin == re_new_upi_pin:
            self.upi_pin = new_upi_pin
            print("UPI PIN changed successfully")
        else:
            print("UPI PIN not matched. Re-enter again")
        self.menu()
        print()
        print()
        print()
    
    def transactions(self):
        print("Transaction History:")
        for transaction in self.transaction_history:
            print(transaction)
        self.menu()
        print()
        print()
        print()

obj = UPI()__
print("1. Register\n2. Login")
option = int(input())
if option == 1:
    obj.register()
elif option == 2:
    obj.login()
else:
    print("Invalid option")