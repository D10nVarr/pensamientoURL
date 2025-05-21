Gen0= [
 [0,0,0,0,0,0,0,1,1,0],
 [0,1,1,0,0,0,0,0,0,0],
 [0,1,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,0,0],
 [0,0,0,0,0,1,1,0,0,0],
 [0,0,0,0,0,1,1,0,0,0],
 [0,0,1,1,0,0,0,0,0,0],
 [0,0,1,1,0,0,0,0,0,0],
 [0,0,0,0,0,0,0,0,1,0],
]

def contar_vecinos(Gen0, fila, columna):
    vecinos=0
    if columna > 0:
        vecinos += Gen0[fila][columna-1]
    if columna< len(Gen0[0])-1:
        vecinos += Gen0[fila][columna+1]
    return vecinos

def new_gen(Gen0):
    filas =len(Gen0)
    columnas= len(Gen0[0])
    new=[]

    for fila in range(filas):
        new_fila =[]
        for columna in range(columnas):
            vecinos = contar_vecinos(Gen0, fila, columna)
            celula= Gen0[fila][columna]

            if celula==1:
                if vecinos ==1 or vecinos==2:
                    new_fila.append(1)
                else:
                    new_fila.append(0)
            else:
                if vecinos ==1:
                    new_fila.append(1)
                else:
                    new_fila.append(0)
        new.append(new_fila)
    return new

print("Generación 0:")
for i in Gen0:
    print(i)

Gen1= new_gen(Gen0)
print("\nGeneración 1:")
for i in Gen1:
    print(i)

Gen2= new_gen(Gen1)
print("\nGeneración 2:")
for i in Gen1:
    print(i)

