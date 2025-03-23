def J(n):
    position = 0
    while n > 0:
        position += 1
        if n % 2:
            print(position)
        n //= 2


J(42)
