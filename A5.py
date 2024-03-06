import math
a, b = map(int, input().split())
if(a == 0):
    if(b == 0):
        print("NWR")
    else:
        print("BR")
else:
    wynik = b/a
    '''
i = 10 kod by jan krasinski, pola brejt, wojciech gruntkowski i jeremi ogrodowczyk
'''
    wynik = wynik * -1
    print(f"{wynik:0.2f}")
