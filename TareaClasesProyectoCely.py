# Autor: Gabriel Cely, clase POO 
# Ejercicio: crear una encuesta con los objetivos para el proyecto

def main():
    print("Esta encuesta tiene como objetivo recolectar informacion sobre los objetivos del proyecto y sus participantes")

    class Pregunta:
        def __init__(self, texto):
            self.texto = texto
            self.respuesta = None

        def mostrar_pregunta(self):
            self.respuesta = input(self.texto + " ")

    class Encuesta:
        def __init__(self, preguntas):
            self.preguntas = preguntas  

        def mostrar_encuesta(self):
            for pregunta in self.preguntas:
                pregunta.mostrar_pregunta()


    for i in range(1, 11):
        print(f"\nPREGUNTAS PARA LA PERSONA {i}")
        pregunta1 = Pregunta("¿Cuál es tu nombre?")
        pregunta2 = Pregunta("¿Cuál es tu edad?")
        pregunta3 = Pregunta("¿Cuál es tu idea de proyecto?")
        pregunta4 = Pregunta("¿Conoces otras librerías de python?")
        encuesta = Encuesta([pregunta1, pregunta2, pregunta3, pregunta4])
        encuesta.mostrar_encuesta()
        print("Respuestas:")
        for pregunta in encuesta.preguntas:
            print(f"{pregunta.texto} {pregunta.respuesta}")


main()