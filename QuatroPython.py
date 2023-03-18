vetor = []  # cria uma lista vazia

for i in range(5):
    numero = int(input(f"Digite o número da posição {i+1}: "))
    vetor.append(numero)

print("O valor apresentado na posição três é:", vetor[2])