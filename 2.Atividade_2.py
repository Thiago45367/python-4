import os

os .system("cls || clear")

class Bancaria:

     def __init__(self, banco: str, agencia: str, numeroDaConta: str, tipoDaConta: str, saldoAtual: float, limiteDisponivel: float) -> None:
           self.banco: str = banco
           self.agencia: str = agencia
           self.numeroDaConta: str = numeroDaConta
           self.tipoDaConta: str = tipoDaConta
           self.limiteDisponivel: str = limiteDisponivel

     def exibir_dados(self) -> str:
          return (
                 f"Banco: {self.banco}"
                 f"\nAgencia: {self.agencia}"
                 f"\nNumero da conta: {self.numeroDaConta}"
                 f"\nTipo da conta: {self.tipoDaConta}"
                 f"\nLimite Disponiveis: {self.limiteDisponivel}"
                  )
     
Bancario = Bancaria(".....", "....", ".....", "......", 086.9, 45.9)

print(Bancaria.exibir_dados())