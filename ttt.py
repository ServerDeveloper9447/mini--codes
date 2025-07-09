class TTT:
    def __init__(self, firstPlayer: str = "O"):
        self._player = firstPlayer
        self._turns = 0
        self._data = [[1,2,3],[4,5,6],[7,8,9]]

    def _print_board(self):
        st = ""
        for i in self._data:
            for j in i:
                st = f'{st}{j} '
            st = f'{st}\n'
        with open('ttt.output.txt', 'w') as file:
            file.write(st)
            file.close()
    
    def _placePoint(self, pos:int):
        if pos in [1,2,3]:
            self._data[0][pos-1] = self._player
        elif pos in [4,5,6]:
            self._data[1][pos-4] = self._player
        elif pos in [7,8,9]:
            self._data[2][pos-7] = self._player
        self._print_board()
        self._checkH()
        self._checkV()
        self._checkD()
        self._player = "O" if self._player == "X" else "X"
        self._turns = self._turns + 1
        if  self._turns == 9:
            print("Draw")
            exit()
    
    def _checkH(self):
        for i in self._data:
            if i[0] == i[1] == i[2]:
                print(f'{self._player} wins')
                exit()
    
    def _checkV(self):
        for i in range(3):
            if self._data[0][i] == self._data[1][i] == self._data[2][i]:
                print(f'{self._player} wins')
                exit()
    
    def _checkD(self):
        if (self._data[0][0] == self._data[1][1] == self._data[2][2]) or (self._data[0][2] == self._data[1][1] == self._data[2][0]):
            print(f'{self._player} wins')
            exit()
    
    def start(self):
        self._data = [[1,2,3],[4,5,6],[7,8,9]]
        self._print_board()
        while True:
            pos = int(input(f'Enter position for {self._player}: '))
            self._placePoint(pos)

ttt = TTT()
ttt.start()
