amount = float(input("Amount: "))
interest = float(input("Interest: "))
years = int(input("Years: "))

balance = amount * (1 + (interest/100))**years

print(f"Balance: {balance:.6f}")