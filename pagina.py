class Pagina():

    def __init__(self, pid, pname, part, end=None, prox=None):
        self.pid = pid
        self.pname = pname
        self.part = part
        self.end = end
        self.prox = prox

    def __str__(self):
        string = 'Pagina - BCP pid:'+str(self.pid)+' part:'+str(self.part)+' pname:'+self.pname
        if self.end != None:
            string += ' end:'+str(self.end)
        return string