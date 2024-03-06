import sys

stawka = int(input())
dni = int(input())
wyplaty = []
minuty = []

for line in sys.stdin.readlines():
    h, m = line.split(":")
    wyplaty.append(int(h))
    minuty.append(int(m))
    '''
    i = 10 kod by wojtek gruntkowski
    '''
minuty = sum(minuty)
wyplata = sum(wyplaty) + minuty//60
minuty = minuty % 60

print(wyplata * stawka)
print(minuty) 
