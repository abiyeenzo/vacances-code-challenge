import string

texte = """
Bonjour! Ceci est un texte d'exemple. Ce texte contient des mots, des répétitions,
et de la ponctuation. Comptez les mots uniques dans ce texte, s'il vous plaît.
"""

def compter_mots_uniques(texte):
    # Nettoyer la ponctuation
    texte_nettoye = texte.lower()
    for ponct in string.punctuation:
        texte_nettoye = texte_nettoye.replace(ponct, "")
    mots = texte_nettoye.split()
    
    total_mots = len(mots)
    mots_uniques = set(mots)
    return total_mots, mots_uniques

def main():
    total, uniques = compter_mots_uniques(texte)
    print(f"Nombre total de mots : {total}")
    print(f"Nombre de mots uniques : {len(uniques)}")
    print("Mots uniques triés :")
    for mot in sorted(uniques):
        print(mot)

if __name__ == "__main__":
    main()
