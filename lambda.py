f = lambda n, m: n + m
print(f(5, 6))

a = lambda x: 'yes' if x % 2 == 0 else 'no'
print(a(9))

# create a list that contains only the filtered even members of another list

lst = []
n = int(input("kaç sayı girecen= "))
for i in range (0, n):
    lst.append(int(input("lütfeninci sayıyı giriniz= ")))

result = list(filter(lambda k: k % 2 == 0, lst))
print(result)
