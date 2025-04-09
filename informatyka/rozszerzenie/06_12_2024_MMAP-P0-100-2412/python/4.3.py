import itertools


def zwroc_max_szerokosc(plik, liczba_kombinacji):
    with open(plik, "r") as file:
        lines = file.readlines()

    prostokaty = [tuple(map(int, line.strip().split())) for line in lines]

    max_szerokosc = 0

    prostokaty.sort(key=lambda x: x[0])
    for wysokosc, szerokosci in itertools.groupby(prostokaty, lambda x: x[0]):
        grupa_list = list(szerokosci)
        if len(grupa_list) < liczba_kombinacji:
            continue

        szerokosci_sorted = sorted(
            [szerokosc for _, szerokosc in grupa_list], reverse=True)

        suma_szerokosci = sum(szerokosci_sorted[:liczba_kombinacji])

        max_szerokosc = max(max_szerokosc, suma_szerokosci)

    return max_szerokosc


dwa = zwroc_max_szerokosc("prostokaty.txt", 2)
print(dwa)
trzy = zwroc_max_szerokosc("prostokaty.txt", 3)
print(trzy)
piec = zwroc_max_szerokosc("prostokaty.txt", 5)
print(piec)
