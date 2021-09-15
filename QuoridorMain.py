import pygame
from QGame.constants import WIDTH, HEIGHT, SQUARE_SIZE
from QGame.Quoridor import QuoridorGame

pygame.init()

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    quoridor = QuoridorGame()


    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            keys = pygame.key.get_pressed()

            if event.type == pygame.KEYDOWN:
                if keys[pygame.K_h]:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    quoridor.place_fence(quoridor.get_not_player_turn(), "h", (col, row))

                elif keys[pygame.K_v]:
                    pos = pygame.mouse.get_pos()
                    row, col = get_row_col_from_mouse(pos)
                    quoridor.place_fence(quoridor.get_not_player_turn(), "v", (col, row))

                elif keys[pygame.K_1]:
                    quoridor.is_winner(quoridor.is_winner('1'))

                elif keys[pygame.K_2]:
                    quoridor.is_winner(quoridor.is_winner('2'))

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                quoridor.move_pawn(quoridor.get_not_player_turn(), (col, row))

        quoridor.draw(WIN)
        pygame.display.update()

    pygame.quit()


main()