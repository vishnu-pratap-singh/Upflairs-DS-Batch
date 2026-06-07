class Atm:
    # Function within a class is called a method
    # Constructor: special method that automatically executes when an object is created
    def __init__(self):
        self.pin = ""
        self.balance = 10000
        self.menu()  # Fixed spelling here

    def menu(self):  # Fixed spelling: removed the extra 'e'
        user_input = input("""
        Hello, how would you like to proceed 
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
        
        Selection: """) # Removed sbi=Atm() from here to stop the infinite loop
        
        # Added quotes because input() returns a string
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":  # Option 2 is deposit
            self.deposite()
        elif user_input == "3":  # Option 3 is withdraw
            self.withdraw()
        elif user_input == "4":
            self.check_blance()
        else:
            print("bye")
    
    def create_pin(self):
        self.pin = input("Enter your pin: ")
        print("Pin set successfully")
        # self.menu()  # Loops back to menu after action
     
    def deposite(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter the Amount: "))
            self.balance = self.balance + amount
            print("Deposit successful")
        else:
            print("Invalid pin")
        # self.menu()  # Loops back to menu
            
    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.pin:
            amount = int(input("Enter Amount: "))
            if amount <= self.balance:  # Changed to <= so you can withdraw full balance
                self.balance = self.balance - amount
                print("Operation successful")
            else:
               print("Insufficient funds")
        else:
            print("Invalid pin") 
        # self.menu()  # Loops back to menu

    def check_blance(self):
        temp = input("Enter pin: ")
        if temp == self.pin:
            print(f"Your balance is: {self.balance}")
        else:
            print("Invalid pin")
        # self.menu()  # Loops back to menu

# --- OBJECT CREATION OUTSIDE THE CLASS ---
# This starts the whole program safely
# sbi = Atm()

