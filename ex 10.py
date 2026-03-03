print(" Classificação de IMC")

peso = float(input("Digite o seu peso em kg:"))
altura = float(input("Digite a sua altura em metros:"))

imc = peso/(altura * altura)
if imc < 18.5 :
    print("Abaixo do peso")

elif 18.5 <= imc < 24.9:
    print("Peso normal")

elif 25 <= imc < 29.9:
    print("Sobrepeso")

else :
    print("Obesidade")