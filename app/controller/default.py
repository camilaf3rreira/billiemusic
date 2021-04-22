
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
            listaMusicas=[]
            maisMusica="1"

            infAlbum=menu.menuAlbum()
            album=Album(infAlbum[0],infAlbum[1],infAlbum[2])
            menu.clear()
            #listaMusicas=menu.listaMusica()

            while maisMusica=="1":
                infMusica=menu.menuMusica()
                musica=Musica(infMusica[0],infMusica[1],infMusica[2])
                listaMusicas.append(musica)
                maisMusica=menu.continuar()


            album.addLista(listaMusicas) 
            listaAlbuns.append(album)
            print("Titulo:", album.tituloDoAlbum)
            print("Ano:", album.anoDeLancamento)
            print("Nome Banda:", album.nomeDaBanda)
            for musica in listaMusicas:
                print("Titulo:", musica.tituloDaMusica)
                print("Duração:", musica.duracaoDaMusica)
                print("Favorita:", musica.favorita)




        


    





