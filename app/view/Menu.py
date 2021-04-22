from os import system

class Menu:

    def menuInicial (self):
        print('''>>>>>Bem vindo ao sistema BillieMusic!<<<<<
        1- Cadastrar Álbum"
        2- Pesquisar Álbum
        3- Pesquisar Música
        4- Gerar Playlist
        5- Sair''')

        option=input("Digite o número referente a opção escolhida:")

        while(option not in ["1","2","3","4","5"]):
           option=input("Você digitou uma opção inválida, tente novamente!")

        return option


    def menuAlbum (self):
        infAlbum=[]
        print(">>>>>Para cadastrar um Álbum<<<<<")
        infAlbum.append(input("Digite o Título:"))
        infAlbum.append(input("Digite o Ano de Lançamento:"))
        infAlbum.append(input("Digite o Nome da Banda:"))
        return infAlbum

    def menuMusica (self):
        infMusica=[]
        print(">>>>>Para cadastrar uma Música<<<<<")
        infMusica.append(input("Digite o Título:"))
        infMusica.append(input("Digite a Duração:"))
        favorita=input("Essa música é Favorita? Digite 0 para Não e 1 Sim!")

        while(favorita not in ["0","1"]):
           favorita=input("Você digitou uma opção inválida, tente novamente!")

        infMusica.append(favorita)
        return infMusica

    def continuar (self):
        maisMusica=input("Você deseja adicionar mais uma <<MÚSICA>>? Diga 0 para Não e 1 Sim!")
        while(maisMusica not in ["0","1"]):
                maisMusica=input("Você digitou uma opção inválida, tente novamente!")
        return maisMusica           

    def continuarAlbum(self):
        maisAlbum=input("Você deseja adicionar mais um <<ÁLBUM>>? Diga 0 para Não e 1 Sim!")
        while(maisAlbum not in ["0","1"]):
                maisAlbum=input("Você digitou uma opção inválida, tente novamente!")
        return maisAlbum

    def clear(self):
        system("cls")

