class Personas:
    def comer_arroz(self,):
        self.accion()

class Chinos(Personas):
    def accion(self,):
        print("Los Chinos comen arroz con palillos")

x=Chinos()
x.comer_arroz()