# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 04:43:38 2020

@author: scker
"""

taxform = []
print("Welcome to the Family Tax Form 1")
taxform.append(float(input("1 Wages, salaries, and tips earned by the first spouse.  ")))
taxform.append(float(input("2 Wages, salaries, and tips earned by the second spouse.  ")))
taxform.append(float(input("3 Bonus earned by the family combined.  ")))
taxform.append(taxform[0]+taxform[1]+taxform[2])
print("4 Add lines 1, 2, and 3. This is your annual gross income.  $" + str("%.2f" % taxform[3]))
taxform.append(5000.00)
print("5 Standard health insurance deduction - $" + str("%.2f" % taxform[4]))
if taxform[4] > taxform[3]:
    taxform.append(0)
else:
    taxform.append(taxform[3] - taxform[4])
print("6 Subtract line 5 from line 4. If line 5 is larger than line 4, enter 0.")
print("This is your taxable income.  $" + str("%.2f" % taxform[5]))
taxform.append(float(input("7 Federal income tax withheld from paychecks for the first spouse.  ")))
taxform.append(float(input("8 Federal income tax withheld from paychecks for the second spouse.  ")))
taxform.append(taxform[6] + taxform[7])
print("9 Add lines 7 and 8. These are your total payments and credits.  $" + str("%.2f" % taxform[8]))
taxform.append(taxform[5] * 0.28)
print("10 Federal tax. Multiply line 6 by 0.28.  $" + str("%.2f" % taxform[9]))
taxform.append(float(input("11 Property tax to be owed.  ")))
taxform.append(taxform[9] + taxform[10])
print("12 Add lines 10 and 11. This is your total tax.  $" + str("%.2f" % taxform[11]))
taxform.append(taxform[11] - taxform[8])
if taxform[12] > 0:
    print("13 Subtract line 9 from line 12. For your taxes, you still owe $" + str("%.2f" % abs(taxform[12])))
else:
    print("13 Subtract line 9 from line 12. For your taxes, you have overpaid by $" + str("%.2f" % abs(taxform[12])))
