

def clear_screen(line):
    print('\n'*line)

def Main():
    incomeDT = ['Self', 'Sponsor']


    #    self_income = input("Income for the year of assessment of Self:")
#    sponsor_income = input("Income for the year of assessment of Spouse:")


#    spouse_income = 10000

#    print('%34s%10s%10s'%("", incomeDT[0], incomeDT[1]))

    clear_screen(5)
    self_allowance = 132000
    spouse_allowance = 132000
    family_allowance = 264000


    lines = []
    while True:
        s = input("Enter the self and spouse income (eg. 100000 20000) or press ENTER to end: ")
        if s:
            lines.append(s)
        else:
            break

    print("OUTPUT: ")
    for i in lines:
#        print(i)
        x, y = i.split()
#        print(x,y)

        self_income = int(x)
        spouse_income = int(y)
        family_income = self_income + spouse_income

#        self_income = 300000
#        spouse_income = 300000
#        family_income = 600000

        self_MPF = Calc_MPF(self_income)
        spouse_MPF = Calc_MPF(spouse_income)
        family_MPF = self_MPF + spouse_MPF

        self_Netincome, self_ChargeIncome, self_Charge1st50K, self_Charge2nd50K, self_Charge3rd50K, self_Charge4th50K, self_ChargeRemain, self_StandardTax, self_ChargeTotal = person_Charge(self_income, self_allowance, self_MPF)
        spouse_Netincome, spouse_ChargeIncome, spouse_Charge1st50K, spouse_Charge2nd50K, spouse_Charge3rd50K, spouse_Charge4th50K, spouse_ChargeRemain, spouse_StandardTax, spouse_ChargeTotal = person_Charge(spouse_income, spouse_allowance, spouse_MPF)
        family_Netincome, family_ChargeIncome, family_Charge1st50K, family_Charge2nd50K, family_Charge3rd50K, family_Charge4th50K, family_ChargeRemain, family_StandardTax, family_ProgChargeTotal = person_Charge(family_income, family_allowance, family_MPF)

        total_StadCharge = self_StandardTax + spouse_StandardTax
        total_ProgCharge = self_ChargeTotal + spouse_ChargeTotal

        print('%30s%20s%10s' % (" ", "Seperated ", "Jointed"))
        print('%30s%10s%10s%10s'%("Personal:", "self", "spouse", ""))
        print('%30s%10.0f%10.0f%10.0f'%("Total Income:", self_income, spouse_income, family_income))
        print('%30s%10.0f%10.0f%10.0f'%("(a) MPF Contribution:", self_MPF, spouse_MPF, family_MPF))
        print('%30s%10.0f%10.0f%10.0f'%("Total Net Income:", self_Netincome, spouse_Netincome, family_Netincome))
        print('%30s%10.0f%10.0f%10.0f'%("Total Allowance:", self_allowance, spouse_allowance, family_allowance))
        print('%30s%10.0f%10.0f%10.0f'%("Net Chargeable Income:", self_ChargeIncome, spouse_ChargeIncome, family_ChargeIncome))
        print('%30s%10.0f%10.0f%10.0f'%("On the 1st 50,000 at 2%:", self_Charge1st50K, spouse_Charge1st50K, family_Charge1st50K))
        print('%30s%10.0f%10.0f%10.0f'%("On the 2nd 50,000 at 6%", self_Charge2nd50K, spouse_Charge2nd50K, family_Charge2nd50K))
        print('%30s%10.0f%10.0f%10.0f'%("On the 3rd 50,000 at 10%:", self_Charge3rd50K, spouse_Charge3rd50K, family_Charge3rd50K))
        print('%30s%10.0f%10.0f%10.0f'%("On the 4th 50,000 at 14%:", self_Charge4th50K, spouse_Charge4th50K, family_Charge4th50K))
        print('%30s%10.0f%10.0f%10.0f'%("Charge Remain:", self_ChargeRemain, spouse_ChargeRemain, family_ChargeRemain))
        print('%30s%10.0f%10.0f%10.0f'%("Tax Payable (Standard):", self_StandardTax, spouse_StandardTax, family_StandardTax))
        print('%30s%20.0f%10.0f'%("Total Tax Payable (Standard):", total_StadCharge, family_StandardTax))
        print('%30s%10.0f%10.0f%10.0f'%("Tax Payable (Progressive):", self_ChargeTotal, spouse_ChargeTotal, family_ProgChargeTotal))
        print('%30s%20.0f%10.0f'%("Total Tax Payable (Progressive):", total_ProgCharge, family_ProgChargeTotal))

        if total_StadCharge < family_StandardTax:
            if total_ProgCharge < family_ProgChargeTotal:
                if total_ProgCharge < total_StadCharge:
                    print('%30s%10.0f%10s%10.0f'%("Because Total Payable (Standard):", total_StadCharge, " < ", family_StandardTax))
                    print('%30s%10.0f%10s%10.0f'%("Because Total Payable (Progressive):", total_ProgCharge, " < ", family_ProgChargeTotal))
                    print('%30s%10.0f%10s%10.0f'%("Because Total Payable:", total_ProgCharge, " < ", total_StadCharge))
                    print("(d) Recommend to Separated Tax in Progressive Rate")
                else :
                    print('%30s%10.0f%10s%10.0f'%("Because Total Payable (Standard):", total_StadCharge, " < ", family_StandardTax))
                    print('%30s%10.0f%10s%10.0f'%("Because Total Payable (Progressive):", total_ProgCharge, " < ", family_ProgChargeTotal))
                    print('%30s%10.0f%10s%10.0f'%("Because Total Payable:", total_ProgCharge, " > ", total_StadCharge))
                    print("(d) Recommend to Separated Tax in Standard Rate")
            else:
                if family_ProgChargeTotal < total_StadCharge:
                    print('%30s%10.0f%10s%10.0f'%("Because Total Payable (Standard):", total_StadCharge, " < ", family_StandardTax))
                    print('%30s%10.0f%10s%10.0f'%("Because Total Payable (Progressive):", family_ProgChargeTotal, " < ", total_ProgCharge))
                    print('%30s%10.0f%10s%10.0f'%("Because Total Payable:", family_ProgChargeTotal, " < ", total_StadCharge))
                    print("(d) Recommend to Jointed Tax in Progressive Rate")
                else :
                    print('%30s%10.0f%10s%10.0f'%("Because Total Payable (Standard):", total_StadCharge, " < ", family_StandardTax))
                    print('%30s%10.0f%10s%10.0f'%("Because Total Payable (Progressive):", total_ProgCharge, " < ", family_ProgChargeTotal))
                    print('%30s%10.0f%10s%10.0f'%("Because Total Payable:", family_ProgChargeTotal, " > ", total_StadCharge))
                    print("(d) Recommend to Seperated Tax in Standard Rate")
        else:
            if total_ProgCharge < family_ProgChargeTotal:
                if total_ProgCharge < family_StandardTax:
                    print('%30s%10.0f%10s%10.0f' % ("Because Total Payable (Standard):", total_StadCharge, " > ", family_StandardTax))
                    print('%30s%10.0f%10s%10.0f' % ("Because Total Payable (Progressive):", total_ProgCharge, " < ", family_ProgChargeTotal))
                    print('%30s%10.0f%10s%10.0f' % ("Because Total Payable:", total_ProgCharge, " < ", family_StandardTax))
                    print("(d) Recommend to Separated Tax in Progressive Rate")
                else:
                    print('%30s%10.0f%10s%10.0f' % ("Because Total Payable (Standard):", total_StadCharge, " > ", family_StandardTax))
                    print('%30s%10.0f%10s%10.0f' % ("Because Total Payable (Progressive):", total_ProgCharge, " < ", family_ProgChargeTotal))
                    print('%30s%10.0f%10s%10.0f' % ("Because Total Payable:", total_ProgCharge, " > ", family_StandardTax))
                    print("(d) Recommend to Jointed Tax in Standard Rate")
            else:
                if family_ProgChargeTotal < family_StandardTax:
                    print('%30s%10.0f%10s%10.0f' % ("Because Total Payable (Standard):", total_StadCharge, " > ", family_StandardTax))
                    print('%30s%10.0f%10s%10.0f' % ("Because Total Payable (Progressive):", family_ProgChargeTotal, " < ", total_ProgCharge))
                    print('%30s%10.0f%10s%10.0f' % ("Because Total Payable:", family_ProgChargeTotal, " < ", family_StandardTax))
                    print("(d) Recommend to Jointed Tax in Progressive Rate")
                else:
                    print('%30s%10.0f%10s%10.0f' % ("Because Total Payable (Standard):", total_StadCharge, " > ", family_StandardTax))
                    print('%30s%10.0f%10s%10.0f' % ("Because Total Payable (Progressive):", total_ProgCharge, " < ", family_ProgChargeTotal))
                    print('%30s%10.0f%10s%10.0f' % ("Because Total Payable:", total_ProgCharge, " > ", family_StandardTax))
                    print("(d) Recommend to Jointed Tax in Standard Rate")
        print("------------------------------------------------------")

