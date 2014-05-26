import webbrowser

class Step():
    def __init__(self, dialogue, option1, option2, status):
        self.dialogue = dialogue
        self.option1 = option1
        self.option2 = option2
        self.status = status

    def win_or_lose(self):
        if self.status == 'Win':
            webbrowser.open("http://labloggergal.com/wp-content/uploads/Congratulations.jpg")
        elif self.status == 'Lose':
            webbrowser.open("http://img.4plebs.org/boards/tg/image/1393/46/1393466113011.jpg")





