import math
#allows certain math procedures to be possible

print("Options-\ninvestment - calculates the amount of interest earned on interest\nbond - calculates the amount you'll have to pay on home loan")
#displays a text of options for user

typ = input("Enter 'investment' or 'bond' in order to proceed: ")
#asks for option chosen by user

#if user entered investment the following block will calculate simple or compound interest, depending on the user's input
if typ == "Investment" or typ == "INVESTMENT" or typ == "investment" :
    dep = float(input("Enter deposit amount: "))
    rate = float(input("Enter the interest rate: "))/100 #added the '/100' for percentage
    noYear = float(input("Enter amount of years for investment: "))
    interest = input("Enter 'simple' or 'compound' interest: ")
    if interest == "simple" or interest == "SIMPLE" or interest == "Simple":
        simp_int = round(dep * (1 + rate * noYear), 2)
        print("Simple interest: R" + str(simp_int))
    else:
        comp_int = round(dep * math.pow((1 + rate), noYear), 2)
        print("Compound interest: R" + str(comp_int))

#the following block will calculate bond
elif typ == "bond" or typ == "Bond" or typ == "BOND" :
    presVal = float(input("Enter present value: "))
    r = float(input("Enter interest rate: ")) / 100 /12 #the added "/12" is compounded monthly
    noMonth = float(input("Enter planned amount of months taken to repay bond: "))
    bond = round((r * presVal) / (1 - (1 + r) ** (-noMonth)), 2)
    print("Bond Monthly Payment: " + str(bond))