class Punto2D():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return "(%d, %d)" % (self.x, self.y)

    def cuadrante(self):
        if self.x == 0 and self.y == 0:
            return 0
        if self.x > 0 and self.y > 0:
            return 1
        if self.x < 0 and self.y > 0:
            return 2
        if self.x < 0 and self.y < 0:
            return 3
        return 4

class PuntoMejorado(Punto2D):
    pass

if __name__ == "__main__":
    punto = Punto2D(1,2)
    punto_2 = Punto2D(-3,4)

    print(punto.__str__() + " esta en el cuadrante : " + str(punto.cuadrante()))
    print(punto_2.__str__() + " esta en el cuadrante : " + str(punto_2.cuadrante()))
