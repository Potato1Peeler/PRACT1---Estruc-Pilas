class Pila:
    def __init__(self):
        self.pila=[]
        self.tope=0
        print(f"La pila esta vacia --- Tope = {self.tope}")
    def insertar(self, pila):
        if len(pila) > 8: 
            print("Error, Pila llena")
        else:
            self.pila.append(pila)
            self.tope+=1
            print(f"Se añadio el elemento {pila} a la pila {self.pila}"" --- " f"Tope = {self.tope}")
    def quitar(self):
        if len(self.pila) == 0:
            print(f"La pila esta vacia --- Tope = {self.tope}")
        else:
            quitarpila=self.pila.pop()
            self.tope-=1
            print(f"Se ha quitado el elemento {quitarpila} de la pila {self.pila}"" --- " f"Tope = {self.tope}")
            
pilas=Pila()


pilas.insertar("X")
pilas.insertar("Y")
pilas.quitar()
pilas.quitar()
pilas.quitar()
pilas.insertar("V")
pilas.insertar("W")
pilas.quitar()
pilas.insertar("R")
