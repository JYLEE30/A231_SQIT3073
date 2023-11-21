import os

def calculate_MonthlyInstalment(principalLoanAmount, annualInterestRate, loanTerm):
    totalInstalmentNo = loanTerm * 12
    principalPerMonth = principalLoanAmount / totalInstalmentNo

    interestRatePerMonth = (annualInterestRate / 100) / 12
    interestPerMonth = principalLoanAmount * (interestRatePerMonth / (1 - (1 + totalInstalmentNo) ** -totalInstalmentNo))
    
    monthlyInstalment = principalPerMonth + interestPerMonth
    return monthlyInstalment

def calculate_TotalAmountPayable(principalLoanAmount, annualInterestRate, loanTerm):
    totalPrincipalInterest = principalLoanAmount*(annualInterestRate / 100)*loanTerm
    
    totalAmountPayable = principalLoanAmount + totalPrincipalInterest
    return totalAmountPayable

def calculate_DSR(applicantMonthlyIncome, otherMonthlyFinancialCommitments, monthlyInstalment):
    totalCommitmentsPerMonth = otherMonthlyFinancialCommitments + monthlyInstalment
    
    dSR = (totalCommitmentsPerMonth / applicantMonthlyIncome) * 100
    return dSR

class loanRecord:
    def __init__(self, principalLoanAmount, monthlyInstalment, totalAmountPayable, dSR, eligibility):
        self.principalLoanAmount = principalLoanAmount
        self.monthlyInstalment = monthlyInstalment
        self.totalAmountPayable = totalAmountPayable
        self.dSR = dSR
        self.eligibility = eligibility

def display_PreviousLoanCalculations(previousLoanCalculations):
    print("\nPrevious Loan Calculation Records")

    i=1
    for r in previousLoanCalculations:

        print("\nRecord " + str(i) 
            + "\nPrincipal: RM " + str(round(r.principalLoanAmount,2)) 
            + "\nMonthly Instalment: RM " + str(round(r.monthlyInstalment,2))
            + "\nTotal Amount Payable: RM " + str(round(r.totalAmountPayable,2))
            + "\nDSR: " + str(round(r.dSR,2)) + "%" 
            + "\nEligibility :" + str(r.eligibility))
        i += 1

def delete_PreviousLoanCalculations(previousLoanCalculations):
    try:
        d = int(input("\nPlease select the record you want to delete: "))
        del previousLoanCalculations[d-1]
        print("\nSelected record succesfully deleted!")
    except:
        print("\nCannot find record! Please select a valid record: ")