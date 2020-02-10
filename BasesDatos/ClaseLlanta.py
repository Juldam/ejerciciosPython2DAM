class Llanta():
    def __init__(self, id, nombremarca, nombrelabrado, precio):
        self.id=id
        self.nombremarca=nombremarca
        self.nombrelabrado=nombrelabrado
        self.precio=precio

    def mostrar(self):
        print(self.id+self.nombremarca+self.nombrelabrado+self.precio)
