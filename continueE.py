#construct a multiplication table that contains only the odd numbers

for i in range (1, 10):
    for j in range (1,10):
        if i %2 == 0:
            continue
        if j %2 == 0:
            continue
        else:
            print(str(i), "*", str (j), "=", +i*j)
