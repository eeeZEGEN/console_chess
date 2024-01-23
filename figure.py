# import *
# ♔♕♖♗♘♙♚♛♜♝♞♟
# Chess figures


class Figure:
    '''
    Chess figure class
    '''
    def __init__(self, type_of_figure: str = 'b_pawn', x: int = 0, y: int = 0) -> None:
        '''
        Initialize chess figure
        '''
        self.fig_type = type_of_figure
        self.fig_view = self.fig_type
        self.desk_x = x
        self.desk_y = y
        self.prob_steps: list = []
    
    
    @property
    def fig_view(self) -> str:
        '''
        Chess views property
        '''
        return self._fig_view
    
    
    @fig_view.setter
    def fig_view(self, type: str) -> None:
        '''
        Chess view setter
        '''
        self.__chess_views = {'b_king': '♔',
                              'b_queen': '♕',
                              'b_rook': '♖',
                              'b_bishop': '♗',
                              'b_knight': '♘',
                              'b_pawn': '♙', 
                              'w_king': '♚', 
                              'w_queen': '♛',
                              'w_rook': '♜',
                              'w_bishop': '♝',
                              'w_knight': '♞',
                              'w_pawn': '♟'}
        self._fig_view = self.__chess_views[type]
    
    
    def genStepRule(self) -> None:
        '''
        Function checks step ability
        '''
        self.prob_steps.clear()
        match (self.fig_type):
            case 'b_king' | 'w_king':
                if not (self.desk_x - 1 < 0):
                    self.prob_steps.append((self.desk_x - 1, self.desk_y))
                    if not (self.desk_y - 1 < 0):
                        self.prob_steps.append((self.desk_x - 1, self.desk_y - 1))
                if not (self.desk_y - 1 < 0):
                    self.prob_steps.append((self.desk_x, self.desk_y - 1))
            case 'b_queen' | 'w_queen':
                pass 
            case 'b_rook' | 'w_rook':
                pass
            case 'b_bishop' | 'w_bishop':
                pass
            case 'b_knight' | 'w_knight':
                pass
            case 'b_pawn' | 'w_pawn':
                pass
            
    
    def __str__(self) -> str:
        return self.fig_view
        

a = Figure('w_king', 2, 2)
print(a.fig_view) 

