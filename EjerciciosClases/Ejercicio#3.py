if __name__ == "__main__":
    class Punto:
        def __init__(self,puntoX,puntoY):
            self.puntoX=puntoX
            self.puntoY=puntoY

        def MostrarPunto(self):
            print(f"El punto es {self.puntoX} y {self.puntoY}")

        def MoverPunto(self):
            nuevoX=int(input("Digite nuevo punto X\n"))
            nuevoY=int(input("Digite nuevo punto Y\n"))
            print(f"Los anteriores puntos eram {self.puntoX} y {self.puntoY}")
            print(f"Los nuevos puntos son {nuevoX} y {nuevoY}")
            puntoViejoX = self.puntoX
            puntoViejoY = self.puntoY
            self.puntoX=nuevoX
            self.puntoY=nuevoY

        def Distancia(self):
            pX=int(input("Enter new parameter in X\n"))
            pY=int(input("Enter new parameter in Y\n"))
            total=(pX-self.puntoX)**2+(pY+self.puntoY)**2
            print(f"La distancia total es: ",total)

hola=Punto(3,3)
hola.Distancia()



