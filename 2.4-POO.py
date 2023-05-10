class Materias:
    def __init__(self, Nombre, Nombre_en_ingles,para_que_sirve) :
        self.Nombre=Nombre
        self.Nombre_en_ingles=Nombre_en_ingles
        self.para_que_sirve=para_que_sirve
    
    def presentarse (self):
        print(f"Hola, mi nombre es " +self.Nombre , "y mi nombre en ingles es " +self.Nombre_en_ingles)
        print(f"¿Para que sirvo? " +self.para_que_sirve)
Materias1=Materias("Matematicas","math","nos hacen razonar mediante una fórmula lógica, utilizando datos reales que son verificables. Esto nos permite enfrentarnos al mundo buscando respuestas basadas en evidencias y no solo en creencias o emociones.")
Materias1.presentarse()


#------------inheritence--------------------------------------#

class MateriasS(Materias):
    def __init__(self, Nombre, Nombre_en_ingles, para_que_sirve):
        super().__init__(Nombre, Nombre_en_ingles, para_que_sirve)
    
Materias2=MateriasS("Ciencias Sociales" , "social Sciences", "Con frecuencia proveo ideas, información y conceptos para ayudarnos a entender el mundo en el que vivimos, quiénes somos, de dónde venimos y hacia dónde vamos. Ayudan a pensar los problemas colectivos que enfrentamos y a imaginar maneras más justas de organizar la vida social.")
Materias2.presentarse()