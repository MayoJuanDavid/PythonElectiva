#1. - Escribe un programa que convierta temperaturas, longitudes o pesos entre distintas unidades. 
#Usa un menú para que el usuario elija qué convertir (por ejemplo: Celsius a Fahrenheit, metros a pies, 
#kilogramos a libras, etc.).
import os
siguiente = ''

def menu_temperatura():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la consola

    opcion1 = ''
    opcion2 = ''
    while True:
        print(r"""
████████╗███████╗███╗   ███╗██████╗ 
╚══██╔══╝██╔════╝████╗ ████║██╔══██╗
   ██║   █████╗  ██╔████╔██║██████╔╝
   ██║   ██╔══╝  ██║╚██╔╝██║██╔═══╝ 
   ██║   ███████╗██║ ╚═╝ ██║██║     
   ╚═╝   ╚══════╝╚═╝     ╚═╝╚═╝     
""")
        print("Seleccione su medida")
        print("1.- Celsius")
        print("2.- Kelvin")
        print("3.- Fahrenheit")
        print("4.- Volver atras")
        print("0.- Salir")
        
        opcion1 = input("Selecciona tu medida: ")

        opcion2 = input("selecciona la medida de conversion: ")

        valor = input("Introduzca el valor a convertir: ")
        valor = float(valor)



        if opcion1 == "1":
            if opcion2 == "2":
                valor = valor + 273.15
                print("El valor de celsius a kelvin es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "3":
                valor = (valor * 9/5) + 32
                print("El valor de celsius a fahrenheit es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

        if opcion1 == "2":
            if opcion2 == "1":
                valor = valor - 273.15
                print("El valor de kelvin a celsius es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return
            elif opcion2 == "3":
                valor = (valor - 273.15) * 9/5 + 32
                print("El valor de kelvin a fahrenheit es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

        
        if opcion1 == "3":
            if opcion2 == "1":
                valor = (valor - 32) * 5/9
                print("El valor de fahrenheit a celsius es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return
            elif opcion2 == "2":
                valor = (valor - 32) * 5/9 + 273.15
                print("El valor de fahrenheit a kelvin es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return
        if opcion1 or opcion2 == 4:
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la consola
            menu_principal()  
        else:
            menu_principal()

def menu_longitud():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la consola

    opcion1 = ''
    opcion2 = ''
    while True:
        print(r"""
██╗      ██████╗  ███╗   ██╗ ██████╗ 
██║     ██╔═══██╗ ████╗  ██║██╔════╝ 
██║     ██║   ██║ ██╔██╗ ██║██║  ███╗
██║     ██║   ██║ ██║╚██╗██║██║   ██║
███████╗╚██████╔╝ ██║ ╚████║╚██████╔╝
╚══════╝ ╚═════╝  ╚═╝  ╚═══╝ ╚═════╝ 
""")

        print("Seleccione su medida")
        print("1.- Kilometro")
        print("2.- Hectometro")
        print("3.- Decametro")
        print("4.- Metro")
        print("5.- Decimetro")
        print("6.- Centimetro")
        print("7.- Milimetro")
        print("8.- volver atras")
        print("0.- Salir")
        
        opcion1 = input("Selecciona tu medida: ")

        opcion2 = input("selecciona la medida de conversion: ")

        valor = input("Introduzca el valor a convertir: ")
        valor = float(valor)



        if opcion1 == "1":
            if opcion2 == "2":
                valor = valor *10
                
            elif opcion2 == "3":
                valor = valor *100
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return
                
            elif opcion2 == "4":
                valor = valor *1000
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "5":
                valor = valor *10000
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "6":
                valor = valor *100000
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "7":
                valor = valor *1000000
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

        if opcion1 == "2":
            if opcion2 == "1":
                valor = valor /10
                
            elif opcion2 == "3":
                valor = valor *10
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return
                
            elif opcion2 == "4":
                valor = valor *100
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "5":
                valor = valor *1000
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "6":
                valor = valor *10000
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "7":
                valor = valor *100000
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return
        
        if opcion1 == "3":
            if opcion2 == "1":
                valor = valor /100
                
            elif opcion2 == "2":
                valor = valor /10
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return
                
            elif opcion2 == "4":
                valor = valor *10
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "5":
                valor = valor *100
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "6":
                valor = valor *1000
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "7":
                valor = valor *10000
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

        if opcion1 == "4":
            if opcion2 == "1":
                valor = valor /1000
                
            elif opcion2 == "2":
                valor = valor /100
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return
                
            elif opcion2 == "3":
                valor = valor /10
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "5":
                valor = valor *10
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "6":
                valor = valor *100
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "7":
                valor = valor *1000
                print("El nuevo valor es: ",valor)  
                input("Presiona Enter para volver al menú principal...")
                return  

        if opcion1 == "5":
            if opcion2 == "1":
                valor = valor /10000
                
            elif opcion2 == "2":
                valor = valor /1000
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return
                
            elif opcion2 == "3":
                valor = valor /100
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "4":
                valor = valor /10
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "6":
                valor = valor *10
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "7":
                valor = valor *100
                print("El nuevo valor es: ",valor) 
                input("Presiona Enter para volver al menú principal...")
                return
        
        if opcion1 == "6":
            if opcion2 == "1":
                valor = valor /100000
                
            elif opcion2 == "2":
                valor = valor /10000
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return
                
            elif opcion2 == "3":
                valor = valor /1000
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "4":
                valor = valor /100
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "5":
                valor = valor /10
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "7":
                valor = valor *10
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

        if opcion1 == "7":
            if opcion2 == "1":
                valor = valor /1000000
                
            elif opcion2 == "2":
                valor = valor /100000
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return
                
            elif opcion2 == "3":
                valor = valor /10000
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "4":
                valor = valor /1000
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return

            elif opcion2 == "5":
                valor = valor /100
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return
            

            elif opcion2 == "6":
                valor = valor /10
                print("El nuevo valor es: ",valor)
                input("Presiona Enter para volver al menú principal...")
                return
            
        if opcion1 or opcion2 == 8:
            os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la consola
            menu_principal()    
        
        else:
            menu_principal()

def menu_peso():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la consola

    factores = {
        "1": 1000000,   # Tonelada
        "2": 100000,    # Quintal
        "3": 1000,      # Kilogramo
        "4": 100,       # Hectogramo
        "5": 10,        # Decagramo
        "6": 1,         # Gramo (base)
        "7": 0.1,       # Decigramo
        "8": 0.01,      # Centigramo
        "9": 0.001      # Miligramo
    }

    while True:
        print(r"""
██████╗ ███████╗███████╗ ██████╗ 
██╔══██╗██╔════╝██╔════╝██╔═══██╗
██████╔╝█████╗  ███████╗██║   ██║
██╔═══╝ ██╔══╝  ╚════██║██║   ██║
██║     ███████╗███████║╚██████╔╝
╚═╝     ╚══════╝╚══════╝ ╚═════╝ 
""")
        print("Seleccione su medida")
        print("1.- Tonelada")
        print("2.- Quintal")
        print("3.- Kilogramo")
        print("4.- Hectogramo")
        print("5.- Decagramo")
        print("6.- Gramo")
        print("7.- Decigramo")
        print("8.- Centigramo")
        print("9.- Miligramo")
        print("B.- Volver atrás")
        print("0.- Salir")

        opcion1 = input("Selecciona tu medida de origen: ").upper()
        if opcion1 == "0":
            exit()
        elif opcion1 == "B":
            
            menu_principal()

        opcion2 = input("Selecciona la medida de conversión: ").upper()
        if opcion2 == "0":
            exit()
        elif opcion2 == "B":
            
            menu_principal()


        try:
            valor = float(input("Introduzca el valor a convertir: "))

            # Convertir a gramos primero, luego a la unidad destino
            valor_en_gramos = valor * factores[opcion1]
            valor_convertido = valor_en_gramos / factores[opcion2]

            print(f"\nEl nuevo valor es: {valor_convertido}\n")
            input("Presione Enter para continuar...")
        except (ValueError, KeyError):
            print("Entrada no válida. Intente nuevamente.")
            input("Presione Enter para continuar...")

def menu_principal():
    os.system('cls' if os.name == 'nt' else 'clear')  # Limpia la consola

    while True:
        print(r"""
            ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
            ████╗ ████║██╔════╝████╗  ██║██║   ██║
            ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
            ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
            ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
            ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ """)
        print("Bienvenido al menu conversor")
        print("Que quieres convertir?")
        print("1.- Temperaturas")
        print("2.- Longitudes")
        print("3.- Peso")
        print("0.- Salir")

        opcion = input("Selecciona una opcion del 1-4: ")

        if opcion == "1":
            menu_temperatura()
        elif opcion == "2":
            menu_longitud()
        elif opcion == "3":
            menu_peso()
        elif opcion == "0":
            break
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Error en la seleccion")
            siguiente = input("Dale a cualquier tecla para volver a empezar ")
            os.system('cls' if os.name == 'nt' else 'clear')
            menu_principal()

menu_principal()