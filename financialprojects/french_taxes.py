# EXERCICE CALCUL IMPOT FRANCAIS

from tabulate import tabulate as tb
def calcul_impot_2022(salaire,LMNP,parts,dons):

    #TRANCHES ET BAREME 2022
    tranche1 = 10777
    tranche2 = 27478
    tranche3 = 78570
    tranche4 = 168994
    taux_tranche1 = 0
    taux_tranche2 = 0.11
    taux_tranche3 = 0.30
    taux_tranche4 = 0.41
    taux_tranche5 = 0.45
    decote = 1378
    taux_decote = 0.4525

    #CALCUL DES IMPOTS BRUTS
    try:
        salaire_net = 0.9 * salaire
        LMNP_net = LMNP * 1.1
        revenus = LMNP_net + salaire_net
        quotient = revenus / parts
        if quotient < tranche1:
            impot_temp = taux_tranche1 * quotient
        elif tranche1 <= quotient < tranche2:
            impot_temp = taux_tranche1 * quotient + taux_tranche2 * (quotient-tranche1)
        elif tranche2 <= quotient < tranche3:
            impot_temp = taux_tranche1 * quotient + taux_tranche2 * (tranche2-tranche1) + taux_tranche3 * (tranche3-quotient)
        elif tranche3 <= quotient < tranche4:
            impot_temp = taux_tranche1 * quotient + taux_tranche2 * (tranche2-tranche1) + taux_tranche3 * (tranche3-tranche2) + taux_tranche4 * (tranche4-quotient)
        elif tranche4 <= quotient:
            impot_temp = taux_tranche1 * quotient + taux_tranche2 * (tranche2-tranche1) + taux_tranche3 * (tranche3-tranche2) + taux_tranche4 * (tranche4-tranche3) + taux_tranche5 * (quotient - tranche4)

        impot_int = impot_temp * parts
        impot_int = impot_int - max (0, decote - (impot_int * taux_decote))

        #CALCUL DES DEDUCTIONS
        tranche_don = 1000
        taux_tranche_don = 0.75

        if dons == 0:
            deduction = 0
        elif 0 < dons <= tranche_don:
            deduction = taux_tranche_don * dons
        elif tranche_don <= dons:
            deduction = taux_tranche_don * tranche_don + 0.66 * (dons-tranche_don)

        #CALCUL IMPOT FINAL
        impot_final = max(0,impot_int-deduction)
        table = [["Impot brut","Deduction","Impot Final"],[round(impot_int,2),round(deduction,2),round(impot_final,2)]]
        print("Voici le récap de vos impots 2022 : ")
        print(tb(table,headers="firstrow",tablefmt="simple"))

    except:
        print("One (or more) arguments is not a number. Please adjust !")

def calcul_impot_2023(salaire,LMNP,location,parts,dons):

    #TRANCHES ET BAREME 2022
    tranche1 = 11294
    tranche2 = 28797
    tranche3 = 82341
    tranche4 = 177106
    taux_tranche1 = 0
    taux_tranche2 = 0.11
    taux_tranche3 = 0.30
    taux_tranche4 = 0.41
    taux_tranche5 = 0.45
    decote = 1378
    taux_decote = 0.4525

    #CALCUL DES IMPOTS BRUTS
    try:
        salaire_net = 0.9 * salaire
        LMNP_net = LMNP * 1.1
        location_net = location * 0.5
        revenus = LMNP_net + salaire_net + location_net
        quotient = revenus / parts
        if quotient < tranche1:
            impot_temp = taux_tranche1 * quotient
        elif tranche1 <= quotient < tranche2:
            impot_temp = taux_tranche1 * quotient + taux_tranche2 * (quotient-tranche1)
        elif tranche2 <= quotient < tranche3:
            impot_temp = taux_tranche1 * quotient + taux_tranche2 * (tranche2-tranche1) + taux_tranche3 * (tranche3-quotient)
        elif tranche3 <= quotient < tranche4:
            impot_temp = taux_tranche1 * quotient + taux_tranche2 * (tranche2-tranche1) + taux_tranche3 * (tranche3-tranche2) + taux_tranche4 * (tranche4-quotient)
        elif tranche4 <= quotient:
            impot_temp = taux_tranche1 * quotient + taux_tranche2 * (tranche2-tranche1) + taux_tranche3 * (tranche3-tranche2) + taux_tranche4 * (tranche4-tranche3) + taux_tranche5 * (quotient - tranche4)

        impot_int = impot_temp * parts
        impot_int = impot_int - max (0, decote - (impot_int * taux_decote))

        #CALCUL DES DEDUCTIONS
        tranche_don = 1000
        taux_tranche_don = 0.75

        if dons == 0:
            deduction = 0
        elif 0 < dons <= tranche_don:
            deduction = taux_tranche_don * dons
        elif tranche_don <= dons:
            deduction = taux_tranche_don * tranche_don + 0.66 * (dons-tranche_don)

        #CALCUL IMPOT FINAL
        impot_final = max(0,impot_int-deduction)
        table = [["Impot brut","Deduction","Impot Final"],[round(impot_int,2),round(deduction,2),round(impot_final,2)]]
        print("Voici le récap de vos impots 2023 : ")
        print(tb(table,headers="firstrow",tablefmt="simple"))

    except:
        print("One (or more) arguments is not a number. Please adjust !")

calcul_impot_2022(40955,2893,2,3908)
print("******************************************************************")
calcul_impot_2023(42108,2893,6857,2,3251)

