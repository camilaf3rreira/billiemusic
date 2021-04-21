from os import system
#from time import sleep

class Menu:

    def menuInicial (self):
        print('''>>>>>Bem vindo ao sistema Billie Music!")
        1- Cadastrar Álbum"
        2- Pesquisar Álbum
        3- Pesquisar Música
        4- Gerar Playlist
        5- Sair''')

        option=input(">>>>>Qual é a sua opção:")

        while(option not in ["1","2","3","4","5"]):
           option=input("Opção inválida, tente novamente!")

        #sleep(2)  
        return option


    def menuAlbum (self):
        infAlbum=[]
       # print(">>>>>Você selecionou a apção 1!")
        infAlbum.append(input("Digite o Título do Album:"))
        infAlbum.append(input("Digite o Ano de Lançamento:"))
        infAlbum.append(input("Digite o Nome da Banda:"))
        return infAlbum

    def menuMusica (self):
        infMusica=[]
        infMusica.append(input("Digite o Título da Música:"))
        infMusica.append(input("Digite a Duração da Música:"))
        favorita=input("Essa música é Favorita? Diga 0 para Não e 1 Sim!")

        while(favorita not in ["0","1"]):
           favorita=input("Opção inválida, tente novamente!")

        infMusica.append(favorita)
        return infMusica

    def listaMusica (self):
        listaMusicas=[]
        print("Músicas existentes no seu Album:")
        infMusica=self.menuMusica()

    
    def clear(self):
        system("cls")

