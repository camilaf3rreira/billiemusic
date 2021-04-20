#from ..view.Menu import Menu

from ..view.Menu import Menu
from ..model.Album import Album
from ..model.Musica import Musica

def start():
   menu=Menu() 
   option=menu.menuInicial()
   menu.clear()

   if option=="1":
       infAlbum=menu.menuAlbum()
       album=Album(infAlbum[0],infAlbum[1],infAlbum[2])
       infoMusica=menu.menuMusica()
       


    





