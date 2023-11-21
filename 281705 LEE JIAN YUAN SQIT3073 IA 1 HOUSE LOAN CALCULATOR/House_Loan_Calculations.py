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

def display_previous_calculations(previousLoanCalculations):
    print("\nPrevious Loan Calculations:")
    i=1
    for record in previousLoanCalculations:
        
        print(str(i) + ". Principal: RM " + str(round(record.principal,2)) 
        + ",\n   Monthly Instalment: RM " + str(round(record.monthly_payment,2))
        + ",\n   Total Amount Payable: RM " + str(round(record.total_amount,2))
        + ",\n   DSR: " + str(round(record.dsr,2)) + "%" 
        + ",\n   Eligibility :" + str(record.eligibility))
        print()
        i+=1

    print() 
    input("Press Enter to continue....")