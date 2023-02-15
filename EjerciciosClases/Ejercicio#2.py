if __name__ == "__main__":
    class Punto:
        def __init__(self,puntoX,puntoY):
            self.puntoX=puntoX
            self.puntoY=puntoY
punto=Punto(3,7)
print(f"El punto es {punto.puntoX} y {punto.puntoY}")