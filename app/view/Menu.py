from os import system


class Menu:
    def __init__(self, tipo):
        self.tipo=tipo

    def menuInicial (self):
        print("Bem vindo ao sistema Billie Music! Selecione a opção a seguir:")
        print("1- Cadastrar Álbum")
        print("2- Pesquisar Álbum")
        print("3- Pesquisar Música")
        print("4- Gerar Playlist")
        print("5- Sair")
        
        option=input()

        while(option not in ["1","2","3","4","5"]):
           option=input("Opção inválida, tente novamente!")
           
        return option

    def clear(self):
        system("cls")