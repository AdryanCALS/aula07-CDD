usuarios = ["joao", "carlos", "mario", "maria", "josefa"]
senhas = [1234, 3432, 5432, 3333, 6666]
mensagem1 = "Usuario nao encontrado!! Digite outro nome!!"
login = input("Digite o nome de usuario!!")
for i in range(len(usuarios)):
    while login == usuarios[i]:
        mensagem1 = "Usuario encontrado!!"
        break
