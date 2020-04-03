kenaruzunluğu = int(input("bir kenarda kaç yıldız var?= "))

for i in range(1, kenaruzunluğu+1):
    for j in range(1, kenaruzunluğu+1):
        print("*", end='')
    print()

#  Print * Rectangle

for i in range(1, kenaruzunluğu+1):
    for j in range(1, kenaruzunluğu+1):
        if (i == 1 or i == kenaruzunluğu):
            print("*",
                  end='')
        else:
            if (j == 1 or j == kenaruzunluğu):
                print("*", end='')
            else:
                print(" ", end='')
    print()
