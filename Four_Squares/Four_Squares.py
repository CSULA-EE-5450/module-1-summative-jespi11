from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class Four_Sqaures(App):
    """
        Class to run Kivy applications
    """
    def build(self):
        return GameBoard()


PLAYER_IDX = ['2', '1']


class GameBoard(GridLayout):
    """
        Creates a class for the GUI using kivy's GridLayout to
        organize and manage any widgets added
    """
    def __init__(self, **kwargs):
        """
            Defines the GridLayout size (cols, rows)
            Creates a board filled with 0's with the size of the GridLayout
            Defines players by the switch_player() function
            Call the next function: self.draw_btn_grid()
        """

        super(GameBoard, self).__init__(**kwargs)

        self.cols = 4
        self.rows = 4
        self.players = self.switch_players()

        self.board = [[0 for col in range(self.cols)] for row in range(self.rows)]

        self.draw_btn_grid()

    def draw_btn_grid(self):
        """
            Adds all the widgets ( Buttons ) to the GirdLayout
            Binds each widget to function self.btn_pressed()
            Fills the game board with all the widgets
            Calls the next function self.btn_pressed()
        """
        for row in range(self.rows):
            for col in range(self.cols):
                btn = Button(background_color=(0, .5, 1, 0.9))
                btn.bind(on_press=self.btn_pressed)
                self.board[row][col] = btn
                self.add_widget(btn)

    def btn_pressed(self, instance):
        """
            if a button has not been pressed, returns 0
            otherwise, if button has been pressed, switches player and
                marks the pressed btn with the player's number
            calls next function self.game_outcome()
        """
        # if button has not been pressed
        if instance.text:
            return 0
        # if button has been pressed
        instance.text = next(self.players)
        instance.font_size = 150
        instance.color = (0, 0, 0, 1)

        self.game_outcome()

    def check_for_winner(self):
        """
            Checks the Board for the possible winning combinations
            returns the player that has won, if the game has ended in a Draw or
                0 if the game is still on-going
                    Board layout:
                      |  0  |  1  |  2  |  3  |
                    0 | 0,0 | 1,1 | 2,2 | 3,3 |
                    1 | 1,0 | 1,1 | 2,2 | 3,3 |
                    2 | 2,0 | 2,1 | 2,2 | 3,3 |
                    3 | 3,0 | 3,1 | 2,2 | 3,3 |
        """
        winning_outcomes = (
            ((0, 0), (0, 1), (1, 0), (1, 1)),
            ((0, 2), (0, 3), (1, 2), (1, 3)),

            ((2, 0), (2, 1), (3, 0), (3, 1)),
            ((2, 2), (2, 3), (3, 2), (3, 3)),

            ((1, 0), (1, 1), (2, 0), (2, 1)),
            ((1, 2), (1, 3), (2, 2), (2, 3)),

            ((1, 1), (1, 2), (2, 1), (2, 2)),

            ((0, 1), (0, 2), (1, 1), (1, 2)),
            ((2, 1), (2, 2), (3, 1), (3, 2))
        )

        for win in winning_outcomes:
            row = []
            for idx in win:
                row.append(self.board[idx[0]][idx[1]].text)

            for player in PLAYER_IDX:
                if all([p_num == player for p_num in row]):
                    return player

        for row in self.board:
            for col in row:
                if col.text == '':
                    return 0

        return 'Draw'

    def game_outcome(self):
        """
            Creates a popup screen with the outcome of the game
                and a button to close the popup
            Prints the result of check_for_winner()
            Calls the next function self.restart_game()
        """
        winner = self.check_for_winner()

        if winner:
            obj = BoxLayout(orientation='vertical')
            if winner == 'Draw':
                obj.add_widget(Label(text="It is a Draw", font_size=48))
            else:
                obj.add_widget(Label(text='Player %s has won the game!' % winner, font_size=48))

            close_btn = Button(text='Close and Restart Game', font_size=48)
            obj.add_widget(close_btn)

            pop_window = Popup(title='Game Over', content=obj, auto_dismiss=False)
            pop_window.open()
            close_btn.bind(on_release=pop_window.dismiss)

            self.restart_game()

    def restart_game(self):
        """
            Clears the contents of the board
            Clears the players numbers and returns 0, to reset the game
        """
        for row in self.board:
            for col in row:
                col.text = ''

        if next(self.players) == '2':
            return 0
        else:
            next(self.players)
            return 0

    def switch_players(self):
        """
            Toggles between players
        """
        while True:
            for player in PLAYER_IDX:
                yield player


if __name__ == '__main__':
    Four_Sqaures().run()
