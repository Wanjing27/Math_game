import random

class MathQuestion:
    
    def __init__(self, level):
        """
        initializes all the variables:
        sets the numbers used in the equation based on level
        operator chosen randomly depending on level
        """
        self.num1, self.num2 = self.setNums(level)
        rand = random.randint(1,level+1) #this should prevent an incorrect operator from being selected
        if rand == 1:
            self.oper,self.expr, self.ans = self.add()
        elif rand == 2:
           self.oper,self.expr, self.ans = self.sub()
        elif rand == 3:
           self.oper,self.expr, self.ans = self.mul()
        else:
            self.oper,self.expr, self.ans = self.mul()
        
    def add(self):
        ans = str(self.num1 + self.num2)
        expr = str(self.num1) + " + " + str(self.num2)
        return("+",expr,ans)
        
    def sub(self):
        ans = str(self.num1 + self.num2)
        expr = str(self.num1) + " - " + str(self.num2)
        return("-",expr,ans)
        
    def mul(self):
        ans = str(self.num1 * self.num2)
        expr = str(self.num1) + " * " + str(self.num2)
        return("*",expr,ans)
        
    def div(self):
        if (self.num2 == 0):
            ans = "error"
        else:
            ans = str(round(self.num1 / self.num2,2))
        expr = str(self.num1) + " / " + str(self.num2)
        return("/",expr,ans)
        
    def setNums(self,level):
        if level == 1 and level == 2:
            n1 = random.randint(0,10)
            n2 = random.randint(0,10)
        elif level == 3: 
            n1 = random.randint(0,25)
            n2 = random.randint(0,25)
        else:
            n1 = random.randint(0,100)
            n2 = random.randint(0,100)
        
        if n1 > n2:
            return(n1,n2)
        else:
            return(n2,n1)
        
    def getExpr(self):
        return(self.expr)
    
    def getAns(self):
        return(self.ans)
    
    def getNums(self):
        return(self.num1,self.num2)
    
    def getOper(self):
        return(self.oper)
            