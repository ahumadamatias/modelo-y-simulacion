from time import sleep
from os import system
import numpy as np

class GameOfLife:
    golBoard = []
    golBoardAux = []
    row = 0
    column = 0
    filePattern = ''
    numberGenerations = 0
    quantityAliveCell = 0
    quantityDeadCell = 0
    
    def __init__(self, filePattern, numberGenerations):
        self.filePattern = filePattern
        self.numberGenerations = numberGenerations

    def createBoardFromFile(self):
        self.golBoard = np.loadtxt(self.filePattern, delimiter=' ', dtype='int')
        self.golBoardAux = np.copy(self.golBoard)
        self.row = len(self.golBoard)
        self.column = len(self.golBoard[0])
        self.calculateAliveCell()
        self.calculateDeadCell()

    def searchForSurvivors(self):
        for x in range(self.row):
            for y in range(self.column):
                xaux = x
                xaux2 = x
                yaux = y
                yaux2 = y
                if yaux2 + 1 == self.column:
                    yaux2 = -1
                if xaux2 + 1 == self.row:
                    xaux2 = -1
                if yaux - 1 == -1:
                    yaux = self.column
                if xaux - 1 == -1:
                    xaux = self.row
                
                sum = self.golBoard[xaux2 + 1][yaux2] + self.golBoard[xaux - 1][yaux2] + self.golBoard[xaux2][yaux2 + 1] + self.golBoard[xaux2][yaux - 1] + self.golBoard[xaux2 + 1][yaux2 + 1] + self.golBoard[xaux - 1][yaux2 + 1] + self.golBoard[xaux - 1][yaux - 1] + self.golBoard[xaux2 + 1][yaux - 1]

                if self.golBoard[x][y] == 1 and (sum == 2 or sum == 3):
                    self.golBoardAux[x][y] = 1
                elif self.golBoard[x][y] == 0 and sum == 3:
                    self.golBoardAux[x][y] = 1
                else:
                    self.golBoardAux[x][y] = 0
        self.calculateAliveCell()
        self.calculateDeadCell()

    def showGolBoard(self):
        print("\n")
        for x in self.golBoardAux:
            print('\t', x)
        print("\n")
    
    def showInfoGame(self, generations):
        print('Cantidad de generaciones recorridas: ', generations)
        print('Cantidad de celdas vivas en la generacion actual: ', self.quantityAliveCell)
        print('Cantidad de celdas muertas en esta generacion: ', self.quantityDeadCell)
        print('*Para terminar el juego presione ctrl+c*')
        
    def calculateAliveCell(self):
        aliveCell = np.where(self.golBoardAux == 1)
        self.quantityAliveCell = len(aliveCell[0])
        
    def calculateDeadCell(self):
        deadCell = np.where(self.golBoardAux == 0)
        self.quantityDeadCell = len(deadCell[0])
        
    def runGame(self):
        self.createBoardFromFile()
        i = 1
        while i <= self.numberGenerations and self.quantityDeadCell != 100:
            system('clear')
            self.showInfoGame(i)
            self.showGolBoard()
            self.searchForSurvivors()
            self.golBoard = np.copy(self.golBoardAux)
            i += 1
            sleep(1)
        
        if self.quantityDeadCell == 100:
            system('clear')
            print('En la generacion numero ', i, ' todas las celdas quedaron muertas')
            self.showGolBoard()