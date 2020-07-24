#Basado de: https://stackabuse.com/the-bridge-design-pattern-in-python/

class Color:
    def figura_cubo(self, tipo):
        pass
    
    def figura_esfera(self, tipo):
        pass
    
class Azul(Color):
    def figura_cubo(self, tipo):
        print("El cubo es azul de intensidad:", tipo)
        
    def figura_esfera(self, tipo):
        print("El cubo es rojo de intensidad: ", tipo) 

class Rojo(Color):
    def figura_cubo(self, tipo):
        print("La esfera es azul de intensidad: ",  tipo )
        
    def figura_esfera(self, tipo):
        print("La esfera es azul de intensidad: ",  tipo)


class Figura:
    def __init__(self, Color):
        self.color = Color
        
    def imprimir_color(self):
        pass
    
    def aumentar_intensidad(self):
        pass
    
class Esfera(Figura):
    def __init__(self, Color, intensidad):
        super().__init__(Color)
        self.intensidad = intensidad

    def imprimir_color(self):
        self.color.figura_esfera(self.intensidad)

    def aumentar_intensidad(self, nueva_intensidad):
        self.intensidad += nueva_intensidad  

class Cubo(Figura):
    def __init__(self, Color, intensidad):
        super().__init__(Color)
        self.intensidad = intensidad

    def imprimir_color(self):
        self.color.figura_cubo(self.intensidad)

    def aumentar_intensidad(self, nueva_intensidad):
        self.intensidad += nueva_intensidad
rojo= Rojo()
azul = Azul()


cubo= Cubo(rojo , 100)
cubo.imprimir_color()
cubo.aumentar_intensidad(25)
cubo.imprimir_color()

esfera = Esfera(azul,10)
esfera.imprimir_color()

cubo2 = Cubo(azul , 120)
cubo2.imprimir_color()

esfera2 = Esfera(rojo,200)
esfera2.imprimir_color()


