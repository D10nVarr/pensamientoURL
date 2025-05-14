dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

niveles_azucar = [130, 160, 95, 175, 160] # mg/dL
niveles_sal = [2000, 2400, 1800, 2400, 2700] # mg
presion = [115, 130, 110, 125, 175] # mmHg

print("Niveles de azucar en la sangre:")
for i in range(len(dias)):
        j= niveles_azucar[i]
        
        if j>70 and j<140:
            print(f"En el dia {dias[i]}: los niveles de azucar son saludables")
        else:
            print(f"En el dia {dias[i]}: los niveles de azucar son saludables")

print("\nNivel de consumo de sal:")
for i in range(len(dias)):
        j= niveles_sal[i]
        
        if j<2300:
            print(f"En el dia {dias[i]}: el consumo del sal es saludable")
        else:
            print(f"En el dia {dias[i]}: el consumo del sal no es saludable")

print("\nLa presion arterial esta en el rango de:")
for i in range(len(dias)):
        j= presion[i]
        
        if j<139 and j>130:
            print(f"En el dia {dias[i]}: Hipertensión tipo 1")
        elif j>= 140:
            print(f"En el dia {dias[i]}: Hipertensión tipo 2")