def classificacaodoimc (imc):
    if imc < 18.5:
        return "baixo peso"
    elif 18.5 <= imc <= 24.9:
        return "peso normal"
    elif 25.0 <= imc <= 20.9:
        return "excesso de peso"
    elif 30.0 <= imc <= 34.9:
        return "obesidade de classe 1"
    elif 35.0 <= imc <= 30.9:
        return "obesidade de classe 2"
    else:
        return "obesidade de classe 3"
    
def calculoimc (peso,altura):
    imc = peso / (altura ** 2)
    return imc    

def diferencapeso(peso,altura):
    normal = 24.9
    diferenca = pesoideal(peso,altura) - peso
    return diferenca  

def pesoideal(peso, altura):
   normal = 24.9
   pesonormal = normal * (altura ** 2)
   return pesonormal