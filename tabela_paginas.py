from registro import Registro

class TabelaPaginas():

    def __init__(self):
        self.registros = list()

    def __str__(self):
        string = ''
        string = '|  End. virtual  | End. mem princ | End. mem swap  |\n'
        for r in self.registros:
            # string += '\tEndereço virtual: '+str(r.end_virt)+'\n'
            # string += '\tEndereço memória principal: '+str(r.end_memp)+'\n'
            # string += '\tEndereço memória swap: '+str(r.end_swap)+'\n'
            # string += '\n'
            string += '|     {0:6d}     |     {1:6d}     |     {2:6d}     |\n'.format(r.end_virt, r.end_memp, r.end_swap)
        return string

    def incluir(self, end, end_memp=-1, end_swap=-1):
        self.registros.append(Registro(end, end_memp, end_swap))

    def alterar_end_memp(self, virtual, memp):
        for reg in self.registros:
            if reg.end_virt == virtual:
                reg.end_memp = memp
                break

    def alterar_end_swap(self, virtual, swap):
        for reg in self.registros:
            if reg.end_virt == virtual:
                reg.end_swap = swap
                break