def generuj_inicjaly(imie_nazwisko):
    slowa = imie_nazwisko.split()
    inicjaly = ""

    for slowo in slowa:
        if '-' in slowo:
            czesci = slowo.split('-')
            for czesc in czesci:
                if czesc[0].isupper():
                    inicjaly += czesc[0].upper()
        elif slowo[0].isupper():
            inicjaly += slowo[0].upper()

    return inicjaly
'''
i = 10 kod by pola brejt, jan krasinski, wojciech gruntkowski i jeremi ogrodowczyk
'''
n = int(input())

for _ in range(n):
    personalia = input()
    inicjaly = generuj_inicjaly(personalia)
    print(inicjaly)
