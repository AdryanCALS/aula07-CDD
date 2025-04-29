nomes = [""]*5
for i in range(5):
    nomes[i] = input(f"Digite o nome numero {i+1}: ")
for j in range(5):
    print(f"{nomes[j]}, {j}")