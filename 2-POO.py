class Animales:
    def __init__(self, Nombre, Apodo, Nombre_en_ingles, edad, Genero,Especie):
        self.Nombre=Nombre
        self.Apodo=Apodo
        self.Nombre_en_ingles=Nombre_en_ingles
        self.Edad=edad
        self.Genero=Genero
        self.Especie=Especie

    def Presentarse (self):
        print(f"Hola, Mi nombre \n" + self.Nombre , "y mi apodo es" +self.Apodo  )
        print(f"Mi nombre en Ingles es \n"+ self.Nombre_en_ingles +"\n"+
              "Tengo " +self.Edad +"años")
        print(f"Soy \n"+self.Genero)
        print(f"¿Eres carnivoro herbivoro o omnivoro? " +self.Especie)
Animal1=Animales("hipopotamo","caballo de río", "Hippo", "31", "Hombre", "Soy herbivoro")
Animal1.Presentarse()


#------------inheritence--------------------------------------#

class Hijos_A(Animales):
    def __init__(self, Nombre, Apodo, Nombre_en_ingles, edad, Genero, Especie, Hijos):
        super().__init__(Nombre, Apodo, Nombre_en_ingles, edad, Genero, Especie)
        self.Hijos=Hijos
    
    def Presentarse2 (self):
        print(f"Hola, Mi nombre \n" + self.Nombre , "y mi apodo es" +self.Apodo  )
        print(f"Mi nombre en Ingles es \n"+ self.Nombre_en_ingles +"\n"+
              "Tengo " +self.Edad +"años")
        print(f"Soy \n"+self.Genero)
        print(f"¿Eres carnivoro herbivoro o omnivoro?" +self.Especie)
        print(f"Tengo Hijos, tengo"+self.Hijos)
Animal2=Hijos_A("hipopotamo","caballo de río", "Hippo", "20", "Mujer", "Soy herbivoro"," 1")
Animal2.Presentarse2()
