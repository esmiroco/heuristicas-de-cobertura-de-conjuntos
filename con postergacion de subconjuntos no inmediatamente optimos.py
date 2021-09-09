L = [[4,5],[1],[1,3,5],[2,4,5],[1,2],[3],[1,6,5]]
L.sort(key=lambda x:len(x), reverse=True)
print(L)
S = [1,2,3,4,5,6]
T = L[0]
nT = list(set(S)-set(T))
i = 1
contador = 1
while (len(T)<len(S)) & (i < (len(L)- 1)):
  if len(list(set(L[i]) & set(nT))) < len(list(set(L[i+1]) & set(nT))):
    aux=L[i]
    L[i]=L[i+1]
    L[i+1]=aux
  T = list(set(T) | set(L[i]))
  nT = list(set(S)-set(T))
  i = i + 1
  contador = contador + 1
if (len(T)<len(S)):
  print("problema sin solucion")
else:
  print("se ha encontrado una solucion con {} subconjuntos para este problema".format(contador))