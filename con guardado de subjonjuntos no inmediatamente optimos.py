L = [[4,5],[1],[1,3,5],[2,4,5],[1,2],[3],[1,6,5]]
L.sort(key=lambda x:len(x), reverse=True)
L = [[1, 3, 5], [1, 6, 5], [2, 4, 5], [4, 5], [1, 2], [1], [3]]
print(L)
S = [1,2,3,4,5,6]
M = []
T = L[0]
nT = list(set(S)-set(T))
i = 1
contador = 1
while (len(T)<len(S)) & (i < (len(L)- 1)):
  if len(list(set(L[i]) & set(nT))) < len(list(set(L[i+1]) & set(nT))):
    M.append(L[i]) # me salto Li, pero lo guardo
    i = i + 1
  T = list(set(T) | set(L[i]))
  nT = list(set(S)-set(T))
  i = i + 1
  contador = contador + 1
if (len(T)<len(S)):
  for X in M:
    if len(list(set(nT)&set(X))) > 0:
      T = list(set(T) | set(X))
      nT = list(set(S)-set(T))
      contador = contador + 1
      print("hola")
  if len(T)==len(S):
    print("se ha encontrado una solucion con {} subconjuntos para este problema".format(contador))
  else:
    print("problema sin solucion")
else:
	print("se ha encontrado una solucion con {} subconjuntos para este problema".format(contador))