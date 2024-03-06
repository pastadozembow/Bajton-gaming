liczby = list(map(int, input().split()))
k = 0
m = 0
x = len(liczby)
for i in range(x):
    if liczby[i] % 2 == 0:
        k += 1
    else:
        m += 1
'''
i = 10 kod by pola brejt
'''
print("Liczb parzystych jest:", k)
print("Liczb nieparzystych jest:", m)