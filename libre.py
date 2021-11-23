def valid_number(val, msg):
    num = int(input(msg))
    while num < val:
        num = int(input(msg))
    return num

def sernar_o_parell(value ,second_val, msg, msg2, msg3):
    num = int(input(msg))
    while num >value:#verifica si el numero es mayor que el numero decidido por el usuario
        if num % second_val == 1: # Comprueba que si el numero residuo del numero divido entre el numero da 1
            print(msg2)#en el mensaje podra poner si es un multiple del numero o si es impar
        else:
            print(msg3)#en el
            # parejo
        num = int(input(msg))
    return num

def valid_number_in_range(val, val_dos,  msg, msg_tw):
    num = int(input(msg))

    while num <= val or num >= val_dos:
        num = int(input(msg))
    print(msg_tw, num)
    return num

def are_equals( msg, msg_o, msg_x, msg_y):
    primer_numero_enter = int(input(msg))
    segon_numero_enter = int(input(msg))
    if primer_numero_enter > segon_numero_enter:
        print(msg_o)
    elif primer_numero_enter == segon_numero_enter:
        print(msg_x)
    elif segon_numero_enter > primer_numero_enter:
        print(msg_y)
    else:
        print("ERROR")
def quantity_of_digits(msg):
    numero_entero = int(input(msg))
    contador = len(str(numero_entero))
    print("It have:", contador, "digits")

def digits_number(msg,msg_u,msg_d):
    numero = int(input(msg))
    contador_digitos = 0
    if numero < 0:
        numero *= -1
    while numero > 0:
        contador_digitos = contador_digitos + 1
        numero = numero // 10

    print(msg_u, contador_digitos, msg_d)
