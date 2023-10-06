class Elevador:
    # Método construtor
    def __init__(self, andar_atual, qtd_pessoas,
                 qtd_andares, capacidade):
        self.andar_atual = andar_atual
        self.qtd_pessoas = qtd_pessoas
        self.qtd_andares = qtd_andares
        self.capacidade = capacidade

    # métodos
    def subir(self):
        if self.andar_atual < self.qtd_andares:
            self.andar_atual += 1
            print("Subindo...")
            print(f"Andar atual: {self.andar_atual}")
        else:
            print("Você está no ultimo andar!")

    def descer(self):
        if self.andar_atual > 0:
            self.andar_atual -= 1
            print("Descendo...")
            print(f"Andar atual: {self.andar_atual}")
        else:
            print("Você está no Térreo!")
    def entrar(self, qtd):
        if self.qtd_pessoas + qtd <= self.capacidade:
            self.qtd_pessoas += qtd
            print("Entrando...")
            print(f"Quantidade atual: {self.qtd_pessoas}")
        else:
            print("Capacidade não suporta essa quantidade!")
    def sair(self, qtd):
        self.qtd_pessoas -= qtd
        if self.qtd_pessoas < 0:
            self.qtd_pessoas = 0
        print("Saindo...")
        print(f"Quantidade atual: {self.qtd_pessoas}")

plaza = Elevador(5, 10, 7, 15)
plaza.subir()
plaza.subir()
plaza.subir()
plaza.entrar(5)
plaza.sair(15)
plaza.sair(2)

-----------------------------------------------------

Crie uma classe chamada Cachorro que possua 3 atributos: nome, raça e peso. Implemente um método: comer ração, que retorna
"croc croc croc".

Crie duas instâncias dessa classe, e imprima na tela: "O cachorro nome_do_cachorro é da raça raça_do_cachorro, pesa peso_do_cachorro quilos e come: croc croc croc".

class Cachorro:
    def __init__(self, nome, raca, peso):
        self.nome = nome
        self.raca = raca
        self.peso = peso

    def comerRacao(self):
        return "croc croc croc"
dog = Cachorro("Pluto", "Pé duro", 10)
dog2 = Cachorro("Pitoco", "Pit bull", 20)
print(f"O cachorro, {dog.nome}, é da raça, {dog.raca} "
      f"pesa, {dog.peso} quilos e "
      f"come: {dog.comerRacao()}")

print(f"O cachorro, {dog2.nome}, é da raça, {dog2.raca} "
      f"pesa, {dog2.peso} quilos e "
      f"come: {dog2.comerRacao()}")
------------------------------------------------------------------------------------
# Classe pai
class Funcionario:
    def __init__(self, matricula, nome, salario):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario
    def exibirDados(self):
        print("--- DADOS DO FUNCIONÁRIO ---")
        print(f"Matricula: {self.matricula}")
        print(f"Nome: {self.nome}")
        print(f"Salário: {self.salario}")

class Professor(Funcionario):
    pass
class Monitor(Funcionario):
    pass
class Coordenador(Funcionario):
    pass
p1 = Professor(1, "Luiz", 3500)
p1.exibirDados()
--------------------------------------------------------------
1. Crie uma classe pai chamada Conta com os atributos
- numero da conta
- nome do cliente
- saldo
1.2 --> Crie também um método para exibir os dados da conta.
2. Crie duas classes filhas de Conta chamada ContaCorrente, ContaPoupanca

# Classe pai
class Funcionario:
    def __init__(self, matricula, nome, salario):
        self.matricula = matricula
        self.nome = nome
        self.salario = salario
    def exibirDados(self):
        print("--- DADOS DO FUNCIONÁRIO ---")
        print(f"Matricula: {self.matricula}")
        print(f"Nome: {self.nome}")
        print(f"Salário: {self.salario}")

class Professor(Funcionario):
    def __init__(self, matricula, nome, salario, turma):
        super().__init__(matricula, nome, salario)
        self.turma = turma

    def exibirDados(self):
        super().exibirDados()
        print(f"Turma: {self.turma}")

class Monitor(Funcionario):
    def __init__(self, matricula, nome, salario, carga_horaria):
        super().__init__(matricula, nome, salario)
        self.carga_horaria = carga_horaria
    def exibirDados(self):
        super().exibirDados()
        print(f'Carga horaria: {self.carga_horaria}')
class Coordenador(Funcionario):
    def __init__(self, matricula, nome, salario, area):
        super().__init__(matricula, nome, salario)
        self.area = area
    def exibirDados(self):
        super().exibirDados()
        print(f'Área: {self.area}')
p1 = Professor(1, "Luiz", 3500, "DFS519")
p1.exibirDados()

c1 = Coordenador(2, "Ana", 4500, "Exatas")
c1.exibirDados()

m1 = Monitor(3, "Julia", 1600, 300)
m1.exibirDados()
+
----------------------------------------------------------------------
1. Adicione a classe Monitor o atributo carga_horaria
1.a. Crie um método para exibir todas as informações do Monitor
2. Adicione a classe Coordenador o atributo area
2.a. Crie um método para exibir todas as informações do Coordenador

class Conta:
    def __init__(self, n_conta, cliente, saldo):
        self.n_conta = n_conta
        self.cliente = cliente
        self.saldo = saldo

    def exibirDados(self):
        print(f"Número da conta: {self.n_conta}")
        print(f"Nome: {self.cliente}")
        print(f"Saldo: {self.saldo}")
class ContaCorrente(Conta):
    pass
class ContaPoupanca(Conta):
    pass

cc = ContaCorrente(1, "Alberto", 1000)
cc.exibirDados()