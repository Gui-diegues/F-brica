class Pessoa:
    def _init_(self, nome, idade, peso, altura):    
       self.nome = nome
       self.idade = idade
       self.peso = peso
       self.altura = altura

    def apresentar(self):
     print (f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos.")
    
    def calcular_imc(self):
        imc = self.peso / (self.altura ** 2)
        return imc
    
    p1 = Pessoa("pedro", 25, 70, 1.70)
    p1 = apresentar()
    print (f"meu imc e {p1.calcular_imc():.2f}")