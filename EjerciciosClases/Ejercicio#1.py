if __name__ == "__main__":
    class Vehiculo:
        def __init__(self,velocidad_maxima,kilometraje ):
            self.velocidad_maxima=velocidad_maxima
            self.kilometraje=kilometraje

carro=Vehiculo(34,56)
print(carro.kilometraje)
print(carro.velocidad_maxima)
