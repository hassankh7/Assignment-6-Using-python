

# Assignment: Bank Class with Class Variable and Class Method

class Bank:
    # Class variable
    bank_name = "National Bank"

    def __init__(self, account_holder):
        self.account_holder = account_holder

    def display_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Bank Name: {Bank.bank_name}")

    # Class method to change the bank name
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name


# Create instances of Bank
acc1 = Bank("Haris")
acc2 = Bank("Ali")

# Display info before changing bank name
print("Before changing bank name:")
acc1.display_info()
acc2.display_info()

print("\nChanging bank name...\n")
# Change the bank name using class method
Bank.change_bank_name("Future Bank")

# Display info after changing bank name
print("After changing bank name:")
acc1.display_info()
acc2.display_info()