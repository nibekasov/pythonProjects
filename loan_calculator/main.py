import math

def calculate_months(principal, monthly_payment):
    return math.ceil(principal / monthly_payment)

def calculate_payment(principal, num_months):
    monthly_payment = math.ceil(principal / num_months)
    last_payment = principal - (num_months - 1) * monthly_payment
    return monthly_payment, last_payment

while True:
    principal = float(input("Enter the loan principal:\n"))
    action = input("What do you want to calculate?\ntype \"m\" for number of monthly payments,\ntype \"p\" for the monthly payment:\n")

    if action == 'm':
        monthly_payment = float(input("Enter the monthly payment:\n"))
        num_months = calculate_months(principal, monthly_payment)
        if num_months == 1:
            print(f"It will take {int(num_months)} month to repay the loan")
        else:
            print(f"It will take {int(num_months)} months to repay the loan")
        break
    elif action == 'p':
        num_months = int(input("Enter the number of months:\n"))
        monthly_payment, last_payment = calculate_payment(principal, num_months)
        if last_payment == monthly_payment:
            print(f"Your monthly payment = {int(monthly_payment)}")
            break
        else:
            print(f"Your monthly payment = {int(monthly_payment)} and the last payment = {int(last_payment)}.")
            break
    else:
        print("Invalid input. Please enter 'm' or 'p'.")

    #another_calculation = input("Do you want to perform another calculation? (yes/no):\n")
    #if another_calculation.lower() != 'yes':
    #    print("Thank you for using the loan repayment calculator!")
    #    break
