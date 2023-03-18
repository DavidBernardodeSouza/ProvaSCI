# Variaveis 

soma = 0
listaPar = []
listaImpar = []

for i in range (5):
    numero = int(input(f'Digite um numero na posição {i+1} '))
    soma += numero
    if numero %2==0:
        listaPar.append(numero)
    else:
        listaImpar.append(numero)
# impressão dos resultados
print('O resultado da média é ', soma/5)
print('Numeros pares ', listaPar,'Numeros impares ', listaImpar)