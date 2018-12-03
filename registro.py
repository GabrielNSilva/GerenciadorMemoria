class Registro():

    def __init__(self, end, end_memp=-1, end_swap=-1):
        self.end_virt = end
        self.end_memp = end_memp
        self.end_swap = end_swap