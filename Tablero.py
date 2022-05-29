from json import load
import pygame as pgame
import Utils.Piezas as p

Ancho = 512
Largo = Ancho
Dimension = 8
Tab_size = Largo // Dimension
FPS = 15
Images = {}

def cargaPiezas():
    piezas = ['Ba', 'Bc', 'Bk', 'Bp', 'Br', 'Bt', 'Na', 'Nc', 'Nk', 'Np', 'Nr', 'Nt']
    for pieza in piezas:
        Images[pieza] = pgame.transform.scale(pgame.image.load('Images/' + pieza + '.png'), (Tab_size, Tab_size))


def main():
    pgame.init()
    screen = pgame.display.set_mode((Ancho, Largo))
    Reloj = pgame.time.Clock()
    screen.fill(pgame.Color('white'))
    gs = p.GameState()
    print(gs.board)
    cargaPiezas()
    ejecutar = True
    while ejecutar:
        for e in pgame.event.get():
            if e.type == pgame.QUIT:
                ejecutar = False
        dibujarEstado(screen, gs)
        Reloj.tick(FPS)
        pgame.display.flip()


def dibujarEstado(screen, gs):
    dibujarTablero(screen)
    dibujarPiezas(screen, gs.board)


def dibujarTablero(screen):
     colores = [pgame.Color('white'), pgame.Color(188, 170, 164)]
     for r in range(Dimension):
         for c in range(Dimension):
             color = colores[((r+c) % 2)]
             pgame.draw.rect(screen, color, pgame.Rect(c*Tab_size, r*Tab_size, Tab_size, Tab_size))

def dibujarPiezas(screen, board):
     for r in range(Dimension):
         for c in range(Dimension):
             pieza = board[r][c]
             if pieza != '--':
                 screen.blit(Images[pieza], pgame.Rect(c*Tab_size, r*Tab_size, Tab_size, Tab_size))

if __name__ == "__main__":
    main()



