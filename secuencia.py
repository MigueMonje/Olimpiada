# Generador de secuencia
def gensec(f0,f1):
    def func(i):
        if i == 0:
            return f0
        elif i == 1:
            return f1
        else:
            return func(i-1) + func(i-2)
    return func
sec = gensec(int(input("F1: ")),int(input("F2: ")))
# Consultas
q = int(input("Q: "))
conj = True
for i in range(q):
    inp = int(input("F"))-1
    if sec(inp) % 2 == 0:
        print("par")
    else:
        print("impar")
        conj = False
if conj:
    print("conjetura")
else:
    print("contradiccion")
