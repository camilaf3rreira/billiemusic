
from ..view.Menu import Menu
from ..model.Album import Album
from ..model.Musica import Musica

class Controller:

    def start(self):
        menu=Menu() 
        option=menu.menuInicial()
        menu.clear()

        if option=="1":
            listaAlbuns=[]
            maisMusica="1"
            maisAlbum="1"
            
            while maisAlbum=="1":
                infAlbum=menu.menuAlbum()
                album=Album(infAlbum[0],infAlbum[1],infAlbum[2])
                menu.clear()

                listaMusicas=[]

                while maisMusica=="1":
                    infMusica=menu.menuMusica()
                    musica=Musica(infMusica[0],infMusica[1],infMusica[2])
                    listaMusicas.append(musica)
                    maisMusica=menu.continuar()
                
                menu.clear()
    
                album.addLista(listaMusicas)
                listaAlbuns.append(album)
                maisAlbum=menu.continuarAlbum()
                maisMusica="1"

            menu.clear()

            for album in listaAlbuns:
                print("Informações do Album:")
                print("Titulo:", album.tituloDoAlbum)
                print("Ano:", album.anoDeLancamento)
                print("Nome Banda:", album.nomeDaBanda)

                for musica in album.listaMusicas:
                    print("Informações da Música:")
                    print("Titulo:", musica.tituloDaMusica)
                    print("Duração:", musica.duracaoDaMusica)
                    print("Favorita:", musica.favorita)

        
        if option=="2":
            pass

        if option=="3":
            pass

        if option=="4":
            pass

        if option=="5":
            print(">>>>>Fim do sistema BillieMusic! Volte sempre!<<<<<<")
            exit()




        


    





