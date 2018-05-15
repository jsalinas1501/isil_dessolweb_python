from tarea51 import Punto


class Triangulo(Punto):
    
    def __init__(self, p2X, p1X, p2Y, p1Y):
        self.p2X = p2X
        self.p1X = p1X
        self.p2Y = p2Y
        self.p1Y = p1Y

    def perimetro(self, d1, d2, d3):
        return d1+d2+d3


def principal():
    obj = Triangulo(10,0,0,0)
    d1 = obj.distancia()
    obj = Triangulo(30,0,0,0)
    d2 = obj.distancia()
    obj = Triangulo(50,0,0,0)
    d3 = obj.distancia()
    print ('El perimetro es: ',obj.perimetro(d1,d2,d3))

if __name__ == '__main__':
    principal()