# EJERCICIO CLASE 10

#   Definir una clase llamada Car para representar objetos tipo coche que tenga:
#   atributos de datos: marca, modelo, combustible, cilindrada, pos_x, pos_y
#   métodos:
#   move_to(pos_x, pos_y): asigna valores a los correspondientes atributos de datos
#   move_incr(x, y): modifica la posicion incrementado el valor actual de x e y
#   get_pos(): devuelve la posición actual del coche
#   __init__(marca, modelo, combustible, cilindrada): inicializa los atributos con valoresde los argumentos. inicializa la posicion x e y a cero
#   crear una lista de objetos Car en la que cada elemento sea un objeto con la informacion de cada diccionario de la lista de diccionarios del ejercicio 9
#   invocar todos los métodos del objeto instaciado
#   almacenar la lista de objetos en disco usando json
#   borra los objetos de la lista


class Car:
    """class represent and manage cars"""

    num_cars = 0

    def __init__(self, marca, modelo, combustible, cilindrada):
        self.marca = marca
        self.modelo = modelo
        self.combustible = combustible
        self.cilindrada = cilindrada
        self.pos_x = 0
        self.pos_y =

    def move_to(x, y)
        self.pos_x = x
        self.pos_y = y

    def move_incr(x, y):
        self.pos_x += x
        self.pos_y += y

    def get_pos():
        return self.pos_x, self.pos_y