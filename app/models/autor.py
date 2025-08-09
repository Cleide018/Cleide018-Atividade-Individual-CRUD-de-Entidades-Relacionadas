class AutorModel:
    def __init__(self, id, nome, nacionalidade):
        self.__id = id
        self.__nome = nome
        self.__nacionalidade = nacionalidade

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_nacionalidade(self):
        return self.__nacionalidade

    def set_nacionalidade(self, nacionalidade):
        self.__nacionalidade = nacionalidade
