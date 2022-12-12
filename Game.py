#fuerza, magia, curacion
#ataque,defensa,inteligencia,vida
#parten con 100 de vida
#decir el nickname del personaje y que tipo de clase es?
#en caso de que escoga uno se le tribuye un 20% de su clase
#al momento de crear un personaje utilizar la libreria random para que salga aleatoriamente
#el personaje que creo tiene que ser mayor a 50%
#crear dos personajes y que se ataquen el uno con el otro,para atacar se tiene que sumar todos los atributos

class Character:
    def __init__(self,nick_name,attack,defense,intelligence,life = 100):
        self.nick_name = _nick_name
        self.life = 100
        self.attack = attack
        self.defense = defense
        self.intelligence = intelligence

    def vivo(self):
        return self.life > 0

    def muerto(self):
        self
            print("Su personaje a muerto ya que tiene¨{self}")
    def 

class Strength(Character):
    def __init__(self,nick_name,attack,defense,intelligence,life,strength):
    super().__init__(nick_name,life):
    self.strength = strength

class Magic(Character):
    def __init__(self,nick_name,attack,defense,intelligence,life,magic):
    super().__init__(nick_name,life):
    self.magic = magic

class Healing(Character):
    def __init__(self,nick_name,attack,defense,intelligence,life,healing):
    super().__init__(nick_name,life)
    self.healing = healing