def Calc_MPF(person_income):
    if person_income < 7100 * 12:
        person_MPF = 0
    elif person_income <= 30000 * 12:
        person_MPF = person_income * 0.05
    else:
        person_MPF = 1500 * 12

    return person_MPF


def person_Charge(person_income, person_allowance, person_MPF):
#    person_allowance = 132000
#    person_income = 300000


    person_Netincome = person_income - person_MPF
    person_StandardCharge = person_Netincome * 0.15
    person_ChargeIncome = person_Netincome - person_allowance
    if person_ChargeIncome <= 0 :
        person_ChargeIncome = 0
        person_Charge1st50K = 0
        person_Charge2nd50K = 0
        person_Charge3rd50K = 0
        person_Charge4th50K = 0
        person_ChargeRemain = 0
    else :

        person_RemainAfter1st50K = person_ChargeIncome - 50000
        if person_RemainAfter1st50K <= 0 :
            person_Charge1st50K = person_ChargeIncome * 0.02
            person_Charge2nd50K = 0
            person_Charge3rd50K = 0
            person_Charge4th50K = 0
            person_ChargeRemain = 0
        else :
            person_Charge1st50K = 50000 * 0.02

            person_RemainAfter2nd50K = person_RemainAfter1st50K - 50000
            if person_RemainAfter2nd50K <= 0 :
                person_Charge2nd50K = person_RemainAfter1st50K * 0.06
                person_Charge3rd50K = 0
                person_Charge4th50K = 0
                person_ChargeRemain = 0
            else :
                person_Charge2nd50K = 50000 * 0.06

                person_RemainAfter3rd50K = person_RemainAfter2nd50K - 50000
                if person_RemainAfter3rd50K <= 0:
                    person_Charge3rd50K = person_RemainAfter2nd50K * 0.10
                    person_Charge4th50K = 0
                    person_ChargeRemain = 0
                else:
                    person_Charge3rd50K = 50000 * 0.10

                    person_RemainAfter4th50K = person_RemainAfter3rd50K - 50000
                    if person_RemainAfter4th50K <= 0:
                        person_Charge4th50K = person_RemainAfter3rd50K * 0.14
                        person_ChargeRemain = 0
                    else:
                        person_Charge4th50K = 50000 * 0.14

                        person_ChargeRemain = person_RemainAfter4th50K * 0.17

    person_ChargeTotal = person_Charge1st50K + person_Charge2nd50K + person_Charge3rd50K + person_Charge4th50K + person_ChargeRemain

    return person_Netincome, person_ChargeIncome, person_Charge1st50K, person_Charge2nd50K, person_Charge3rd50K, person_Charge4th50K, person_ChargeRemain, person_StandardCharge, person_ChargeTotal





### Main Program ###
if __name__ == '__main__':
    Main()
    print('Finished')
