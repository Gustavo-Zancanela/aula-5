real = float(input('Digite um valor: '))
dolar = real * 5.46
euro = real * 6.05
print(dolar, "dolares", euro, "euros", real, "reais")

distancia = input("Digite qual distância será convertida, em milhas ou km: ")
if (distancia == "km"):
    km = float(input("Digite um valor: "))
    print(km*0, 621371, "km")

elif (distancia == "milhas"):
    milhas = float(input("Digite um valor: "))
    print(milhas*1.60934, "milhas")
