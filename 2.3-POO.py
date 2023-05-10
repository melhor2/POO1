class Textos:
    def __init__(self, Nombre, Nombre_en_ingles,para_que_sirve) :
        self.Nombre=Nombre
        self.Nombre_en_ingles=Nombre_en_ingles
        self.para_que_sirve=para_que_sirve
    
    def presentarse (self):
        print(f"Hola, mi nombre es " +self.Nombre , "y mi nombre en ingles es " +self.Nombre_en_ingles)
        print(f"¿Para que sirvo? " +self.para_que_sirve)
Textos1=Textos("texto descriptivo","descriptive text","Mi objetivo principal es informar acerca de cómo es, ha sido o será una persona, objeto o fenómeno")
Textos1.presentarse()

#------------inheritence--------------------------------------#

class textosC (Textos):
    def __init__(self, Nombre, Nombre_en_ingles, para_que_sirve):
        super().__init__(Nombre, Nombre_en_ingles, para_que_sirve)
    
textos2=textosC("Texto científico", "Cientific text","Mi objetivo estransmitir, de manera apropiada, clara y concisa, los resultados de un trabajo de investigación en un tema específico a la comunidad científica, así como al público interesado en general.")
textos2.presentarse()