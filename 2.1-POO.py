class Cuerpos_celestes:
    def __init__(self, Nombre, Apodo, Nombre_en_ingles, edad):
        self.Nombre=Nombre
        self.Apodo=Apodo
        self.Nombre_en_ingles=Nombre_en_ingles
        self.Edad=edad
        

    def Presentarse (self):
        print(f"Hola, Mi nombre \n" + self.Nombre , "y mi apodo es" +self.Apodo  )
        print(f"Mi nombre en Ingles es \n"+ self.Nombre_en_ingles +"\n"+
              "Tengo " +self.Edad +" de años")
Cc1=Cuerpos_celestes("estrella","Nair, Aldebarán, Algieba, Alioth, Aludra \nTengo muchos apodos:D", "star", "1000 millones ")
Cc1.Presentarse()

#------------inheritence--------------------------------------#

class Meteoroides (Cuerpos_celestes):
    def __init__(self, Nombre, Apodo, Nombre_en_ingles, edad):
        super().__init__(Nombre, Apodo, Nombre_en_ingles, edad)

Cc2=Meteoroides("Meteoroides", " meteoro,fenómeno luminoso","meteoroids" , "4 600 millones ")
Cc2.Presentarse()