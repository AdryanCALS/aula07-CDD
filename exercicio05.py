notas = [""]*5
soma = 0
media = 0
for i in range(len(notas)):
    notas[i] = float(input("Digite a nota: "))

for j in range(len(notas)):
    soma += notas[j]

media = soma/len(notas)

print(f"A media da turma é: {media:.2f}")

acima_media = 0
for k in range(len(notas)):
    if notas[k] > media:
        acima_media +=1
print(f"O numero de alunos acima da media é {acima_media}")