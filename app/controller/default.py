
from ..view.Menu import Menu
from ..model.Album import Album
from ..model.Musica import Musica

class Controller:

    def start(self):
        menu=Menu() 
        option=menu.menuInicial()
        menu.clear()

        if option=="1":
            infAlbum=menu.menuAlbum()
            album=Album(infAlbum[0],infAlbum[1],infAlbum[2])
            infoMusica=menu.menuMusica()
        


    





