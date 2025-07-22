# Liste non triée fournie
nombres = [23, 1, 56, 3, 78, 12, 5, 9]

# Tri à bulles simple
def tri_bulle(liste):
    n = len(liste)
    for i in range(n):
        for j in range(0, n - i - 1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j + 1] = liste[j + 1], liste[j]
    return liste

triée = tri_bulle(nombres)
print("Liste triée :", triée)
