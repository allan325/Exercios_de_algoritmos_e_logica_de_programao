print("Contador de números pares")

numero = int(input("Digite um numero:"))

while  numero > 0  :
    if numero %2 !=0 :

        print (numero)
        numero -=1
        print("Número par")
    else:
     print(numero)
     numero -=2
     print("Número par")
