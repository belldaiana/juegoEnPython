#encoding:UTF-8
import random
import sys

puntajeUsuario = 0
puntajePc = 0
puntajeTotal = 0
ganaPc = 0
ganaUsuario = 0

def get_int():
    userdata = input("Ingrese un número, o 's' para salir del programa ")
    if userdata == 's':
        print ("Nos vemos!")
        sys.exit()
    try:
        user_num = int(userdata)
        return user_num
    except ValueError:
        print("Necesito un número para continuar: ")
        return(get_int())

def porcentaje():
    if puntajeTotal > 0:
        x = ((puntajeTotal - puntajePc) / puntajeTotal) * 100
        return x
    elif puntajeTotal == 0:
        x = 0
        return x

while True: 
    aleatorio = random.randrange(0, 5)
    eligePc = ""
    again = ""
    print("1)Piedra")
    print("2)Papel")
    print("3)Tijera")
    print("4)Lagarto")
    print("5)Spock")
    print("6)Mostrar Puntajes")
    opcion = get_int()
    
    if opcion == 1:
        eligeUsuario = "piedra"
    elif opcion == 2:
        eligeUsuario = "papel"
    elif opcion == 3:
        eligeUsuario = "tijera"
    elif opcion == 4:
        eligeUsuario = "lagarto"
    elif opcion == 5:
        eligeUsuario = "Spock"
    elif opcion == 6:
        print ("Puntajes: ")
        print ("Usuario: ", puntajeUsuario)
        print ("Pc: ", puntajePc)
        print ("Porcentaje de victorias: ", porcentaje(), "%")
    else:
        print ("Valor Invalido")
        continue
        
    print("Tu eliges: ", eligeUsuario)   
    if aleatorio == 0:
        eligePc = "piedra"
    elif aleatorio == 1:
        eligePc = "papel"
    elif aleatorio == 2:
        eligePc = "tijera"
    elif aleatorio == 3:
        eligePc = "lagarto"
    elif aleatorio == 4:
        eligePc = "Spock"
    print("PC eligio: ", eligePc)
    print("...")
    
    if eligePc == "piedra" and eligeUsuario == "papel":
        print("Ganaste, papel envuelve piedra")
        ganaUsuario = 1
    elif eligePc == "papel" and eligeUsuario == "tijera":
        print("Ganaste, tijera corta papel")
        ganaUsuario = 1
    elif eligePc == "lagarto" and eligeUsuario == "tijera":
        print("Ganaste, tijera decapita lagarto")
        ganaUsuario = 1
    elif eligePc == "tijera" and eligeUsuario == "piedra":
        print("Ganaste, piedra pisa tijera")
        ganaUsuario = 1
    elif eligePc == "lagarto" and eligeUsuario == "piedra":
        print("Ganaste, piedra aplasta lagarto")
        ganaUsuario = 1
    elif eligePc == "Spock" and eligeUsuario == "lagarto":
        print("Ganaste, lagarto envenena Spock")
        ganaUsuario = 1
    elif eligePc == "papel" and eligeUsuario == "lagarto":
        print("Ganaste, lagarto debora papel")
        ganaUsuario = 1
    elif eligePc == "tijera" and eligeUsuario == "Spock":
        print("Ganaste, Spock rompe tijera")
        ganaUsuario = 1
    elif eligePc == "piedra" and eligeUsuario == "Spock":
        print("Ganaste, Spock vaporiza piedra")
        ganaUsuario = 1
    elif eligePc == "Spock" and eligeUsuario == "papel":
        print("Ganaste, papel desautoriza Spock")
        ganaUsuario = 1

    if eligeUsuario == "piedra" and eligePc == "papel":
        print("Perdiste, papel envuelve piedra")
        ganaPc = 1
    elif eligeUsuario == "papel" and eligePc == "tijera":
        print("Perdiste, tijera corta papel")
        ganaPc = 1
    elif eligeUsuario == "lagarto" and eligePc == "tijera":
        print("Perdiste, tijera decapita lagarto")
        ganaPc = 1
    elif eligeUsuario == "tijera" and eligePc == "piedra":
        print("Perdiste, piedra pisa tijera")
        ganaPc = 1
    elif eligeUsuario == "lagarto" and eligePc == "piedra":
        print("Perdiste, piedra aplasta lagarto")
        ganaPc = 1
    elif eligeUsuario == "Spock" and eligePc == "lagarto":
        print("Perdiste, lagarto envenena Spock")
        ganaPc = 1
    elif eligeUsuario == "papel" and eligePc == "lagarto":
        print("Perdiste, lagarto debora papel")
        ganaPc = 1
    elif eligeUsuario == "tijera" and eligePc == "Spock":
        print("Perdiste, Spock rompe tijera")
        ganaPc = 1
    elif eligeUsuario == "piedra" and eligePc == "Spock":
        print("Perdiste, Spock vaporiza piedra")
        ganaPc = 1
    elif eligeUsuario == "Spock" and eligePc == "papel":
        print("Perdiste, papel desautoriza Spock")
        ganaPc = 1
    elif eligePc == eligeUsuario:
        print("Empate")
    puntajeUsuario = puntajeUsuario + ganaUsuario
    puntajePc = puntajePc + ganaPc
    puntajeTotal = puntajeUsuario + puntajePc
    while again == "":
        again = input("Jugamos de nuevo? Si/No: ")
        if 'si' in again:
            break
        elif 'no' in again:
            print("Nos vemos!")
            sys.exit()
        else:
            print("Valor Invalido")
            again = ""
            continue