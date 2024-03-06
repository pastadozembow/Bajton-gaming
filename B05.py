text = input()
res = [int(i) for i in text.split() if i.isdigit()]
suma = 0
'''
i = 10 kod by pola brejt
'''
for o in range(len(res)):
  suma += res[o]
print(suma)