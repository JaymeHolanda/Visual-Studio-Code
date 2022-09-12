altura = float(input("Digite sua altura em metros"))
peso = float(input("Digite seu peso em quiligramas")) 
imc = peso/(altura*altura)

if imc <= 18.5:
    print("Abaixo do peso normal")
    print("Procure um nutricionista, porque seu IMC atual é de",imc)
elif 18.5 < imc < 24.9:
    print("Peso Normal, Parabéns!")
elif 25.0 <= imc < 29.9: 
    print("Com o seu peso atual de",peso)
    print("Seu IMC foi",imc,"Procure um especialista")
    print("Excesso de Peso!")
elif 30.0 <= imc < 34.9:
    print("Com o seu peso atual de",peso)
    print("Seu IMC foi",imc,"Procure um especialista!")
    print("obesidade classe I")
elif 35.0 <= imc < 39.9: 
    print("Com o seu peso atual de",peso)
    print("De acordo com o seu IMC de",imc)
    print("Foi classificado como Obesidade Classe II")
else:
    print("Obesidade Classe III, procure um especialista!")
    print("seu IMC é de",imc) 

     


