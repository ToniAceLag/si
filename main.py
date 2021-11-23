import libre as l


def main():
    numero = l.valid_number(1, "Insert a natural number: ")
    print(numero)
    cosa = l.sernar_o_parell(0,2,"Insert a number or a 0 if u want to finish: ", "The number is odd: ", "The number is even: ")
    print(cosa)
    prueba_tres = l.valid_number_in_range(0,10,"Introdueix un nombre entre 0 i 10:","Aquest es el teu numero: ")
    print(prueba_tres)
    prueba_cuatro = l.are_equals("Instert a non decimal and natural number: ","The first number is bigger than the second: ","The numbers are equal: ","The second number is bigger than the first: ")
    print(prueba_cuatro)
    prueba_cinco = l.quantity_of_digits("Inster a number to know how many digits it have's: ")
    print(prueba_cinco)
if __name__ == '__main__':
    main()


