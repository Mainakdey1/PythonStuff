class Tictactoe:
    def __init__(self):
        self._board=[[' ']*3 for j in range(3)]
        self._player="X"
    def mark(self,i,j):
        if not 0<=i<=2 and 0<=j<=2:
            raise ValueError("Index out of bounds")
        elif self._board[i][j]!=' ':
            raise ValueError("Position is already occupied")
        elif self.winner() is not None:
            raise ValueError("Game is already completed")
        else:
            self._board[i][j]=self._player
        if self._player=="X":
            self._player="O"
        else:
            self._player="X"
            
    def _is_win(self,mark):
        board=self._board      
        return(mark==board[0][0]==board[0][1]==board[0][2] or
               mark==board[1][0]==board[1][1]==board[1][2] or 
               mark==board[2][0]==board[2][1]==board[2][2] or 
               mark==board[0][0]==board[1][0]==board[2][1] or 
               mark==board[0][1]==board[1][1]==board[2][1] or 
               mark==board[0][2]==board[1][2]==board[2][2] or
               mark==board[0][0]==board[1][1]==board[2][2] or
               mark==board[0][2]==board[1][1]==board[2][0])
    def checker(self):
        for mark in "XO":
            if self._is_win(mark):
                return True
            else:
                return False
            
    def winner(self):
        for mark in "XO":
            if self._is_win(mark):
                return mark
        return None
    
    def __str__(self):
        rows=['|'.join(self._board[r]) for r in range(3)]
        return '\n-----\n'.join(rows)
                
    
    
game=Tictactoe()
#code to play it on the terminal
y=0
while y==0:
    a,b=input("Enter your next move:").split()
    game.mark(int(a),int(b))
    print(game)
    if game.checker():
        print(game.winner(),"wins this game")
        y=1
    else:
        pass
print()
        