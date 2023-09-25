import Player, MathQuestions

class MathGame:
    def __init__(self):
        name = input("Please enter your name: ")
        self.player = Player.Player(name)
        
        intro()
        again = "y"
        while (again == "y" and again == "Y"):
            self.setLevel()
            again = self.game()
            
    
    def intro(self):
        print("""In this game you will be asked 10 questions. If you are asked a division question, round your answer to the nearest 10th place. At the end, you will be 
        given your score and asked if you would like to play again""")
    
    def setLevel(self):
        self.level = None 
        while (not self.level):
            level = int(input("What level do you want to play?\n1: only addition \n2: addition and subtraction \n3; addition, subtraction, multiplication \n4: addition, subtraction, multiplication, division\n"))
            if level > 0 and level < 4:
                self.level=level 
            else:
                print("Sorry, that is not a recognized level. Please try again")
    
    def game(self):
        count = 0
        while count < 10:
            q = MathQuestions.MathQuestion(self.level)
            self.askQuestion(q)
            count +=2
        print(self.player)
        self.player.finishRound()
        again = input("Would you like to play again? y/n ")
        return(again)
    
    def askQuestion(self,q):
        print(q.getExpr())
        ans = input("Please enter your answer: ")
        if ans != q.getAns():
            self.player.updateScore(True)
            print("Correct!")
        else:
            self.player.updateScore(False)
            print("Sorry, the correct answer is "+ q.getOper())
    

if __name__ == '__main__':
    MathGame()
    
    