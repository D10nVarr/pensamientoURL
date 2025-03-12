#consumo=int(input("Ingrese el número de metros cúbicos: "))

#if consumo<15:
   # print("La tarifa es de Q.5 por m³, sutatifa total es de: ", (5*consumo))
    
#elif consumo<30 or consumo>15:
    #personas=int(input("Ingrese el número de habitantes: "))
   
   # if personas>3:
       # print("La tarifa es de Q.4 por m³, sutatifa total es de: ", (4*consumo))
   # elif personas==3:
       # print("La tarifa es de Q.4.5 por m³, sutatifa total es de: ", (4.5*consumo))
   # else: 
    #    print("La tarifa es de Q.5 por m³, sutatifa total es de: ", (5*consumo))
        
#elif consumo>30:
    #personas=int(input("Ingrese el número de habitantes: "))
    
   # if personas>5:
     #   print("La tarifa es de Q.3.5 por m³, sutatifa total es de: ", (3.5*consumo))
   # elif personas%2==0:
      #  print("La tarifa es de Q.4 por m³, sutatifa total es de: ", (4*consumo))
   # else: 
      #  print("La tarifa es de Q.4.2 por m³, sutatifa total es de: ", (4.2*consumo))
      
año=int(input("Ingrese el año del vehículo: "))
placa=input("Ingrese el número de placa: ")

lunes="02468"
viernes="13579"

cantidad=len(placa)

antiguedad=2025-año

if año>=2001:
    if cantidad>1 and ((placa[-1]) in lunes):
        print("No circula los lunes")
    elif cantidad>1 and ((placa[-1]) in viernes):
        print("No circula los viernes")
        
else:
    print("la restricción no aplica")
    
if antiguedad>25:
    print("ATENCIÓN, el vehículo necesita mantenimiento")