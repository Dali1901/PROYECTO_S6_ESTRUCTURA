# import os
# os.system("cls")

class Menusp6:
    def __init__(self):
        pass
    def menu(self,opciones,titulo):
        print(titulo)
        for x in opciones:
            print(x)
        opc = input("Elija la Opción[1...{}]: ".format(len(opciones)))
        return opc


