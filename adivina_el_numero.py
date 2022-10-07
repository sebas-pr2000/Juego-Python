#importando modulo
import random


def run():
    #definiendo vidas
    vidas = 10
    #variables 
    numero_aleatorio = random.randint(1,100)
    numero_elegido = int(input("Elige un número del 1 al 100: "))
    
    if numero_elegido > 0 and numero_elegido < 101:
        while numero_elegido != numero_aleatorio and vidas > 0:
            if numero_elegido < numero_aleatorio:
                print("Te quedan " + str(vidas) + " Vidas")
                print("Busca un número más Grande")
                vidas -= 1
            else:
                print("Te quedan " + str(vidas) + " Vidas")
                print("Busca un número más Pequeño")    
                vidas -= 1
            numero_elegido = int(input("Elige otro número: "))
        if vidas > 0:    
            print("GANASTE!")     
        else:
            print("Lo siento perdiste el numero era " + str(numero_aleatorio))
    else:
          print("Debes de Elegir un número entre el 1 y el 100")
          run()

if __name__ == "__main__":
    run()