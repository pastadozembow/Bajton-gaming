import math
a, d = map(float, input().split())
ds = d*d
ad = a*a
b = ds - ad
b = math.sqrt(b)
pole = a*b
'''
i = 10 kod by jan krasinski, pola brejt, wojciech gruntkowski i jeremi ogrodowczyk
'''
obwod = a + b
obwod = 2*obwod
print(f"{pole:0.2f}")
print(f"{obwod:0.2f}")
