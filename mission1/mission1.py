# Calcul simple de la somme des nombres pairs entre 1 et 100

total = 0
for i in range(1, 101):
    if i % 2 == 0:
        total += i

print("Somme des nombres pairs de 1 à 100 :", total)
