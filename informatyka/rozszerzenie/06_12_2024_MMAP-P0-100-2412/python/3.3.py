larger = 0
smaller = 0
equal = []


with open("liczby.txt", "r") as f:
    for line in f:
        number = int(line.strip())
        highest = int(''.join(sorted(line.strip(), reverse=True)))
        lowest = int(''.join(sorted(line.strip())))

        larger += (highest - lowest) > number
        smaller += (highest - lowest) < number
        equal.append(number) if (highest - lowest) == number else None

print(f"{smaller} smaller,\n {larger} larger,\n {len(equal)} equal: {equal}")
