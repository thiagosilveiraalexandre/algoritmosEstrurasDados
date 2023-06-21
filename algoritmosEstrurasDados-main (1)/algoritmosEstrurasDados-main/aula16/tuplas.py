carros = ("Uno", "Doblo","Toro","Hilux")
print(sorted(carros))
print(carros)

jogadores = ("Ronaldinho","Neymar","Messi","Di maria")

print(jogadores)
print(jogadores[1])
print(jogadores[1:3])
print(jogadores[1:])
print(jogadores[0:3])
print(jogadores[3:-3])

def calcular(x,y):
    return x+y,x-y,x*y,x/y 

resultado = calcular(10,5)
print(resultado)
print("Multiplicação: ", resultado[2])
a,b,c,d = calcular( 9, 3)
print("Soma: ", a)
print("Subtração: ", b)
print("Multiplicação: ", c)
print("Divisão: ", d)