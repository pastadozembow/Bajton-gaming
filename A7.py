import math
a, b, c = map(float, input().split())
'''
i = 10 kod by jan krasinski
'''
if(a + b > c):

    if(b + c > a):

        if(a + c > b):
            print("Tak")
        else:
            print("Nie")
    else:
        print("Nie")
else:
    print("Nie")