import random


def juego(vidas, ronda):
    numero = random.randint(1, 100)
    print('ronda ' + str(ronda))
    print(str(vidas) + ' vidas restantes')
    numero_elegido = int(input('Elige un número del 1 al 100: '))
    print('')
    while numero_elegido != numero and vidas > 1:
        if numero_elegido < numero:
            pista = 'mayor'
        elif numero_elegido > numero:
            pista = 'menor'
        vidas -= 1
        print(str(vidas) + ' vidas restantes')
        numero_elegido = int(input('Elige un numero ' + pista + ': '))
        print('')
    return vidas


def run():
    ronda = 1
    vidas = 10
    vidas = juego(vidas, ronda)
    while vidas != 1:
        print('Has ganado')
        print('')
        ronda += 1

        if ronda <= 5:
            vidas += 10
        elif ronda <= 10:
            vidas += 8
        elif ronda > 15:
            vidas += 5
        
        vidas = juego(vidas, ronda)
        if vidas == 1:
            break
    print('Perdiste')



if __name__ == '__main__':
    run()
