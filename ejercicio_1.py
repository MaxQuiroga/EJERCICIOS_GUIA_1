# MAXIMILIANO QUIROGA:    
#       EJERCICIO 1

def rut():
    COD = [2,3,4,5,6,7,2,3,4,5,6,7]
    R = input("Ingrese RUT sin verificador: ")
    R = R[::-1]
    c = 0
    d = 0
    dv = 12
    suma = 0
    
    while c < len(R):
        d = int(R[c])*int(COD[c])
        suma = suma + d
        c = c + 1
    print (suma)
    v = 11 - (suma % 11)
    
    if 0 < v < 10:
        dv = v
    elif v == 11:
        dv = 0
    elif v == 10:
        str(dv)
        dv = "K"
        
    print ("El digito verificador es: ", dv)
    
rut()