def get_num_of_dividers(n):
    dividers = set()
    divider = 2
    while divider * divider <= n:
        while n % divider == 0:
            dividers.add(divider)
            n //= divider
        divider += 1
    if n > 1:
        dividers.add(n)
    return len(dividers)


with open("liczby.txt", "r") as file:
    for line in file:
        if get_num_of_dividers(int(line)) >= 5:
            print(line.rstrip())
