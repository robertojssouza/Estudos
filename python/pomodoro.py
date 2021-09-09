from time import sleep
import os

def leiaSeg():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    while True:
        try:
            t = int(input('Digite quantos minutos você vai trabalhar entre as pausas: ')) * 60
            return t
        
        except (ValueError, TypeError):
            print('Digite um valor válido')
            continue
           
     
def contador():
    try:
        t = leiaSeg()
        while t:
            min = t // 60
            sec = t % 60
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'{min:02d}:{sec:02d}')
            sleep(0.2)
            t -= 1
        print('Está na hora de esticar o esqueleto, beber água ou café')
        sleep(10)
    except (KeyboardInterrupt):
        print('O usuário interrompeu o programa.')



contador()
