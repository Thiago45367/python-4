import os

os .system("cls || clear")

class Pet:

    def __init__(self, nome: str, idade: int, raca: str, porte: str, alimentacao: str) -> None:
         self.nome: str = nome
         self.idade: int = idade
         self.raca: str = raca
         self.porte: str = porte
         self.alimentacao: str = alimentacao

    def exibir_dados(self) -> str:
          return (
                 f"Nome: {self.nome}"
                 f"\nIdade: {self.idade}"
                 f"\nRaça: {self.raca}"
                 f"\nPorte: {self.porte}"
                 f"\nAlimentação: {self.alimentacao}"
                  )


pet = Pet("hercules", 2, "chow-chow", "médio", "ração")

print(pet.exibir_dados())