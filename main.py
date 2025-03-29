import numpy as np

n = 3
#array_np = np.array([[1,3,4,7],[2,1,3,4],[1,1,2,1]], dtype=np.float64)
array_np = np.array([[10, 5, -1, 1, 2], [2, 10, -2, -1, -26],
                     [-1, -2, 10, 2, 20], [1, 3, 2, 10, -25]],
                    dtype=np.float64)

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
