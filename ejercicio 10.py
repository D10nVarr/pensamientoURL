# #EJERCICIO 1
# class Animal:
#     def __init__(self, nombre, edad, peso):
#         self.nombre=nombre
#         self.edad=edad
#         self.peso=peso

#     def calcular_dosis(self):
#         if self.peso>10:
#             i=self.peso*0.7
#         elif self.peso > 5:
#             i=self.peso*0.5
#         elif self.peso > 0:
#             i=self.peso*0.25
#         else:
#             print("Peso inválido")
#             return
#         return i

#     def datos_basicos(self):
#         return f"Nombre del {self.__class__.__name__}: {self.nombre}, Edad: {self.edad} años, Peso: {self.peso} kg"
    
#     def ficha_medica(self):
#         return f"{self.datos_basicos()}\nDosis recomendada: {self.calcular_dosis()} mg"


# class Perro(Animal):
#     def __init__(self, nombre, edad, peso, raza):
#         super().__init__(nombre, edad, peso)
#         self.raza=raza

#     def dosis(self):
#         self.calcular_dosis()


# class Gato(Animal):
#     def __init__(self, nombre, edad, peso, tamaño):
#         super().__init__(nombre, edad, peso)
#         self.tamaño=tamaño

#     def dosis(self):
#         self.calcular_dosis()


# class Ave(Animal):
#     def __init__(self, nombre, edad, peso, plumaje):
#         super().__init__(nombre, edad, peso)
#         self.plumaje=plumaje

#     def dosis(self):
#         self.calcular_dosis()


# class Reptil(Animal):
#     def __init__(self, nombre, edad, peso, habitad):
#         super().__init__(nombre, edad, peso)
#         self.habitad=habitad

#     def dosis(self):
#         self.calcular_dosis()


# perroA=Perro("Juan", 5, 15, "Golden")
# print(perroA.ficha_medica())
# print()
# gatoA=Gato("Mostaza", 6, 5, "grande")
# print(gatoA.ficha_medica())
# print()
# aveA=Ave("Jack", 2, 0.5, "azul")
# print(aveA.ficha_medica())
# print()
# reptilA=Reptil("Rango", 3, 1, "húmedo")
# print(reptilA.ficha_medica())




#EJERCICIO 2
class Persona:
    def __init__(self, nombre, edad, dni):
        self.nombre=nombre
        self.edad=edad
        self.dni=dni

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"


class Estudiante(Persona):
    def __init__(self, nombre, edad, dni, carrera, semestre, cursos):
        super().__init__(nombre, edad, dni)
        self.carrera=carrera
        self.semestre=semestre
        self.cursos=cursos

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Carrera: {self.carrera}, Semestre: {self.semestre}, Cursos: {self.cursos}"


class Profesor(Persona):
    def __init__(self, nombre, edad, dni, materia, experiencia):
        super().__init__(nombre, edad, dni)
        self.materia=materia
        self.exp=experiencia

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Materia: {self.materia}, Años de experiencia: {self.exp}"


class Administrativo(Persona):
    def __init__(self, nombre, edad, dni, departamento, cargo):
        super().__init__(nombre, edad, dni)
        self.departamento=departamento
        self.cargo=cargo

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Departamento: {self.departamento}, Cargo: {self.cargo}"


est=Estudiante("Manuel Perez", 20, 87654321, "ingenieria", 4, 50)
print(est.mostrar_info())
print()
profe=Profesor("Jose Lopez", 45, "12345678", "Matemáticas", 20)
print(profe.mostrar_info())
print()
admon=Administrativo("Maria Rodriguez", 41, 12348765, "contabilidad", "gestor de ingresos")
print(admon.mostrar_info())



