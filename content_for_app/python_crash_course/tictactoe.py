""" This file corresponds to the problem "Tic Tac Toe" the Python Crash
Course.

"""

# imports go here if you need any, e.g.:
# import random

# global constants go here if you need any, e.g.:
# NUMBER_OF_BOARDS = 200

class TicTacToe:
    """ This text is called the 'docstring' of your class.  It's the main
    comment that describes how your class functions, its attributes and
    methods.  It shows up in the Python interpretter if you type:
    >>> help(TicTacToe)

    (try it out!)

    Check out your favorite references to see what should go in this docstring.
    """
    def __init__ (self,board):
        """ This is the constructor for your class.  Unlike Java, you only
        define one constructor for your class, but it can often take many
        different kinds of arguments (Python's word for inputs).

        Params:
            self -- Python classes have a very-confusing-for-beginners
                argument for each of their methods.  It's usually called
                `self`, and it's a reference to the object itself.  Think of
                it like `this` in Java, except you'll see that it needs to
                be in the definition line for each (non-static) method you
                define, and every time you refer to an attribute.
            board -- multi-line string containing the board description,
                including as its first line the game_id
        """
        # implement me!
        self.game_id = None # Fix this! Note the `self` reference, that's
                            # what makes this an attribute
        self.board = self.make_board(board) # See how I don't put `self`
                                            # into the arguments?

    def make_board(self, board_string):
        """
        Create the board, a 2-dimensional list.

        Params:
            board_string -- multi-line string containing the board description,
                including as its first line the game_id

        Return:
            a 2-dimensional list describing the state of the board.
        """
        # implement me!
        board = [[None]]
        return board

    def is_game_over(self):
        """
        Determine if the game is over.

        Return:
            1 if X has won, -1 if O has won, 2 if tie, 0 otherwise
            (Or use whatever you want to use to describe the condition.
            Methods with a name that sounds like a question usually can get
            called from an if statement, and this one can:
            >>> if my_game.is_game_over():
            >>>     do_something()
            Because 0 evaluates to `False`, and non-zero to `True`.
            )
        """
        # implement me!
        return 0

    def determine_turn(self):
        """
        Determine whose turn it is, if possible.

        This method assumes that the game is not over.

        Return:
            1 if X's turn, -1 if O's turn, 0 otherwise
        """
        # implement me!
        return 0


if __name__ == "__main__":
    """ This code block is for your script, namely part 4.  What the above
    `if` statement checks is the following: if I called this script from
    the command line, then execute this code block; otherwise skip it.

    The point is this: suppose you wanted to import your `TicTacToe` class
    into another file.  Then you probably wouldn't want to have this code
    block execute, because for example you may not even have a text file
    called `tictactoe_games.txt` present.
    """
    # Look up this "with" keyword, and understand what it does.
    with open("tictactoe_games.txt",'r') as f_in:
        # implement me!
        example_board = ("001)\n"
                         " X |   | X \n"
                         "-----------\n"
                         "   | O | X \n"
                         "-----------\n"
                         " X | O | O")
        example_game = TicTacToe(example_board)
