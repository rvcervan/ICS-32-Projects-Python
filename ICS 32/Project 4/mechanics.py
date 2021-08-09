class Game:
    def __init__(self, gameboard: [[int]], row: int, col: int):
        '''
        game mechanics for the faller game
        no input calls should be used for any of the methods
        '''
        self._board = gameboard
        self._row = row + 2
        self._col = col
        self._faller = []

    def place_faller_cond(self):
        '''
        A condition where another faller is not able to be place if a faller is already present
        '''
        counter = 0
        for y in range(self._col):
            for x in range(self._row):
                if "[" in self._board[x][y] or '|' in self._board[x][y] or '*' in self._board[x][y]:
                    counter += 1
        if counter >= 3:
            return False
        else:
            return True
    def board_conditions(self):
        '''conditions that seperates the behaviors of pieces that contain | or ['''
        counter = 0
        for y in range(self._col):
            for x in range(self._row):
                if '[' in self._board[x][y]:
                    counter += 1
                elif '|' in self._board[x][y]:
                    counter += 2
        return counter

    def star_checker(self):
        '''conditions to check the stars in the board so that certain actions are taken'''
        counter = 0
        for y in range(self._col):
            for x in range(self._row):
                if '*' in self._board[x][y]:
                    counter += 1
        return counter
        

    def new_faller(self, jewels: list):
        '''initializes new faller evertime a faller is created'''
        self._faller = jewels
        return self._faller

    def board(self):
        '''prints the fully designed gameboard'''
        return self._board

    def falling(self):
        '''if input is empty line then jewel falls into next position'''
        
        for i in range(self._col):
            for x in reversed(range(self._row - 1)):
                if self._board[x + 1][i] == '   ':
                    self._board[x + 1][i] = self._board[x][i]
                    self._board[x][i] = '   '

        return self._board

    def freeze_faller(self):
        '''
        if there is a piece below a faller freeze the faller
        if an indexerror is raised from the faller reaching the bottom, freeze faller
        '''
        try:
            counter = 0
            for y in range(self._col):
                for x in range( self._row):
                    if '[' in self._board[x][y]:
                        if self._board[x+1][y] != '   ':
                            counter += 1
        except IndexError:
            counter = len(self._faller)
        if counter == len(self._faller):
            for y in range(self._col):
                for x in range(self._row):
                    if '[' in self._board[x][y]:    
                        self._board[x][y] = '|{}|'.format(self._board[x][y][1])

        return self._board

    def unfreeze_faller(self):
        '''
        if the faller were to be moved from its freezing position where there is a piece under it,
        to a position where there is no piece under it, unfreeze faller.'''
        try:
            counter = 0
            for y in range(self._col):
                for x in range(self._row):
                    if '|' in self._board[x][y]:
                        if self._board[x+1][y] != '   ':
                            counter += 1
        except IndexError:
            counter = 2
        if counter == 2:
            for y in range(self._col):
                for x in range(self._row):
                    if '|' in self._board[x][y]:    
                        self._board[x][y] = '[{}]'.format(self._board[x][y][1])
        return self._board
    def unfreeze_condition(self):
        '''condition to see if the faller can be unfrozen'''
        counter = 0
        for y in range(self._col):
                for x in range(self._row):
                    if '|' in self._board[x][y]:
                        if self._board[x+1][y] != '   ':
                            counter += 1

        return counter

    def frozen_faller(self):
        '''faller is frozen if it detects bars surrounding the pieces'''
        for y in range(self._col):
            for x in range(self._row):
                if '|' in self._board[x][y]:
                    self._board[x][y] = ' {} '.format(self._board[x][y][1])

        return self._board



    ##a faller is a group of jewels
    ##Jewels are individual pieces which are S, T, V, W, X, Y, Z

    def drop_faller(self, col_num: int):
        '''
        Drops the faller that was created
        '''
        col_num = col_num - 1

        for y in range(3):
            self._board[y][col_num] = self._faller[y]
        return self._board


    def rotate(self):
        """Rotates the faller"""
        counter = 0
        for y in range(self._col):
            for x in range(self._row):
                if "[" in self._board[x][y] or "|" in self._board[x][y]:
                    counter +=1
                    if counter == 1:
                        place_holder = self._board[x+2][y]
                        self._board[x+2][y] = self._board[x+1][y]
                        self._board[x+1][y] = self._board[x][y]
                        self._board[x][y] = place_holder
        return self._board

    def move_left(self):
        """
        Moves the faller to the left
        Won't move left if there are jewels in the way
        check piece to left if it is zero, if it is then you can move left
        """

        counter = 0
        for y in range(1, self._col):
            for x in reversed(range(self._row)):
                if '[' in self._board[x][y] and self._board[x][y-1] == '   ':
                    counter += 1
                elif '|' in self._board[x][y] and self._board[x][y-1] == '   ':
                    counter += 1
        if counter == 3:

            for y in range(1, self._col):
                for x in reversed(range(self._row)):
                    if '[' in self._board[x][y] and self._board[x][y - 1] == '   ':
                        self._board[x][y-1] = self._board[x][y]
                        self._board[x][y] = '   '
                    elif '|' in self._board[x][y] and self._board[x][y-1] == '   ':
                        self._board[x][y-1] = self._board[x][y]
                        self._board[x][y] = '   '

        return self._board

    def move_right(self):
        '''
        Move the faller to the righT
        Won't move right if there are jewels in the way
        check piece to right if it is zero, if it is then you can move right
        '''
        # for i in range(3):
        counter = 0
        for y in reversed(range(self._col - 1)):
            for x in reversed(range(self._row)):
                if '[' in self._board[x][y] and self._board[x][y+1] == '   ':
                    counter += 1
                elif '|' in self._board[x][y] and self._board[x][y+1] == '   ':
                    counter += 1

        if counter == 3:
            for y in reversed(range(self._col - 1)):
                for x in reversed(range(self._row)):
                    if '[' in self._board[x][y] and self._board[x][y + 1] == '   ':
                        self._board[x][y+1] = self._board[x][y]
                        self._board[x][y] = '   '
                    elif '|' in self._board[x][y] and self._board[x][y+1] == '   ':
                        self._board[x][y+1] = self._board[x][y]
                        self._board[x][y] = '   '

        return self._board

    def replace_matching(self):
        '''
        If there are matching jewels(longer than 3), (horizontally, vertically, diagonally)
        replace with *char*.
        '''
        for y in range(1, self._col - 1):
            for x in range(self._row):
                if self._board[x][y] != '   ':
                    if self._board[x][y][1] == self._board[x][y-1][1] and\
                            self._board[x][y][1] == self._board[x][y+1][1]:
                        self._board[x][y] = '*{}*'.format(self._board[x][y][1])
                        self._board[x][y-1] = '*{}*'.format(self._board[x][y-1][1])
                        self._board[x][y+1] = '*{}*'.format(self._board[x][y+1][1])

        for y in range(self._col):
            for x in range(1, self._row - 1):
                if self._board[x][y] != '   ':
                    if self._board[x][y][1] == self._board[x-1][y][1] and\
                            self._board[x][y][1] == self._board[x+1][y][1]:
                        self._board[x][y] = '*{}*'.format(self._board[x][y][1])
                        self._board[x-1][y] = '*{}*'.format(self._board[x-1][y][1])
                        self._board[x+1][y] = '*{}*'.format(self._board[x+1][y][1])

        for y in range(1, self._col - 1):
            for x in range(1, self._row - 1):
                if self._board[x][y] != '   ':
                    if self._board[x][y][1] == self._board[x-1][y-1][1] and\
                            self._board[x][y][1] == self._board[x+1][y+1][1]:
                        self._board[x][y] = '*{}*'.format(self._board[x][y][1])
                        self._board[x-1][y-1] = '*{}*'.format(self._board[x-1][y-1][1])
                        self._board[x+1][y+1] = '*{}*'.format(self._board[x+1][y+1][1])

        for y in range(1, self._col - 1):
            for x in range(1, self._row - 1):
                if self._board[x][y] != '   ':
                    if self._board[x][y][1] == self._board[x+1][y-1][1] and\
                            self._board[x-1][y+1][1] == self._board[x][y][1]:
                        self._board[x][y] = '*{}*'.format(self._board[x][y][1])
                        self._board[x-1][y+1] = '*{}*'.format(self._board[x-1][y+1][1])
                        self._board[x+1][y-1] = '*{}*'.format(self._board[x+1][y-1][1])
        return self._board

    def delete_matching(self):
        '''
        erase pieces with * and put empty piece in place
        '''
        for y in range(self._col):
            for x in range(self._row):
                if '*' in self._board[x][y]:
                    self._board[x][y] = '   '


    def board_checker(self):
        '''
        If created faller lands and not all pieces of created faller are present, end game
        '''
        checker = []
        for y in range(self._col):
            for x in range(self._row):
                if '[' in self._board[x][y] or '|' in self._board[x][y] or '*' in self._board[x][y]:
                    checker.append(self._board[x][y])

        if len(checker) == 0:
            return True

    def end_game(self):
        '''
        if there are pieces frozen out of bounds at the top of the board,
        end game
        '''
        checker=[]
        for y in range(self._col):
            for x in range(2):

                if self._board[x][y] != '   ':
                    checker.append(self._board[x][y])
        if len(checker) > 0:
            return True


                

    def fill_empty_space(self):
        '''
        jewels will fall in the beginning to fill empty spaces in preset boarD
        '''
        for w in range(self._row):
            for i in range(self._col):
                for x in reversed(range(self._row - 1)):
                    if self._board[x+1][i] == '   ':
                        self._board[x+1][i] = self._board[x][i]
                        self._board[x][i] = '   '
        return self._board

    def obstructing_jewel(self, col: int):
        '''
        condition that blocks the user from placing the faller in a full column
        '''
        col = col - 1
        if self._board[2][col] != '   ':
            return False
        elif self._board[2][col] == '   ':
            return True

    def full_board(self):
        '''
        if the board is full and no piece can't be place, game is over
        '''
        counter = 0
        for y in range(self._col):
            for x in range(2, self._row):
                if self._board[x][y] == '   ':
                    counter += 1

        return counter
