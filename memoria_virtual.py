import math

class MemoriaVirtual():
    def __init__(self, tamanho, tam_paginas):
        self.tamanho = tamanho
        # self.tam_paginas = tamanho / paginas
        self.tam_paginas = tam_paginas
        # self.qtd_paginas = paginas
        self.qtd_paginas = math.floor(tamanho / tam_paginas)
        self.pagina = self.gerar_paginas()
    
    def gerar_paginas(self):
        page = list()
        for i in range(self.qtd_paginas):
            page.append(None)
        return page

    def alterar_tam_paginas(self, tam_paginas):
        self.tam_paginas = tam_paginas
        self.qtd_paginas = math.floor(self.tamanho / tam_paginas)

    def alterar_qtd_paginas(self, qtd_paginas):
        self.qtd_paginas = qtd_paginas
        self.tam_paginas = self.tamanho / qtd_paginas