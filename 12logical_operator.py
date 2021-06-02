# The logical operator is used when you wanna check more than one condition.
# Example - Loan eligibility - High Income & good credit score.

high_income = True
good_credit_score = False

# The 'and' operator
if high_income and good_credit_score:
    # these lines of code gets executed if both the conditions are True
    print("You are welcome to take loan!")
else:
    print("Better luck next time!!")

# The 'or' operator
# Example - Loan sanction - High Income or good credit score.
if high_income or good_credit_score:
    # these lines of code get's executed if one of the condition is True
    print("Loan Sanctioned")
else:
    print("your loan is under process!")

# The 'not' operator is used to reverse the operation
if not high_income:
    print("You should make your income high!!")
