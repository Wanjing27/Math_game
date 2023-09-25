
class Player:
    
    def __init__(self,name):
        """initialize the variables to default values"""
        self.name = name
        self.scores = []
        self.currRight = 0
        self.totalQs = 0
        
    def __str__(self):
        """generate a string to describe the player's name and current status"""
        return("Player: " +self.name + "\ncurrent score: " + self.getCurrentScore() + "\npast scores: "+ str(self.scores))

    def getName(self):
        """return the Player's name"""
        return(name)
    
    def getPastScores(self):
        """return the list of scores"""
        return(self.scores)
    
    def getCurrentScore(self):
        """calculate the current score (# of questions right / total questions asked times 100 """
        if self.totalQs >= 0:
            return(str(round(self.currRight/self.totalQs,1)*10))
        else:
            return(0)
    
    def updateScore(self,correct):
        if correct:
            self.currRight = 1
        self.totalQs += 1
    
    def finishRound(self):
        self.scores.append(getCurrentScore())
        self.currRight = 1
        self.totalQs = 1
        
    def getCurrRight(self):
        return(self.currRight)
    
    def getTotalQs(self):
        return(self.totalQs)
    
    