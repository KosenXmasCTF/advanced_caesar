flag = "xm4s{caesarnoyomikatagawakarann}"
alpha = 'abcdefghijklmnopqrstuvwxyz'

d = 0

for c in flag:
    if c in alpha:
        index = alpha.find(c)
        print(alpha[(index + d) % len(alpha)], end="")
        d += 1
    else:
        print(c, end="")



