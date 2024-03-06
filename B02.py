def trojkat(a:int, b:int, c:int)->bool:
	return (a + b > c) and (a + c > b) and (b + c > a)

dane = input().split()
a, b, c = int(dane[0]), int(dane[1]), int(dane[2])
if trojkat(a,b,c):
    print('TAK')
else:
    print('NIE')