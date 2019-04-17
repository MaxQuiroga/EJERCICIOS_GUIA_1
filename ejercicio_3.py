# MAXIMILIANO QUIROGA EJERCICIO 3

x = int(input("Ingrese el ángulo1: "))
y = int(input("Ingrese el ángulo2: "))
z= 180 - (x+y)

if x == 90 or y == 90 or z==90:
    print("El triangulo es rectángulo")
elif x < 90 and y < 90 and z < 90:
    print("El triangulo es acutángulo")
elif x > 90 or y > 90 or z > 90:
    print("El triangulo es obtusángulo")