class Punto:
    def __init__(self, p2X, p1X, p2Y, p1Y):
        self.p2X = p2X
        self.p1X = p1X
        self.p2Y = p2Y
        self.p1Y = p1Y

    def distancia(self):
        return (((self.p2X-self.p1X)**2)+((self.p2Y-self.p1Y)**2))**0.5


def principal():
    obj = Punto(10,0,0,0)
    print ('La distancia entre los puntos p1 y p2 es: ',obj.distancia())

if __name__ == '__main__':
    principal()