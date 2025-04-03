##EJERCICIO 1
# n=int(input("Tamaño array: "))
# m=int(input("multiplos: "))

# salida=[] #vector vacio, el tamaño no es fijo y su tipo de dato no es fijo

# for i in range(1,n+1):
#     salida.append(i*m)
# print(salida)

# #EJERCICIO 2
# arr=int(input("Ingrese el tamaño de los 2 vectores: "))

# nombres=[]
# long=[]

# while arr>0:
#     nom=str(input("Ingrese los nombres: "))
#     nombres.append(nom)
#     long.append(len(nom))
#     arr-=1
# print("")
# print(nombres)
# print(long)

#ESCENARIO 1
n=int(input("Ingrese el numero de clientes: "))

print("Evalue la atención recibida en la siguiente escala")

print("5. Excelente")
print("4. Muy Buena")
print("3. Buena")
print("2. Regular")
print("1. Mala")

cliente=[]
atencion=[]

excelente=0
muy=0
buena=0
regular=0
malo=0


for i in range(1,n+1):
    opcion=int(input(f"ingrese la evaluación del 1 al 5 del cliente {i}: "))

    if 1 <= opcion <=5:
        cliente.append(i)
        atencion.append(opcion)

        if opcion==5:
            excelente+=1
        if opcion==4:
            muy+=1
        if opcion==3:
            buena+=1
        if opcion==2:
            regular+=1
        if opcion==1:
            malo+=1
    else:
        print("Opción no válida")

print("Cliente  ",cliente)
print("Atención ",atencion)
print("")

print("a) Excelente:", excelente)
print("   Muy Buena:", muy)
print("   Buena:", buena)
print("   regular:", regular)
print("   Mala:", malo)

maximo=max(excelente,muy,buena,regular,malo)

if maximo==excelente:
    print("b) Más frecuente: 5" )
elif maximo==muy:
    print("b) Más frecuente: 4" )
elif maximo==buena:
    print("b) Más frecuente: 3" )
elif maximo==regular:
    print("b) Más frecuente: 2" )
elif maximo==malo:
    print("b) Más frecuente: 1" )

promedio=(5*excelente+4*muy+3*buena+2*regular+1*malo)/n

print("c) Promedio: ",promedio )

debajo_promedio = malo + regular + buena 
if promedio > 3:
    debajo_promedio = malo + regular  

porcentaje_debajo = (debajo_promedio / n) * 100

print("d) Porcentaje menor al primedio: ", porcentaje_debajo)

# Cliente   [1, 2, 3, 4, 5]
# Atención  [1, 3, 3, 5, 4]

