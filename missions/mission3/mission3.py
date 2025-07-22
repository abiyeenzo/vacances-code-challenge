def celsius_vers_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def main():
    try:
        celsius = float(input("Entrez la température en degrés Celsius : "))
        fahrenheit = celsius_vers_fahrenheit(celsius)
        print(f"{celsius}°C correspond à {fahrenheit:.2f}°F.")
    except ValueError:
        print("Erreur : veuillez entrer un nombre valide.")

if __name__ == "__main__":
    main()
