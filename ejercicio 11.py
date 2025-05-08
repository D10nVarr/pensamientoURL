# #EJERCICIO 1
# from abc import ABC, abstractclassmethod

# class ExperimentoFisico (ABC):
#     def realizar_experimento(self):
#         pass

# class Caidalibre(ExperimentoFisico):
#     def __init__(self, altura, gravedad):
#         self.altura=altura
#         self.gravedad=gravedad
#     def tiempo_caida(self):
#         if self.altura <0:
#             raise ValueError("La altura debe ser un número positivo")
#         if self.gravedad==0:
#             raise ValueError("La gravedad no debe ser cero")
        
#         ca=((2 * self.altura) / self.gravedad)**(1/2)
#         return ca


# try: 
#     h=float(input("Ingrese la altura: "))
#     g=float(input("Ingrese el valor de la gravedad: "))

#     x=Caidalibre(h,g)

#     t=x.tiempo_caida()

#     print(round(t,2))

# except ValueError as e:
#     print(f"Error: {e}")



#EJERCICIO 2
import math

class OperacionCientifica():
    def __init__(self, dato, resultado=0):
        self.dato=dato 
        self.resultado=resultado
    def calcular(self):
        return f"De la operación {self.__class__.__name__} el resultado es de: {self.resultado}"

class RaizCuadrada(OperacionCientifica):
    def __init__(self, dato):
        super().__init__(dato)

    def raiz(self):
        try:
            if self.dato<0:
                raise ValueError("El número debe ser un positivo")
            self.resultado=(self.dato)**(1/2)
            return super().calcular()
        except ValueError as e:
            return f"Error en RaizCuadrada: {e}"

class Potencia(OperacionCientifica):
    def __init__(self, dato):
        super().__init__(dato)

    def potencia(self):
        exp=int(input("\nIngrese el valor del exponente: "))
        self.resultado=(self.dato)**(exp)
        return super().calcular()
    
class Logaritmo(OperacionCientifica):
    def __init__(self, dato):
        super().__init__(dato)

    def log(self):
        try:
            if self.dato<=0:
                raise ValueError("El número debe ser un positivo")
            self.resultado=math.log10(self.dato)
            return super().calcular()
        except ValueError as e:
            return f"Error en Logaritmo: {e}"

class Factorial(OperacionCientifica):
    def __init__(self, dato):
        super().__init__(dato)

    def fact(self):
        try:
            if self.dato<0 or not self.dato.is_integer():
                raise ValueError("El número debe ser un positivo y un entero")
            self.resultado=math.factorial(int(self.dato))
            return super().calcular()
        except ValueError as e:
            return f"Error en Factorial: {e}"

numero= float(input("Ingrese el número que desee calcular: "))

raiz= RaizCuadrada(numero)
potencia = Potencia(numero)
logaritmo= Logaritmo(numero)
factorial= Factorial(numero)

print(f"\n{raiz.raiz()}")
print(potencia.potencia())
print(f"\n{logaritmo.log()}")
print(f"\n{factorial.fact()}")
        










        