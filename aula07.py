import random
nomes = [""]*5
for i in range(5):
    nomes[i] = input(f"Digite o nome numero {i+1}: ")
p1 = random.randint(0,4)
p2 = random.randint(0,4)
if p2 == p1:
    p2 = p1+1
print(f"OBA!! {nomes[p1]} gosta de {nomes[p2]}!!!")