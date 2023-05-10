class Personas:
    def __init__(self, Nombre, Apellido, Ocupacion, edad, Genero):
        self.Nombre=Nombre
        self.Apellido=Apellido
        self.Ocupacion=Ocupacion
        self.Edad=edad
        self.Genero=Genero

    def Presentarse (self):
        print(f"Hola, buenos dias Mi nombre \n" + self.Nombre, self.Apellido )
        print(f"Mi ocupacion es \n"+ self.Ocupacion +"\n"+
              "Tengo " +self.Edad +"años")
        print(f"Soy \n"+self.Genero)
persona1=Personas("Jeremy","Rodriguez","Estudiante" ,"19", "Hombre")
persona1.Presentarse()


#------------inheritence----------------------------------------------#


class Profesional(Personas):
    def __init__(self, Nombre, Apellido, Ocupacion, edad, Genero, Hijos):
        super().__init__(Nombre, Apellido, Ocupacion, edad, Genero)
        self.Hijos=Hijos
        
    def Presentarse2 (self):
        print(f"Hola, buenos dias Mi nombre \n" + self.Nombre, self.Apellido )
        print(f"Mi ocupacion es \n"+ self.Ocupacion +"\n"+
              "Tengo " +self.Edad +"años")
        print(f"Soy \n"+self.Genero)
        print(f"Tengo hijos, tengo"+self.Hijos)

        
persona2=Profesional ("jeremy", "Rodriguez", "Ingenieron de sistemas", "21", "Hombre"," 3 hijos" ) 
persona2.Presentarse2()
