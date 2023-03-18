numeromaior= 0
for i in range(5):
    numero = int(input(f'Digite um numero na posição {i + 1}: '))
    if numero > numeromaior:
        numeromaior = numero
print('O maior numero é ', numeromaior)