from fractions import Fraction

#pi=3.14
#r=int(input("dammi il raggio del cerchio: "))
#A=pi*r**2
#print("L'area è ", A)

#a=int(input("n1: "))
#b=int(input("n2: "))
#a,b=b,a
#print(f"{a} , {b}")

#C=int(input("temperatura: "))
#F=(C*9/5)+32
#print(F)

# pi=3.14
# raggio=3
# A=pi*raggio**2
# Circonferenza=2*raggio*pi
# print(f"L'area è {A}, la circonferenza è {Circonferenza}")

# altezza=3
# base=2
# A=base*altezza/2
# print(f"L'area è {A}")

# numero=0.5
# numero_intero=int(numero)
# numero_fratto=(Fraction(numero))
# print(numero_intero)
# print(numero_fratto)

# prezzo_originale=50
# prezzo_scontato=prezzo_originale-(prezzo_originale*20/100)
# print(prezzo_scontato)

"""
def controlli():
    while True:
        try:
            prezzo_originale=int(input("dammi un prezo: "))
            # lunghezza=0
            # num=prezzo_originale
            # while num>1:
            #     num=num/10
            #     lunghezza+=1
            if prezzo_originale >= 4:
                print("numero troppo lungo")
            else:
                prezzo_scontato=prezzo_originale-(prezzo_originale*20/100)
                print(prezzo_scontato)
                break
        except ValueError:
            print("devi darmi un numero")
controlli()
"""
"""
def palindrome(frase):
    #if (frase).is_integer:
        #print("voglio una frase")
    #else:
        lista=list(frase)
        print(frase)
        #frase_girata=" ".join(frase.split().reverse())
        print(f"quando viene girata è '{frase_girata}'")
        z=0
        t=lista.count(" ")
        while t>z:
            lista.remove(" ")
            z+=1
        print(lista)
        if lista==lista[::-1]:
            print(" questa frase è palindrome")
        else:
            print(" questa frase non è palindrome")
palindrome("aceto nell enoteca")
"""


def frase(testo):
    frase1 = list(testo)  # Converti la stringa in una lista di caratteri
    frase1.reverse()      # Inverti la lista di caratteri
    frase1 = "".join(frase1)  # Unisci i caratteri invertiti in una stringa
    print(frase1)

frase("aceto nell enoteca")

def fibonacci():
    while True:
        try:
            n=int(input("dammi un valore: "))
            lista=[0,1]
            a=0
            b=1
            while n>len(lista):
                c=a+b
                a=b
                b=c
                lista.append(c)
            print(lista)
            print(len(lista))
            break
        except ValueError:
            print("voglio un intero")
fibonacci()














