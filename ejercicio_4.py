# MAXIMILIANO QUIROGA EJERCICIO 4

NOMBRE = input("ingrese el nombre del clavadista: ")
D = float(input("igrese la dificultad del clavado: "))
JUECES=7
x=0
i=0
I=0
puntajes=[]
for i in range(0,JUECES) :
    x=float(input("ingrese puntaje del juez: "))
    x=x+I
    puntajes.append(x)
    if I==0:
        I=1/2
puntajes.sort()

puntajes.pop(-1)

puntajes.pop(0)

R = (puntajes[0]+puntajes[1]+puntajes[2]+puntajes[3]+puntajes[4])*(3/5)
R = R*D
print("el puntaje del clavadista es: ",r)