# from filosofo import Filosofo
from tabela_paginas import TabelaPaginas
# from main import *
from pagina import Pagina
import math
from memoria_fisica import MemoriaFisica
from memoria_virtual import MemoriaVirtual
# from mmu import MMU

# Processador de 16bits, logo endereca 2**16 = 65536 posicoes
espaco_virtual = 2**16
# RAM de 4 KB = 4 * 2**10 = 4096
espaco_fisico  = 4*2**10
tam_pag = 2**8

mem_virt = MemoriaVirtual(espaco_virtual, tam_pag) # 4095 paginas
mem_prin = MemoriaFisica(espaco_fisico, tam_pag) # 16 molduras
mem_swap = MemoriaFisica(2*espaco_fisico, tam_pag) # 32 molduras

class MMU():

    def __init__(self):
        self.page_table = TabelaPaginas()

    def overlay(self, obj):
        # print(type(obj))
        if str(type(obj)) == "<class 'filosofo.Filosofo'>":
            ovs = list()
            # print('ovs:',ovs)
            tam_processo = obj.F_MAX - obj.fome
            qtd_overlays = math.ceil(tam_processo / tam_pag)
            print('tam:',tam_processo,',  qtd_overlays:',qtd_overlays)
            for i in range(qtd_overlays):
                pg = Pagina(obj.id, obj.nome, i)
                ovs.append(pg)
                # print('\t',pg)
            return ovs

    def alocar_virtual(self, page, end_virt=None):
        if isinstance(page, Pagina):
            if end_virt and not mem_virt.pagina[end_virt]:
                page.end = end_virt
                mem_virt.pagina[end_virt] = True # flag so pra saber q end virtual esta em uso
                # Salvando pagina na memoria fisica - PAGINACAO
                self.paginar(page, end_virt)
                return end_virt

            for end in range(0, len(mem_virt.pagina), 10):
                if mem_virt.pagina[end] == None:
                    page.end = end
                    mem_virt.pagina[end] = True # flag so pra saber q end virtual esta em uso
                    # Salvando pagina na memoria fisica - PAGINACAO
                    self.paginar(page, end)
                    return end

    def get_virtual(self, end): # aqui é passado o end virtual
        if mem_virt.pagina[end]:
            # busca-se o end correspondente na mem fisica
            for reg in self.page_table.registros:
                if reg.end_virt == end:
                    # Primeiro na MP, caso n esteja la procura-se na swap
                    if reg.end_memp != None:
                        return mem_prin.moldura[reg.end_memp]
                    elif reg.end_swap != None:
                        return mem_swap.moldura[reg.end_swap]
                    break
        return False

    def paginar(self, page, endv):
        # Tentar salvar na MP
        end_memp = -1
        if isinstance(page, Pagina):
            for end in range(len(mem_prin.moldura)):
                if mem_prin.moldura[end] == None:
                    # page.end = end
                    end_memp = end
                    mem_prin.moldura[end] = page
                    break
        # Salvar copia na swap
        end_swap = -1
        if isinstance(page, Pagina):
            for end in range(len(mem_swap.moldura)):
                if mem_swap.moldura[end] == None:
                    # page.end = end
                    end_swap = end
                    mem_swap.moldura[end] = page
                    break
        # Armazenar relação na tabela de pagina
        self.page_table.incluir(endv, end_memp, end_swap)

    def repaginar(self, obj):
        pass
        # N sei direiro, esse metodo é so uma ideia
        # para atualizar uma pagina q foi alterada durante seu passeio no cpu
        # deve-se substituir as paginas antigas pelas novas