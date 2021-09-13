# Author: Daquan Patterson
# Date 8/11/2021
# Description: This program allows for a 2 player version of a board game called Quoridor to be played. It allows
# for players to move turn by turn or place fences turn by turn. If one player is able to reach the opposite end of
# their start end, then the game is won.

import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, GREY, COLS, WHITE, VERTICAL, HORIZONTAL, BROWN, BROWN2

class QuoridorGame:

    """ This class is a blue print for the game called Quoridor and creates the necessary conditions for the game to
    be played."""

    def __init__(self, p1="1", p2="2"): #
        """ This init method creates a game board which is made up of lists. It has two parameters with default values
        set to 1 and 2. The board has the letter f in each of it's four corners so that no It also contains the the data members of player 1 fences and player 2 fences that tracks the
        amount of fences left for each respective player. The data member not player turn tracks the turn of the person
        not allowed to play. Lastly, the game won data member tracks the gamestate and whether one of the player has
        won.
        """

        self._board = [
                    [ ["f"], [], [], [], [p1], [], [], [], ["f"]],
                    [ [], [], [], [], [], [], [], [], []],
                    [ [], [], [], [], [], [], [], [], []],
                    [ [], [], [], [], [], [], [], [], []],
                    [ [], [], [], [], [], [], [], [], []],
                    [ [], [], [], [], [], [], [], [], []],
                    [ [], [], [], [], [], [], [], [], []],
                    [ [], [], [], [], [], [], [], [], []],
                    [ ["f"], [], [], [], [p2], [], [], [], ["f"]]
                       ]

        self._not_player_turn = "2" #

        self._game_won = False

        self._player_1_fence_count = 10

        self._player_2_fence_count = 10

        self._selected = None

    # def select(self, player, coordinates): # parameters will need to be fixed 10:04 in tim's video
    #     if self._selected:
    #         result = self.move_pawn(player, coordinates) # parameters will need to be fixed
    #         if not result:
    #             self._selected = None
    #             self.select(player, coordinates)
    #
    #     piece = self.get_piece([coordinates[1]],[coordinates[0]])
    #     if piece != [] and self._not_player_turn != player:
    #         self._selected = piece
            # self.valid_moves = self._board.get_valid_pieces(piece)

    def select(self, player, coordinates):
        return self.move_pawn(player, coordinates)
        #if self.move_pawn is True:


    def draw_squares(self, win):
        win.fill(BROWN)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(win, BROWN2, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 5)

    # def highlight(self, win):
    #     self.draw_squares(win)
    #     radius = SQUARE_SIZE // 2 - 15
    #     for row in range(ROWS):
    #         for col in range(COLS):
    #             piece = self._board[row][col]
    #             if self.move_pawn() is True:
    #                 # draw blue dot
    #                 pass

    def draw(self, win):
        self.draw_squares(win)
        radius = SQUARE_SIZE // 2 - 15
        for row in range(ROWS):
            for col in range(COLS):
                piece = self._board[row][col]
                if "1" in piece:
                    pygame.draw.circle(win, WHITE, (col*SQUARE_SIZE + SQUARE_SIZE // 2, row*SQUARE_SIZE + SQUARE_SIZE // 2), radius + 2)
                    pygame.draw.circle(win, WHITE, (col*SQUARE_SIZE + SQUARE_SIZE // 2, row*SQUARE_SIZE + SQUARE_SIZE // 2), radius)
                #
                if "2" in piece:
                    pygame.draw.circle(win, GREY, (col*SQUARE_SIZE + SQUARE_SIZE // 2, row*SQUARE_SIZE + SQUARE_SIZE // 2), radius + 2)
                    pygame.draw.circle(win, GREY, (col*SQUARE_SIZE + SQUARE_SIZE // 2, row*SQUARE_SIZE + SQUARE_SIZE // 2), radius)

                if "h" in piece:
                    win.blit(HORIZONTAL, (col * SQUARE_SIZE, row * SQUARE_SIZE))

                if "v" in piece:
                    win.blit(VERTICAL,(col * SQUARE_SIZE, row * SQUARE_SIZE))

    def get_piece(self, row, col):
        if "1" in self._board[row][col]:
            return "1"
        elif "2" in self._board[row][col]:
            return "2"

    def get_not_player_turn(self):
        if self._not_player_turn == "1":
            return "2"
        elif self._not_player_turn == "2":
            return "1"

    # def calc_position(self):
    #     self._x = SQUARE_SIZE *

    def print_board(self):
        """ This method prints the board."""
        for i in range(len(self._board)):
            print(self._board[i])

    def double_vert_jump(self, coordinates, i, count, player, op_player=None):
        """ This method allows for the player to jump over the opposite player as long as the necessary conditions are
        met. It is called by the move pawn method as long as the necessary coordinates are put in."""

        if player == "1": #
            op_player = "2" #

            if coordinates == (i, count + 2) and op_player in self._board[count + 1][i] and "h" not in \
                    self._board[count + 2][i] and "h" not in self._board[count + 1][i]:

                self._not_player_turn = player

                self._board[coordinates[1]][coordinates[0]].append(player)

                return True

            else:
                self._board[count][i].append(player)
                return False

        elif player == "2": #
            op_player = "1" #

            if coordinates == (i, count - 2) and op_player in self._board[count - 1][i] and "h" not in \
                    self._board[count - 1][i] and "h" not in self._board[count][i]:

                self._not_player_turn = player

                self._board[coordinates[1]][coordinates[0]].append(player)

                return True

            else:
                self._board[count][i].append(player)
                return False

    def vertical_move(self, coordinates, i, count, player, op_player=None):
        """ This method allows for vertical movements. The player can only move forward or backwards by one place
        at a time. This method is called by the move pawn method.
        """

        if player == "1": #
            op_player = "2" #

        elif player == "2": #
            op_player = "1" #

        if coordinates == (i, count + 1) and op_player not in self._board[coordinates[1]][coordinates[0]] and \
                "h" not in self._board[coordinates[1]][coordinates[0]]:

            self._not_player_turn = player

            self._board[coordinates[1]][coordinates[0]].append(player)

            return True

        elif coordinates == (i, count - 1) and op_player not in self._board[coordinates[1]][coordinates[0]] and \
                "h" not in self._board[count][i]:

            self._not_player_turn = player

            self._board[coordinates[1]][coordinates[0]].append(player)

            return True

        elif coordinates == (i, count + 1) and op_player in self._board[coordinates[1]][coordinates[0]]:
            self._board[count][i].append(player)

            return False

        elif coordinates == (i, count - 1) and op_player in self._board[coordinates[1]][coordinates[0]]:
            self._board[count][i].append(player)

            return False

        elif coordinates == (i, count + 1) and "h" in self._board[coordinates[1]][coordinates[0]]:
            self._board[count][i].append(player)

            return False

        elif coordinates == (i, count - 1) and "h" in self._board[count][i]:
            self._board[count][i].append(player)

            return False

        elif coordinates == (i, count + 2) or coordinates == (i, count - 2):
            return self.double_vert_jump(coordinates, i, count, player)

    def horizontal_move(self, coordinates, i, count, player, op_player=None):

        """ This method allows for vertical movements. The player can only move left or right by one place
                at a time. This method is called by the move pawn method.
                """

        if player == "1": #
            op_player = "2" #

        elif player == "2": #
            op_player = "1" #

        if coordinates == (i + 1, count) and op_player not in self._board[coordinates[1]][coordinates[0]] and \
                "v" not in self._board[coordinates[1]][coordinates[0]]:

            self._not_player_turn = player

            self._board[coordinates[1]][coordinates[0]].append(player)

            return True

        elif coordinates == (i - 1, count) and op_player not in self._board[coordinates[1]][coordinates[0]]\
                and "v" not in self._board[count][i]:

            self._not_player_turn = player

            self._board[coordinates[1]][coordinates[0]].append(player)

            return True

        elif coordinates == (i - 1, count) and op_player in self._board[coordinates[1]][coordinates[0]]:
            self._board[count][i].append(player)

            return False

        elif coordinates == (i + 1, count) and op_player in self._board[coordinates[1]][coordinates[0]]:
            self._board[count][i].append(player)

            return False

        elif coordinates == (i + 1, count) and "v" in self._board[coordinates[1]][coordinates[0]]:
            self._board[count][i].append(player)

            return False

        elif coordinates == (i - 1, count) and "v" in self._board[count][i]:
            self._board[count][i].append(player)

            return False

    def diagonal_move(self, coordinates, i, count, player, op_player=None):
        """" This method communicates with the move_pawn method to allow for diagonal movements.The coordinates accepted
         in the method will allow for the player to diagonally as long as the necessary conditions are met.
        """

        if player == "1": #
            op_player = "2" #

            if coordinates == (i - 1, count + 1) and op_player in self._board[count + 1][i] \
                    and "h" in self._board[count + 2][i] and "h" not in self._board[coordinates[1]][coordinates[0]]:

                self._not_player_turn = player

                self._board[coordinates[1]][coordinates[0]].append(player)
                return True

            elif coordinates == (i + 1, count + 1) and op_player in self._board[count + 1][i] \
                    and "h" in self._board[count + 2][i] and "h" not in self._board[coordinates[1]][coordinates[0]]:

                self._not_player_turn = player

                self._board[coordinates[1]][coordinates[0]].append(player)
                return True

            else:
                self._board[count][i].append(player)
                return False

        elif player == "2": #
            op_player = "1" #

            if coordinates == (i - 1, count - 1) and op_player in self._board[count - 1][i] \
                    and "h" in self._board[count - 1][i] and "h" not in self._board[count][i - 1]:

                self._not_player_turn = player

                self._board[coordinates[1]][coordinates[0]].append(player)
                return True

            elif coordinates == (i + 1, count - 1) and op_player in self._board[count - 1][i] \
                    and "h" in self._board[count - 1][i] and "h" not in self._board[count][i + 1]:

                self._not_player_turn = player

                self._board[coordinates[1]][coordinates[0]].append(player)
                return True

            else:
                self._board[count][i].append(player)
                return False

    def move_pawn(self, player, coordinates):
        """ This method takes in two different parameters that allows for the movement of a player piece. The player
        pieces are represented by the integers 1 and 2. The coordinate parameter allows for exact movement as long as
        the movement is allowable. The method will keep checking for a player's current location via a for and a
        while loop and once found, it will allow for restrictive movements till a winner is declared.
        """

        row = 0
        count = 0
        if player == self._not_player_turn or self._game_won is True:

            return False

        else:

            if player == "1" or player == "2": #

                while count != 9:

                    for i, c in enumerate(self._board[row]):

                        if player in c:

                            self._board[count][i].remove(player)

                            if 9 in coordinates or -1 in coordinates:

                                self._board[count][i].append(player)

                                return False

                            elif coordinates == (i, count + 1) or \
                                    coordinates == (i, count - 1) or coordinates == (i, count + 2) \
                                    or coordinates == (i, count - 2):

                                return self.vertical_move(coordinates, i, count, player)

                            elif coordinates == (i + 1, count) or \
                                    coordinates == (i - 1, count):

                                return self.horizontal_move(coordinates, i, count, player)

                            elif coordinates == (i - 1, count + 1) or coordinates == (i + 1, count + 1) or \
                                    coordinates == (i - 1, count - 1) or coordinates == (i + 1, count - 1):
                                return self.diagonal_move(coordinates, i, count, player)

                            else:
                                self._board[count][i].append(player)
                                return False

                        if i == 8:
                            row += 1
                            count += 1

    def fair_play_check(self, p):
        pass

    def place_fence(self, player, position, coordinates):

        """ This method allows for the player to place a fence on the board. It takes in three parameters and the places
        the position letter in the specified list/location. If a list of the same position exists within the specified
        location already then the method will return false"""

        if player == self._not_player_turn or self._game_won is True:

            return False

        else:

            if player == "1": #

                if self._player_1_fence_count == 0 or coordinates[1] < 0 or coordinates[1] >= 9 or \
                        coordinates[0] < 0 or coordinates[0] >= 9:

                    return False

                elif position not in self._board[coordinates[1]][coordinates[0]] and "f" not in \
                        self._board[coordinates[1]][coordinates[0]]:

                    self._player_1_fence_count -= 1

                    self._not_player_turn = player

                    self._board[coordinates[1]][coordinates[0]].append(position)

                    return True

                elif position in self._board[coordinates[1]][coordinates[0]] or "f" in \
                        self._board[coordinates[1]][coordinates[0]]:

                    return False

            elif player == "2": #

                if self._player_2_fence_count == 0 or coordinates[1] < 0 or coordinates[1] >= 9 or \
                        coordinates[0] < 0 or coordinates[0] >= 9:

                    return False

                elif position not in self._board[coordinates[1]][coordinates[0]] and "f" not in \
                        self._board[coordinates[1]][coordinates[0]]:

                    self._player_2_fence_count -= 1

                    self._not_player_turn = player

                    self._board[coordinates[1]][coordinates[0]].append(position)

                    return True

                elif position in self._board[coordinates[1]][coordinates[0]] or "f" in \
                        self._board[coordinates[1]][coordinates[0]]:

                    return False

    def is_winner(self, player):

        """ This method checks for a winner via the input of the player argument. If said player is in the correct \
        position necessary for a win then the method will return true. It will also change the game won data member
        which will end the game."""

        if player == "1": #

            for pos in self._board[8]:

                if player in pos:

                    self._game_won = True

                    return True

            return False

        elif player == "2": #

            for pos in self._board[0]:

                if player in pos:

                    self._game_won = True

                    return True

            return False

# e = Entry(root, width=35, borderwidth=5)
#
# e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
#
# #e.insert(0, "what is your coordinates: ")
#
#
# mybutton = Button(root, command=myClick)
#
# for i in mybutton:
#     i.grid()