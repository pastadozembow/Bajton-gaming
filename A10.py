i = 0
su = 0
sd = 0
n = int(input())
'''
i = 10 kod by jan krasinski, pola brejt, wojciech gruntkowski i jeremi ogrodowczyk
'''
for i in range(n):
    liczba = int(input())
    if(liczba < 0):
        su = su + liczba
    elif(liczba > 0):
        sd = sd + liczba
    else:
        break
print(su)
print(sd)
