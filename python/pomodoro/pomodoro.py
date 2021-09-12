from time import sleep
import os

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def leia_seg():
    limpa_tela()
    
    while True:
        try:
            t = int(input('Digite quantos minutos você vai trabalhar até a próxima pausa: ')) * 60
            return t
        
        except (ValueError, TypeError):
            print('\033[31mDigite um valor válido\033[39m')
            continue
           

def valida_sim():
    voltar = str(input('Digite "sim" para voltar ao trabalho: ')).lower().strip()

    while voltar != 'sim':
        voltar = str(input('Digite \033[31m"sim"\033[39m para voltar ao trabalho: ')).lower().strip()
    
    if voltar == 'sim':
        return contador()


def contador():
    try:
        t = leia_seg()
        
        while t:
            min = t // 60
            sec = t % 60
            limpa_tela()
            print(f'{min:02d}:{sec:02d}')
            sleep(1)
            t -= 1

        limpa_tela()
        print('\033[34mEstá na hora de esticar o esqueleto, beber água ou café\033[39m')
        sleep(10)
        valida_sim()

    except (KeyboardInterrupt):
        print('O usuário interrompeu o programa.')



contador()
