# Entrada
n = int(input("Columnas: "))
mon = []
mult = []
for i in range(n):
    mon += [int(input(f"Caja de monedas {i}: "))]
for i in range(n):
    mult += [int(input(f"Multiplicador {i}: "))]
# Resolucion
sortmon = [i for i in mon]
sortmon.sort()
sortmult = [i for i in mult]
sortmult.sort()
r = dict(zip(sortmon,sortmult))
rmult = []
for i in mon:
    rmult += [r[i]]
print(*rmult, sep= " ")