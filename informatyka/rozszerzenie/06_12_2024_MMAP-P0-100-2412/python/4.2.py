strings = []
i = 0
strings.append(0)

with open("prostokaty_przyklad.txt", "r") as f:
    lines = f.readlines()

    for prev_line, current_line in zip(lines, lines[1:]):
        prev_line = prev_line.strip().split(" ")
        current_line = current_line.strip().split(" ")
        s1, h1 = list(map(int, prev_line))
        s2, h2 = list(map(int, current_line))

        if s1 >= s2 and h1 >= h2:
            # strings[i] += 1
            print(f"{s2} {h2}")
        else:
            # strings.append(0)
            print(f"{s2} {h2} s")
            i += 1

print(strings)
print(i)
# prev_line =
#     s, h = list(map(int, numbers))
#     field = s * h

#     if s <= s2 & h <= h2
