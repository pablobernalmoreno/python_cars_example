import os

os.system('cls')
print('\n \n')


class Carro:

    def __init__(self,llantas,color,gente,vel):

        self.llantas = llantas
        self.color = color
        self.gente = gente
        self.vel = vel

    def __str__(self):
        return f'{type(object).__name__} \nLlantas: {self.llantas}\nColor: {self.color}\nPasajeros: {self.gente}\nVelocidad: {self.vel}km/h\n'


class Deportivo(Carro):

    def __init__(self,llantas,color,gente,vel,turbo):
        super().__init__(llantas,color,gente,vel)
        self.turbo = turbo
    
    def __str__(self):
        return super().__str__() + f'\nTurbo: {self.turbo} disponible\n'

class Moto(Carro):
    def __init__(self,llantas,color,gente,vel,casco,):
        super().__init__(llantas,color,gente,vel)
        self.casco = casco

    def __str__(self):

        if self.llantas > 2:
            return f'{type(object).__name__}\n' + ('No se puede crear la moto con mas de 2 ruedas\n')
        else:
            return super().__str__() + f'\nCasco: {self.casco} disponible\n'

class Bus(Carro):
    def __init__(self,llantas,color,gente,vel,bath):
        super().__init__(llantas,color,gente,vel)
        self.bath = bath

    def __str__(self):

         return super().__str__() + f'\nNum baños: {self.bath}\n'

class Nave(Carro):
    def __init__(self,llantas,color,gente,vel,propulsores):
        super().__init__(llantas,color,gente,vel)
        self.propulsores = propulsores

    def __str__(self):

         return super().__str__() + f'\nNum de propulsores: {self.propulsores}\n'


podrido = Carro(4,'verde',5,85)
print(podrido)

beso_negro = Moto(3,'negro',2,100,'Acrilico')
print(beso_negro)

mini = Deportivo(4,'girs','4',200,'Nitro')
print(mini)

buseta = Bus(6,'blanco',35,70,2)


halcon = Nave(7,'girs',6,1050,'de luz')
print(halcon.__dict__)

print(podrido)
print(beso_negro)
