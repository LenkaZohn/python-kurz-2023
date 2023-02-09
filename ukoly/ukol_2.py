sklad = {
    "1N4148": 250,
    "BAV21": 54,
    "KC147": 147,
    "2N7002": 97,
    "BC547C": 10
}

Kod_soucastky = input("Zadej kód součástky:")
Mnozstvi_soucastky = int(input("Zadej množství součástky."))

if Kod_soucastky not in sklad:
    print(f"Součástka {Kod_soucastky} není skladem.")
else:
    if sklad[Kod_soucastky] < Mnozstvi_soucastky:
        print(f"Součástky {Kod_soucastky} lze prodat pouze omezené množství {sklad[Kod_soucastky]}.")
        sklad.pop(Kod_soucastky)
    else:
        print(f"Poptávku lze uspokojit v plné výši.")
        sklad[Kod_soucastky] -= Mnozstvi_soucastky