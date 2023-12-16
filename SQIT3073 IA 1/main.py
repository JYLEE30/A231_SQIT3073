# Import operating system
import os
os.system('cls')

# Import House_Loan_Calculations.py
import House_Loan_Calculations as HLC

# Create new list
previousLoanCalculations = []

# Print headings
print("\n--------------- Welcome to House Loan Calculator ---------------")


while True:
    # Menu instruction
    print("\nPlease choose what you want to do...")
    print("\nPress button 1 to calculate new loan")
    print("Press button 2 to view past record")
    print("Press button E to exit calculator")
    
    menuSelection1 = input("\nPlease enter an action: ")
    
    # Calculate new loan
    if menuSelection1 == "1":
        # Key in new loan details
        principalLoanAmount = float(input("\nPlease enter your Principal Loan Amount: RM "))
        annualInterestRate = float(input("Please enter your Annual Interest Rate: "))

        # Check loan tenure validity
        lT = True
        while lT:
            loanTerm = int(input("Please enter your Loan Term (in years): "))
            if loanTerm > 35:
                print("\nThe maximum loan term is 35 years only.\n")
            elif loanTerm < 1:
                print("\nThe minimum loan term is at least 1 year.\n")
            else:
                lT = False

        applicantMonthlyIncome = float(input("Please enter your Monthly Income: RM "))
        otherMonthlyFinancialCommitments = float(input("Please enter your Other Monthly Financial Commitments: RM "))

        # Calculate Monthly Instalment, Total Amount Payable, DSR
        monthlyInstalment = HLC.calculate_MonthlyInstalment(principalLoanAmount, annualInterestRate, loanTerm)
        totalAmountPayable = HLC.calculate_TotalAmountPayable(principalLoanAmount, annualInterestRate, loanTerm)
        dSR = HLC.calculate_DSR(applicantMonthlyIncome, otherMonthlyFinancialCommitments, monthlyInstalment)

        # Check eligibility using DSR
        if dSR <= 70:
            eligibility = "Eligible to get the loan as your Debt Service Ratio is below 70%" 
        elif dSR > 70:
            eligibility = "Not Eligible to get the loan as your Debt Service Ratio is above 70%"

        # Add new record into the list
        previousLoanCalculations.append(HLC.loanRecord(principalLoanAmount, monthlyInstalment, totalAmountPayable, dSR, eligibility))

        # Display calculated values and eligibility
        print(f"\nMonthly Instalment: RM {round(monthlyInstalment,2)}")
        print(f"Total Amount Payable: RM{round(totalAmountPayable,2)}")
        print(f"Debt Service Ratio (DSR): {round(dSR,2)}%")
        print(f"Eligibility: {eligibility}")

        input("\nTo continue, please press enter...")
        continue
    
    # View all records in list
    if menuSelection1 == "2":
        if len(previousLoanCalculations) == 0:
            print("\nNo past records in the list...")
            input("\nTo continue, please press enter...")
            continue
        else:
            HLC.display_PreviousLoanCalculations(previousLoanCalculations)
            
            # Delete record in list selections
            print("\nTo delete past data please press button D.")
            print("To return, please press enter...")

            menuSelection2 = input("\nPlease enter an action: ")
            if menuSelection2 == "d" or menuSelection2 == "D":
                HLC.delete_PreviousLoanCalculations(previousLoanCalculations)
            else:
                continue
            
    # End calculator
    elif menuSelection1 == "e" or menuSelection1 == "E":
        print("\nThank you for using, feel free to come back again ~\n")
        exit()

    # Invalid action
    else:
        print("\nInvalid input! Please enter a valid input to continue...")