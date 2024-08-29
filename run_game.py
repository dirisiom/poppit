import pygame as pg
from src.elements.board import Board

def main():
    pg.init()
    # make the window size unable to change

    screen = pg.display.set_mode((960, 800))
    pg.display.set_caption("Poppit")

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill((50, 50, 50))

    board = Board()

    screen.blit(background, (0, 0))
    pg.display.flip()

    going = True
    while going:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False

        screen.blit(background, (0, 0))
        board.draw(screen)
        pg.display.flip()

    pg.quit()


if __name__ == '__main__':
    main()
