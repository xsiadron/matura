largest_field = 0
lowest_field = 99999999999999

with open("prostokaty.txt", "r") as f:
    for line in f:
        numbers = line.strip().split(" ")
        s, h = list(map(int, numbers))
        field = s * h

        if field > largest_field:
            largest_field = field

        if field < lowest_field:
            lowest_field = field

print(f"Najmniejsze pole: {lowest_field}")
print(f"Największe pole: {lowest_field}")
