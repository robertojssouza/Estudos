from time import sleep
import os


def contador():
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        try:
            t = int(input('Digite quantos minutos você vai trabalhar entre as pausas: ')) * 60
            while t:
                min = t // 60
                sec = t % 60
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f'{min:02d}:{sec:02d}')
                sleep(1)
                t -= 1
            print('Está na hora de esticar o esqueleto, beber água ou café')
            sleep(10)
            break

        except (ValueError, TypeError):
            print('Digite um valor válido')
            continue

        except (KeyboardInterrupt):
            print('O usuário interrompeu o programa.')
            break



contador()
