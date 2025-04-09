prostokaty = []
i = 0
prostokaty.append(0)

with open("prostokaty.txt", "r") as f:
    lines = f.readlines()

    najdluzszy_ciag = []
    aktualny_ciag = []

    for i in range(len(lines)):
        wysokosc, szerokosc = map(int, lines[i].strip().split())

        if not aktualny_ciag or (aktualny_ciag[-1][0] >= wysokosc and aktualny_ciag[-1][1] >= szerokosc):
            aktualny_ciag.append((wysokosc, szerokosc))
        else:
            if len(aktualny_ciag) > len(najdluzszy_ciag):
                najdluzszy_ciag = aktualny_ciag[:]
            aktualny_ciag = [(wysokosc, szerokosc)]

    if len(aktualny_ciag) > len(najdluzszy_ciag):
        najdluzszy_ciag = aktualny_ciag[:]

print(len(najdluzszy_ciag), najdluzszy_ciag[-1][0], najdluzszy_ciag[-1][1])
