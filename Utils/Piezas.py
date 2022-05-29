class GameState():
    def __init__ (self):
        self.board=[
            ['Nt','Nc','Na','Nr','Nk','Na','Nc','Nt'],
            ['Np','Np','Np','Np','Np','Np','Np','Np'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['--','--','--','--','--','--','--','--'],
            ['Bp','Bp','Bp','Bp','Bp','Bp','Bp','Bp'],
            ['Bt','Bc','Ba','Br','Bk','Ba','Bc','Bt']
        ]
        self.movimiento=True
        self.movpieza=[]