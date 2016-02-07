balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid = 0
for i in range(12):
    print('Month: %d' % (i + 1))
    monthlyPaid = balance * monthlyPaymentRate
    totalPaid += monthlyPaid
    print('Minimum monthly payment: %f' % round(monthlyPaid, 2))
    balance = (balance - monthlyPaid) * (1 + annualInterestRate / 12)
    print('Remaining balance: %f' % round(balance, 2))
    if i == 11:
        print('Total paid: %f' % round(totalPaid, 2))
        print('Remaining balance: %f' % round(balance, 2))
