# Author: Daquan Patterson
# Date 8/6/2021
# Description:

class QuoridorGame:

    """ This class is a blue print for the game called Quoridor and creates the necessary conditions for the game to
    be played."""

    def __init__(self, p1=1, p2=2):
        """ This init method creates a game board which is made up of lists. It has two parameters with default values
        set to 1 and 2. It also contains the the data members of player 1 fences and player 2 fences that tracks the
        amount of fences left for each respective player. This of course will be our first step as all other steps will
        be based on the board."""

        """DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS"""

        """The board is initialized as a 2D array and the board is also initialized with the parameters of p1 and p2 
            in their respective lists that reflects their starting positions in the board game. Also, the total count of
             fences will be tracked by the player_1_fence and player_2_fence data members.Those two data members will 
             decrease when the corresponding player places a fence. """
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

        self._not_player_turn = 2

        self._game_won = False

        self._player_1_fence_count = 10

        self._player_2_fence_count = 10

    def get_board(self):
        """ This method returns the board. It is mainly used for visually testing movements and may or may not be
        removed in the final version."""
        return self._board

    def double_vert_jump(self, coordinates, i, count, player, op_player=None): # Line_count = 18

        if player == 1:
            op_player = 2

            if coordinates == (i, count + 2) and op_player in self._board[count + 1][i] and "h" not in \
                    self._board[count + 2][i]:

                self._not_player_turn = player

                self._board[coordinates[1]][coordinates[0]].append(player)

                return True

            else:
                self._board[count][i].append(player)
                return False

        elif player == 2:
            op_player = 1

            if coordinates == (i, count - 2) and op_player in self._board[count - 1][i] and "h" not in \
                    self._board[count - 2][i]:

                self._not_player_turn = player

                self._board[coordinates[1]][coordinates[0]].append(player)

                return True

            else:
                self._board[count][i].append(player)
                return False

    def vertical_move(self, coordinates, i, count, player, op_player=None): # Line_count = 22

        if player == 1:
            op_player = 2

        elif player == 2:
            op_player = 1

        if coordinates == (i, count + 1) and op_player not in self._board[coordinates[1]][coordinates[0]] and \
                "h" not in self._board[coordinates[1]][coordinates[0]]:

            self._not_player_turn = player

            self._board[coordinates[1]][coordinates[0]].append(player)

            return True

        elif coordinates == (i, count - 1) and op_player not in self._board[coordinates[1]][coordinates[0]] and \
                "h" not in self._board[coordinates[1]][coordinates[0]]:

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

        elif coordinates == (i, count - 1) and "h" in self._board[coordinates[1]][coordinates[0]]:
            self._board[count][i].append(player)

            return False

        elif coordinates == (i, count + 2) or coordinates == (i, count - 2):
            return self.double_vert_jump(coordinates, i, count, player)

    def horizontal_move(self, coordinates, i, count, player, op_player=None): # Line_count = 21

        if player == 1:
            op_player = 2

        elif player == 2:
            op_player = 1

        if coordinates == (i + 1, count) and op_player not in self._board[coordinates[1]][coordinates[0]] and \
                "v" not in self._board[coordinates[1]][coordinates[0]]:

            self._not_player_turn = player

            self._board[coordinates[1]][coordinates[0]].append(player)

            return True

        elif coordinates == (i - 1, count) and op_player not in self._board[coordinates[1]][coordinates[0]]\
                and "v" not in self._board[coordinates[1]][coordinates[0]]:

            self._not_player_turn = player

            self._board[coordinates[1]][coordinates[0]].append(player)

            return True

        elif coordinates == (i - 1, count) and op_player in self._board[coordinates[1]][coordinates[0]]:
            self._board[count][i].append(player)

            return False

        elif coordinates == (i + 1, count) and "v" in self._board[coordinates[1]][coordinates[0]]:
            self._board[count][i].append(player)

            return False

        elif coordinates == (i - 1, count) and "v" in self._board[coordinates[1]][coordinates[0]]:
            self._board[count][i].append(player)

            return False

    def diagonal_move(self, coordinates, i, count, player, op_player=None): # Line_count = 26
        """" This potential method will communicate with the move_pawn method to allow for diagonal movements.
        This method exist because of the 20-25 line restriction. The coordinates accepted in the method will be
        for diagonal movements while the move pawn method allows for horizontal and vertical movements. This an
        alternate step in which it will account for a potential situation that may arise.
        """

        """DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS"""

        """" This method should only be called once we one other two players encounter a situation in which a wall """
        # still need to add a way for the program to tell if a wall is blocking the diag move
        if player == 1:
            op_player = 2

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

        elif player == 2:
            op_player = 1

            if coordinates == (i - 1, count - 1) and op_player in self._board[count - 1][i] \
                    and "h" in self._board[count - 2][i] and "h" not in self._board[coordinates[1]][coordinates[0]]:

                self._not_player_turn = player

                self._board[coordinates[1]][coordinates[0]].append(player)
                return True

            elif coordinates == (i + 1, count - 1) and op_player in self._board[count - 1][i] \
                    and "h" in self._board[count - 2][i] and "h" not in self._board[coordinates[1]][coordinates[0]]:

                self._not_player_turn = player

                self._board[coordinates[1]][coordinates[0]].append(player)
                return True

            else:
                self._board[count][i].append(player)
                return False

    def move_pawn(self, player, coordinates): # Line_count = 25
        """ This method takes in two different parameters that allows for the movement of a player piece. The player
        pieces are represented by the integers 1 and 2. The coordinate parameter allows for exact movement as long as
        the movement is allowable. This is technically a second step. We need to have the players move about the boards.
         The method will keep checking via a for and while loop and allow for restrictive movements till a winner is
         declared."""

        """DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS"""

        """This method is reliant on an honor system, so the current player
            has to be respectful to the opposite player's turn. The method uses a for loop that loops through the board
             and find the exact position of the player's piece. It loops through each list with the aide of 
             variables var1 and count. It will then only allow for horizontal and vertical 
             movements by restrictive if statements and will return false if they are violated. """

        row = 0
        count = 0
        if player == self._not_player_turn or self._game_won is True:

            return False

        else:

            if player == 1 or player == 2:

                while count != 9:

                    for i, c in enumerate(self._board[row]):

                        if player in c:

                            # print(count, i) # index is a bit different from coordinates but they still act the same
                            # print(i, count + 1) # vertical

                            self._board[count][i] = []

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

    def place_fence(self, player, position, coordinates): # Line_count = 25

        """ This method allows for the player to place a fence on the board. It takes in three parameters and the places
        the position letter in the specified list. This is connected with the second step as the player can switch
        between moving or not."""

        """DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS"""

        """Placement of fences are dependent on if the desired list is empty of any fences. If a fence with a specific 
        position already exist inside of a the desired list, then further placements of that same position is not 
        allowed. Additionally, if said list has a position in it, then the opposing player will
        not be able to move to that list via that position. So /"h/" is for horizontal 
        and /"v/" is for vertical. In other words, fences on the board are tracked by a letter inside of a list.
        This method still needs to account for out of bounds placement. 
        Like the method above this method reliant on an honor system and so the players will use it depending on their
         judgement of their upcoming turn."""

        if player == self._not_player_turn or self._game_won is True:

            return False

        else:

            if player == 1:

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

            elif player == 2:

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
        position necessary for a win then the method will return true. This is a last step."""

        """DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS"""

        """ This method uses a for loop to loop through each end of the board depending on the player parameter.
        If it is player 1, it checks for the board end that player 1 needs to reach so that a win can be declared. It 
        does the same for player 2 but on the opposite end. """

        if player == 1:

            for pos in self._board[8]:

                if player in pos:

                    self._game_won = True

                    return True

            return False

        elif player == 2:

            for pos in self._board[0]:

                if player in pos:

                    self._game_won = True

                    return True

            return False





#var = QuoridorGame()
#print(var.move_pawn(1, (4,1)))
#print(var.place_fence(1, "h", (4,9)))
#print(var.move_pawn(1, (5,1)))
#print(var.move_pawn(1, (4,2)))
#print(var.move_pawn(2, (4,7)))
#print(var.move_pawn(1, (6,1)))
#print(var.move_pawn(2, (4,6)))
#print(var.move_pawn(1, (4,4)))
#print(var.move_pawn(2, (4,5)))
#print(var.place_fence(1, "h", (3,)))
#print(var.place_fence(2, "h", (4,6)))
#print(var.move_pawn(1, (3,5)))
# print(var.move_pawn(1, (4,4)))
# #print(var.place_fence(1, "h", (4,3)))
# print(var.move_pawn(1, (4,6)))
# print(var.move_pawn(2, (3,4)))
#print(var.move_pawn(1, (4,4)))
#print(var.place_fence(1, "v", (4,0)))
# print(var.place_fence(2, "v", (4,0)))
#print(var.get_board())

# self._board_3 = "+==+==+==+==+==+==+==+==+==+ \
#                  |                          | \
#                  +  +  +  +  +  +  +  +  +  + \
#                  |                          | \
#                  +                          + \
#                  |                          | \
#                  +                          + \
#                  |                          | \
#                  +                          + \
#                  |                          | \
#                  +                          + \
#                  |                          | \
#                  +                          + \
#                  |                          | \
#                  +                          + \
#                  |                          | \
#                  +                          + \
#                  |                          | \
#                  +==+==+==+==+==+==+==+==+==+"
#
# self._board_4 = "+==+==+==+==+==+==+==+==+==+" \
#                 "|                          |" \
#                 "+  +  +  +  +  +  +  +  +  +" \
#                 "|                          |" \
#                 "+  +  +  +  +  +  +  +  +  +" \
#                 "|                          |" \
#                 "+  +  +  +  +  +  +  +  +  +" \
#                 "|                          |" \
#                 "+  +  +  +  +  +  +  +  +  +" \
#                 "|                          |" \
#                 "+  +  +  +  +  +  +  +  +  +" \
#                 "|                          |" \
#                 "+  +  +  +  +  +  +  +  +  +" \
#                 "|                          |" \
#                 "+  +  +  +  +  +  +  +  +  +" \
#                 "|                          |" \
#                 "+  +  +  +  +  +  +  +  +  +" \
#                 "|                          |" \
#                 "+==+==+==+==+==+==+==+==+==+"

