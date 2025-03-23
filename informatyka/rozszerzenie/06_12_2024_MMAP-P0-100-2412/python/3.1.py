import math

valid_numbers = []
with open("liczby.txt", "r") as file:
    for line in file:
        square_root = math.sqrt(int(line))

        number = str(square_root).split(".")

        if (int(number[1]) == 0):
            valid_numbers.append(int(line))
print(
    f"Liczba numerów to: {len(valid_numbers)} a te numery to: {valid_numbers}")
