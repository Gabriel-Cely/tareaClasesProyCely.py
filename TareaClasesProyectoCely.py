# Autor: Gabriel Cely, clase POO 
# Ejercicio: crear una encuesta con los objetivos para el proyecto
print ("Esta encuesta tiene como objetivo recolectar informacion sobre los objetivos del proyecto y sus participantes")

class Pregunta:
    def __init__(self, texto):
        self.texto = texto
        self.respuesta = None

    def mostrar_pregunta(self):
        self.respuesta = input(self.texto + " ")

class Encuesta:
