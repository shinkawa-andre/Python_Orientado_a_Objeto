
# INÍCIO DA CLASS FUNCIONARIO
class Funcionario:
    def __init__(self, nome, salario, cargo, imposto, beneficio):
        self.nome = nome
        self.salario = salario
        self.beneficio = beneficio
        self.imposto = imposto
        self.lista_cargos = ["Analista","Diretor"]
        if cargo in self.lista_cargos:
            self.cargo = cargo
        else:
            raise Exception("Cargo inválido")



#MÉTODO

    def calcular_salario(self):

        if self.cargo == "Analista":
            valor = (self.salario * (self.imposto / 100))
            valor_salario = ((self.salario - valor) + self.beneficio)
            print(f"Seu salário como ANALISTA é: R${valor_salario}")
        elif self.cargo == "Diretor":
            valor = (self.salario * (self.imposto / 100))
            valor_salario = ((self.salario - valor) + self.beneficio)
            print(f"Seu salário como DIRETOR é: R${valor_salario}")


#INSTANCIANDO

funcionario_a = Funcionario("André", 2000, "Analista", 15, 1360)
funcionario_a.calcular_salario()

funcionario_d = Funcionario("André Shinkawa", 5500, "Diretor", 25, 2450)
funcionario_d.calcular_salario()