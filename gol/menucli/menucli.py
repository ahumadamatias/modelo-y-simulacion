class Menu:
    filePattern = ''
    numberGenerations = 0
    
    def showMenu(self):
        print("**********Game of Life*********")
        print("Instrucciones:")
        print("1- Cree un archivo .txt a la misma altura del main con la siguiente forma:\n0 1 0\n0 0 1\n1 1 1")
        print("*Donde los 0 son celdas muertas y los 1 celdas viva*")
        print("*El tamaño de la matriz puede ser cualquiera siempre que sea cuadrada se recomienda 10x10*")
        self.filePattern = input("2- Ingrese el nombre del archivo: ")
        self.numberGenerations = int(input("2- Ingrese la cantidad de generaciones a recorrer: "))