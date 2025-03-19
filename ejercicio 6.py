saldo=3000

intentos=3

while saldo > 0:
    print("Saldo actual: Q",saldo)
    monto = int(input("Ingrese monto a retirar (0 para salir): "))
            
    if monto == 0:
        print("Operación cancelada. Adiós.")
        break
            
    if monto > saldo:
        intentos -= 1
        if intentos == 0:
            print("Se agotaron los intentos. Operación bloqueada.")
            break
        print("Saldo insuficiente. Intentos restantes:",intentos)
    else:
        saldo -= monto
        print("Retiro exitoso. Nuevo saldo: Q",saldo)
        if saldo == 0:
            print("Saldo agotado. Adiós.")
            break
