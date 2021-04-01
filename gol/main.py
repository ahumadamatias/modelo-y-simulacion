from menucli.menucli import Menu
from GameOfLife.gameOfLife import GameOfLife
import signal, sys
from os import system

def signalHandler(sig, frame):
    system('clear')
    print('\n*******GAME OVER********\n')
    sys.exit(0)

if __name__ == '__main__':
    menu = Menu()
    menu.showMenu()
    signal.signal(signal.SIGINT, signalHandler)
    gameOfLife = GameOfLife(menu.filePattern, menu.numberGenerations)
    gameOfLife.runGame()
    sys.exit(0)
    signal.pause()