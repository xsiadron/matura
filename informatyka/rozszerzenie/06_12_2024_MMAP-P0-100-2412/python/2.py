def F(x, p):
    global l_wywolan
    l_wywolan += 1
    if x == 0:
        return 0
    else:
        c = x % p
        if c % 2 == 1:
            return F(x//p, p) + c
        else:
            return F(x//p, p) - c


# 2.1 ==========
# l_wywolan = 0
# wynik = F(125, 2)

# print(f"{wynik}, {l_wywolan}")
# ==========

# 2.2 ==========
# l_wywolan = 0

# x = 99
# p = 4
# while x > 0:
#     if F(x, p) == 0:
#         print(x)
#         break
#     x -= 1
# =========
