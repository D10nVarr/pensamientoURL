num=int(input("Ingrese un numero entre 1 - 9: "))
resultado=""

    
if num>9:
    print("El número no es válido")
    
elif num<=0:
    print("El número no es válido")

elif num==9:
    resultado=(abs(num-10)*"I")+"X"
    print("El valor en números nomanos es:",resultado)

elif num>=6:
    resultado="V"+(num-5)*"I"
    print("El valor en números nomanos es:",resultado)
    
elif num==5:
    resultado="V"+(num-5)*"I"
    print("El valor en números nomanos es:",resultado)

elif num==4:
    resultado=(abs(num-5)*"I")+"V"
    print("El valor en números nomanos es:",resultado)

elif num<4:
    resultado=num*"I"
    print("El valor en números nomanos es:",resultado)
