print ("Calculadora de desconto")

valor = float(input("Digite o valor da compra:"))

if valor > 100:
   desconto = (valor *0.9)
   print(desconto)

else:
   print("não tem desconto")
