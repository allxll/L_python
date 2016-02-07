balance = 320000
annualInterestRate = 0.2
lowerBound = balance / 12.0
upperBound = (balance * (1 + annualInterestRate/12)**12) / 12.0
print(lowerBound, upperBound)
while (upperBound - lowerBound) >= 0.01:
    pay = (upperBound + lowerBound) / 2
    bala = balance
    for i in range(12):
        bala = (bala - pay) * (1 + annualInterestRate/12)
        print(bala)
    if bala > 0:
        lowerBound = pay
    elif bala < 0:
        upperBound = pay


print('Lowerst Payment: %s' % round(upperBound, 2))
print(lowerBound)
