if __name__ == "__main__":
    class Punto:
        def __init__(self,puntoX,puntoY):
            self.puntoX=puntoX
            self.puntoY=puntoY

        def MostrarPunto(self):
            print(f"El punto es {self.puntoX} y {self.puntoY}")

punto=Punto(3,7)
punto.MostrarPunto()
