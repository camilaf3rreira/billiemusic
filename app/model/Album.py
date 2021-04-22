class Album:
    def __init__ (self, tituloDoAlbum, anoDeLancamento, nomeDaBanda):
        self.tituloDoAlbum=tituloDoAlbum
        self.anoDeLancamento=anoDeLancamento
        self.nomeDaBanda=nomeDaBanda
        self.listaMusicas=[]

    def addLista(self, listaMusicas):
        self.listaMusicas=listaMusicas
        


