import sys
if len(sys.argv) == 4:
    withdraw_amount = float(sys.argv[1])
    balance = float(sys.argv[2])
    pin = sys.argv[3]
    print(f"ATM withdrawal amount is: {withdraw_amount}")
    print(f"Balance is: {balance}")
    print(f"PIN is: {pin}")
else:
    
    withdraw_amount = 500
    balance = 2000
    pin = 636360
print(f"ATM withdrawal amount is: {withdraw_amount}")
print(f"Balance is: {balance}")
print(f"PIN is: {pin}")


if balance > withdraw_amount:
    print("\nThe transaction is approved")
else:
    print("\nThe transaction is declined")
