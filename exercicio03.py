nomes = ["joao", "carlos", "maria", "luiza", "isabel"]
perg = input("digite o nome da pessoa: ")
msg = "n esta na lista"
for i in range(len(nomes)):
    if nomes[i] == perg:
        msg = f"Oba, o nome: {perg}, esta na posição {i} da lista!"
        break
print(msg)