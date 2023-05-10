class Bebidas:
    def __init__(self, Nombre, azucar, mercado, precio):
        self.Nombre=Nombre
        self.Azucar=azucar
        self.mercado=mercado
        self.precio=precio
        

    def Presentarse (self):
        print(f"Hola, Mi nombre \n" + self.Nombre   )
        print(f"Tengo " +self.mercado + " a la venta")
        print(f"Tengo " +self.Azucar)
        print(f"Mi precio actual es  " +self.precio)
Bd1=Bebidas("Coca-cola","45 gramos en envase de 600mL" , "131 años ","$5.900")
Bd1.Presentarse()


#------------inheritence--------------------------------------#


class Bebidas2(Bebidas):
    def __init__(self, Nombre, azucar, mercado, precio):
        super().__init__(Nombre, azucar, mercado, precio)

Bd2=Bebidas2("Sprite","6,6 gramos en una lata de 33 cl","100 años", "$4.500")
Bd2.Presentarse()