class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False

    def is_full(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def play(self):
        while True:
            self.print_board()
            row, col = map(int, input(f'Player {self.current_player}, enter row and column (1-3): ').split())
            row -= 1
            col -= 1
            if 0 <= row <= 2 and 0 <= col <= 2 and self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                if self.check_win():
                    print(f'Player {self.current_player} wins!')
                    break
                if self.is_full():
                    print("It's a draw!")
                    break
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            else:
                print('Invalid move! Try again.')


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
