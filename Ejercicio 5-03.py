#1 ejercicio:

# entrada="Python es un lenguaje poderoso"

# nuevo=entrada.split()
# cantidad=len(nuevo)

# print("Primera palabra: ",nuevo[0])
# print("Primera palabra: ",nuevo[cantidad-1])

#2 ejercicio:

# entrada="Hola      mundo      en Python"

# nuevo=entrada.split()
# sin= " ".join(nuevo)

# print(sin)

#3 ejercicio:

# entrada="usuario@gmail.com"

# nuevo=entrada.split("@")

# print(nuevo[1])

#4 ejercicio

#entrada="documento.pdf"

#a=entrada.endswith(".pdf")

#print(a)

#5
# entrada="Me gusta Python"

# palabra=entrada.split()

# nuevo=palabra[::-1]

# a=" ".join(nuevo)

# print(a)

#6
entrada=input("Ingrase los que desea: ",)

poema1="Podrá nublarse el sol eternamente; Podrá secarse en un instante el mar; Podrá romperse el eje de la tierra Como un débil cristal."
canto1="Eres como la noche, callada y constelada. Tu silencio es de estrella, tan lejano y sencillo. Me gustas cuando callas porque estás como ausente. Distante y dolorosa como si hubieras muerto."

if entrada in poema1:
    print("El poema relacionado es:", poema1)
    
elif entrada in canto1:
   print("El canto relacionado es:", canto1)
