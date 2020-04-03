def ters(x):
    return x[::-1]

x = input("ters cevirelim: ")
y = ters(x)
if x == y:
    print("this is a palindrome")
else:
    print("bu normal cümle")

lista = x.split(" ")
print(lista)
wordindici= int(input("kaçıncı kelime? "))
indnum = wordindici-1
if wordindici > len(lista):
    print("you have to write not more than " + str(len(lista)))
else:
    print(str(wordindici) + ". kelime" + lista[indnum]