import pygame
from QGame.constants import WIDTH, HEIGHT, SQUARE_SIZE
from QGame.Quoridor import QuoridorGame

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Quoridor")

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

                elif keys[pygame.K_w]:
                    if quoridor.is_winner(quoridor.get_not_player_turn()) is True:
                        pygame.quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                # piece = quoridor.get_piece(row, col)
                quoridor.move_pawn(quoridor.get_not_player_turn(), (col, row))
                # quoridor.move_pawn("2", (col, row))

            #if event.type == pygame.KEYDOWN and :

                #quoridor.print_board()
                #print(row, col)
                #print(piece)
                # piece = quoridor.get_piece(row, col)
                # CHECK SELECT METHOD  ON TIM VIDEO AT 48:26
                # quoridor.move_pawn(piece, (5,0))
                # quoridor.move_pawn(piece, (4, 7))

        quoridor.draw(WIN)
        #quoridor.create_board(WIN)
        pygame.display.update()

    pygame.quit()


main()


# C:\Users\quanj\PycharmProjects\portfolio-project-dpatters550\QuoridorMain.py

# width = 513
#
# height = 513
#
# dimension = 9
#
# sq_size = height//dimension
#
# max_fps = 15
#
# images = {}

# project_dir = os.path.dirname(os.path.abspath(__file__))
# image_path = os.path.join(project_dir, "images")
# # image_path = os.path.join(project_dir, "images", piece + ".png")

# def loadimages():
#     pieces = ["1", "2", "v", "h", "f"]
#     for piece in pieces:
#
#         #hello = os.getcwd()
#         #print(hello)
#         #print(image_path)
#         bird = p.image.load(os.path.join(image_path, "1.png"))
#         #images[piece] = p.transform.scale(p.image.load(image_path), (sq_size, sq_size))
#         #images[piece] = p.image.load("images/" + piece + ".png")
#         # images[piece] = p.transform.scale(p.image.load("PycharmProjects/portfolio-project-dpatters550/images/" + piece + ".png"), (sq_size, sq_size))

# def main():
#     p.init()
#     screen = p.display.set_mode((width, height))
#     clock = p.time.Clock()
#     screen.fill(p.Color("brown"))
#     gs = Quoridor.QuoridorGame()
#     running = True
#     while running:
#         for e in p.event.get():
#             if e.type == p.QUIT:
#                 running = False
#             drawgamestate(screen, gs)
#             clock.tick(max_fps)
#             p.display.flip()
#
# def drawgamestate(screen, gs):
#     draw_board(screen)
#
#     draw_pieces(screen, gs.get_board())
#
# def draw_board(screen):
#     colors = [p.Color("black"), p.Color("black")]
#     for r in range(dimension):
#         for c in range(dimension):
#             color = colors[((r+c) % 2)]
#             p.draw.rect(screen, color, p.Rect(c*sq_size, r*sq_size, sq_size, sq_size), 5)
#
#
# def draw_pieces(screen, board):
#     for r in range(dimension):
#         for c in range(dimension):
#             piece = board[r][c]
#             if "1" in piece:
#                 p.draw.circle(screen, (255, 255, 0), (c*sq_size, r*sq_size), (sq_size//2 - dimension))
#             elif "2" in piece:
#                 p.draw.circle(screen, (255, 100, 5), (c * sq_size, r * sq_size), (sq_size // 2 - dimension))
#             elif "v" in piece:
#                 p.draw.line(screen, (255,255,0), (c*sq_size, c*sq_size), (c*sq_size, sq_size), 5)
#
#
#
# # if __name__ == " __main__ ":
# main()