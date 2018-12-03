# from memoria_fisica import MemoriaFisica
# from memoria_virtual import MemoriaVirtual
# # from mmu import MMU

# # Processador de 16bits, logo endereca 2**16 = 65536 posicoes
# espaco_virtual = 2**16
# # RAM de 4 KB = 4 * 2**10 = 4096
# espaco_fisico  = 4*2**10
# tam_pag = 2**8

# mem_virt = MemoriaVirtual(espaco_virtual, tam_pag) # 4095 paginas
# mem_prin = MemoriaFisica(espaco_fisico, tam_pag) # 16 molduras
# mem_swap = MemoriaFisica(2*espaco_fisico, tam_pag) # 32 molduras

from mmu import MMU

mmu = MMU()