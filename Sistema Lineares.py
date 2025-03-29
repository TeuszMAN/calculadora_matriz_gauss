import numpy as np

n =  int(input("Digite o tamanho da matriz: "))
print("-")


matriz = []

for j in range(n):
    linha = []
    for i in range(n):
        coeficiente = float(input(f"Digite o coeficiente do termo A[{j}][{i}]: "))
        linha.append(coeficiente)

    termo_independente = float(input(f"Digite o termo independente (soma dos termos) A[{j}][{n}]: "))
    linha.append(termo_independente)

    matriz.append(linha)


cabecario = []

array_np = np.array(matriz)

for i in range(n):
    cabecario.append("x" + str(i+1))
cabecario.append("ind")

print("\n matriz inserida: ")
print(" | ".join(v.ljust(6) for v in cabecario))
for linha in matriz:
    print (" | ".join(f"{v:.2f}".ljust(6) for v in linha))


for i in range(array_np.shape[0] - 1):
  for j in range(i + 1, array_np.shape[0]):
    fator = array_np[j, i] / array_np[i, i]
    array_np[j] = array_np[j] - fator * array_np[i]
    print(array_np)
    print("-")


def escalar(array_np):
  n = array_np.shape[0]
  valores = np.zeros(n)

  for i in range(n - 1, -1, -1):
    valores[i] = array_np[i, -1]

    for j in range(i + 1, n):
      valores[i] -= array_np[i, j] * valores[j]

    valores[i] /= array_np[i, i]
  return valores


solucao = escalar(array_np)
print("resposta para valores: ")
for i in range(solucao.size):
  print("x", i + 1, " :", solucao[i])

