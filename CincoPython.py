notas=[]
maiormedia = 0
menormedia = 10
alunoMaiorMedia=''
alunoMenorMedia=''

for i in range(3):
    aluno=(input('Digite o nome do aluno '))
    notas_aluno=[]
    for j in range(4):
        nota=(float(input(f'Digite a nota {j + 1} ')))
        notas_aluno.append(nota)
    notas.append((aluno,notas_aluno))

medias = []
for aluno in notas:
    nome = aluno[0]
    notas_aluno = aluno[1]
    media = sum(notas_aluno) / len(notas_aluno)
    if media > maiormedia:
        maiormedia=media
        alunoMaiorMedia = nome
    if media < menormedia:
        menormedia = media
        alunoMenorMedia = nome
    medias.append((nome, media))
    print("Aluno:", nome)
    print("Média:", media)

print(f'O aluno com a maior média foi {alunoMaiorMedia} com média {maiormedia}')
print(f'O aluno com a maior média foi {alunoMenorMedia} com média {menormedia}')