A = [5,6,7,8,9]
M = [""]*5
Multiplicador = int(input("Digite o numero que vai multiplicar o array: "))
for i in range(len(M)):
    M[i] = A[i]* Multiplicador
print(A)
print(Multiplicador)
print(M)