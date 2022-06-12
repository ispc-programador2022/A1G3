import time, os

class Presentation:
  
    def presentacion(self):
        users=[
            'ABATI, KAREN',
            'ABDENUR, LUCAS',
            'ACUÑA, PÍA',
            'AGUSTI, YASMIN',
            'ALONSO, MARCOS',
            'ALVAREZ, AGUSTIN',
            'AMUSQUIBAR, BARBARA',
            'ARANDA VILLARREAL, KEVIN AXEL',
            'ARECO, WALTER',
            'ARELLANO COVARRUBIAS, ADOLFO IGNACIO',
            'ARGUELLO, SOLEDAD',
            'ARRIOLA, GABRIEL',
            'ASTRADA, ANDRES EMILIANO'
            ]
        print("Bienvenidos somos el Grupo 3 del Aula 1")
        print("Situación profesional 1 - Proyecto en equipo")
        print("Integrantes:")
        for alumno in users:
            print(">> ", alumno)
        print("\n" * 5)    
        print("se limpiara en 5 seg...")
        self.limpiar()

    def limpiar(self):
        time.sleep(5)
        os.system('cls')  
