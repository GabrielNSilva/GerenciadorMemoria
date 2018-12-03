import math

class MemoriaFisica():
    def __init__(self, tamanho, tam_molduras):
        self.tamanho = tamanho
        # self.tam_molduras = tamanho / molduras
        self.tam_molduras = tam_molduras
        # self.qtd_molduras = molduras
        self.qtd_molduras = math.floor(tamanho / tam_molduras)
        self.moldura = self.gerar_molduras()
    
    def gerar_molduras(self):
        mold = list()
        for i in range(self.qtd_molduras):
            mold.append(None)
        return mold

    def alterar_tam_molduras(self, tam_molduras):
        self.tam_molduras = tam_molduras
        self.qtd_molduras = math.floor(self.tamanho / tam_molduras)

    def alterar_qtd_molduras(self, qtd_molduras):
        self.qtd_molduras = qtd_molduras
        self.tam_molduras = self.tamanho / qtd_molduras