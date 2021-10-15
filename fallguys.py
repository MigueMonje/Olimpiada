# Entrada
n = int(input("Numero de jugadores: "))
d = []
for i in range(n):
    d += [int(input(f"Jugador #{i+1}: "))]
# Descalificaciones
d2 = [
    x for x in d
    if (x % 3) != 0
    if (x % 2) == 0
]
# Salvados
if d2 == []:
    print(0)
else:
    print(d.index(max(d2))+1)