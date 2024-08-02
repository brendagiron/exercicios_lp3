from imc import classificacaodoimc,calculoimc,pesoideal,diferencapeso

def main():
    peso = float(input("Qual o seu peso(kg)?"))
    altura = float(input("Qual a sua altura(metros)?"))
    
    imc = calculoimc(peso, altura)
    classificacao = classificacaodoimc(imc)
    diferenca = diferencapeso(peso, altura)
    ideal = pesoideal(peso,altura)
    
    print("Seu IMC: {:.2f}".format(imc))
    print("Sua classificação: {}".format(classificacao))
    
    if imc > 24.9:
       print("Você está precisando perder {:.2f}kg para chegar ao peso ideal de {:.2f}kg".format(diferenca,ideal))
    elif imc < 18.5:
       print("Você está precisando ganhar {:.2f}kg para chegar ao peso ideal de {:.2f}kg".format(diferenca,ideal))
    else:
        print("Você está com o peso ideal")  
        
        
if __name__ == "__main__":
    main()