import unittest 
import Player
import MathQuestions 

class PlayerTests(unittest.TestCase):
    """Tests Play methods."""

    def test_is_a_player(self):
        """Test to verify that the p object becomes a Player class"""
        p = Player.Player("Steve")
        self.assertTrue(type(p) == Player.Player)
    
    def test_name(self):
        """Test to verify the name returned is correct """
        p = Player.Player("Steve")
        self.assertEqual(p.getName(), "Steve")
        
    def test_update_score0(self):
        """Test to verify that a player with no answered questions has the right number of current correct and total questions"""
        p = Player.Player("Steve")
        self.assertEquals(p.getCurrRight(),0)
        self.assertEquals(p.getTotalQs(),0)
        
    def test_update_score1(self):
        """Test to verify that an update with a correct answer returns the right current correct and total questions"""
        p = Player.Player("Steve")
        p.updateScore(True)
        self.assertEquals(p.getCurrRight(),1)
        self.assertEquals(p.getTotalQs(),1)
        
    def test_update_score2(self):
        """Test to verify that an update with an incorrect answer returns the right current correct and total questions
        Relies on the score update tests to work correctly"""
        p = Player.Player("Steve")
        p.updateScore(False)
        self.assertEquals(p.getCurrRight(),0)
        self.assertEquals(p.getTotalQs(),1)
        
    def test_update_score3(self):
        """Test to verify that an update with two correct answers returns the right current correct and total questions
        Relies on the score update tests to work correctly"""
        p = Player.Player("Steve")
        p.updateScore(True)
        p.updateScore(True)
        self.assertEquals(p.getCurrRight(),2)
        self.assertEquals(p.getTotalQs(),2)

    def test_score1(self):
        """Test to verify that initial score is 0
        Relies on the score update tests to work correctly"""
        p = Player.Player("Steve")
        self.assertEqual(p.getCurrentScore(),0)
        
    def test_score2(self):
        """Test to verify that after getting 1 question correct the score is 100
        Relies on the score update tests to work correctly"""
        p = Player.Player("Steve")
        p.updateScore(True)
        self.assertTrue(p.getCurrentScore(),100)
        
    def test_score3(self):
        """Test to verify that after getting 1 question correct and 1 question wrong the score is 50
        Relies on the score update tests to work correctly"""
        p = Player.Player("Steve")
        p.updateScore(True)
        p.updateScore(False)
        self.assertTrue(p.getCurrentScore(),50)
        
    def test_score4(self):
        """Test to verify that after getting 1 question correct and 2 questions wrong the score is 33.3. This tests the rounding as well
        Relies on the score update tests to work correctly"""
        p = Player.Player("Steve")
        p.updateScore(True)
        p.updateScore(False)
        p.updateScore(False)
        self.assertTrue(p.getCurrentScore(),33.3)
        
    def test_finish_round1(self):
        """Test to make sure the function that ends the round works
        The previous score tests must be working in order for this to work"""
        p = Player.Player("Steve")
        p.updateScore(True)
        p.updateScore(True)
        p.updateScore(True)
        p.finishRound()
        self.assertEquals(p.getPastScores(),[100])
        self.assertEquals(p.getCurrRight(),0)
        self.assertEquals(p.getTotalQs(),0)

class QuestionTests(unittest.TestCase):
    """Tests MathQuestions methods."""
    
    def test_is_question(self):
        """test to verify the __init__ function works to create a MathQuestion"""
        m = MathQuestions.MathQuestion(1)
        self.assertIs(type(m), MathQuestions.MathQuestion)
        
    def test_numbers_level_1(self):
        """test to ensure that numbers generated for level 1 are between 0 and 10 (inclusive)
        since numbers are generated randomly, we will use a loop to test multiple questions
        """
        m = MathQuestions.MathQuestion(1)
        count = 0
        while count < 100:  #since numbers should only be between 0 and 10, 100 tests should be enough to randomly generate a number outside of the range at least once
            m.setNums(1)
            num1,num2 = m.getNums()
            with self.subTest("num1 = " + str(num1)):
                self.assertTrue(num1 >=0 and num1 <= 10)
            with self.subTest("num2 = " + str(num1)):
                self.assertTrue(num2 >=0 and num2 <= 10)
            count +=1
            
    def test_numbers_level_2(self):
        """test to ensure that numbers generated for level 1 are between 0 and 10 (inclusive)
        since numbers are generated randomly, we will use a loop to test multiple questions
        """
        m = MathQuestions.MathQuestion(2)
        count = 0
        while count < 100:  #since numbers should only be between 0 and 10, 100 tests should be enough to randomly generate a number outside of the range at least once
            m.setNums(2)
            num1,num2 = m.getNums()
            with self.subTest("num1 = " + str(num1)):
                self.assertTrue(num1 >=0 and num1 <= 10)
            with self.subTest("num2 = " + str(num1)):
                self.assertTrue(num2 >=0 and num2 <= 10)
            count +=1
    
    def test_numbers_level_3(self):
        """test to ensure that numbers generated for level 1 are between 0 and 10 (inclusive)
        since numbers are generated randomly, we will use a loop to test multiple questions
        """
        m = MathQuestions.MathQuestion(3)
        count = 0
        while count < 1000:  #since numbers should only be between 0 and 100, 1000 tests should be enough to randomly generate a number outside of the range at least once
            m.setNums(3)
            num1,num2 = m.getNums()
            expr = m.getExpr()
            with self.subTest("num1 = " + str(num1)):
                self.assertTrue(num1 >=0 and num1 <= 25)
            with self.subTest("num2 = " + str(num1)):
                self.assertTrue(num2 >=0 and num2 <= 25)
            with self.subTest("operation =" + expr):
                self.assertTrue("+" in expr or "-" in expr or "*" in expr)
            count +=1          
        
    def test_numbers_level_4(self):
        """test to ensure that numbers generated for level 1 are between 0 and 10 (inclusive)
        since numbers are generated randomly, we will use a loop to test multiple questions
        """
        m = MathQuestions.MathQuestion(4)
        count = 0
        while count < 1000: #since numbers should only be between 0 and 100, 1000 tests should be enough to randomly generate a number outside of the range at least once
            m.setNums(4)
            num1,num2 = m.getNums()
            with self.subTest("num1 = " + str(num1)):
                self.assertTrue(num1 >=0 and num1 <= 100)
            with self.subTest("num2 = " + str(num1)):
                self.assertTrue(num2 >=0 and num2 <= 100)
            count +=1  
            
    def test_expression_1(self):
        """test to make sure that expressions generated for level 1 contain only addition
        since expressions are generated randomly, we will use a loop to test multiple questions"""
        count = 0
        while count < 100:  
            m = MathQuestions.MathQuestion(1)
            expr = m.getExpr()
            oper = m.getOper()
            with self.subTest("expression =" + expr):
                self.assertTrue("+" in expr)
                self.assertFalse("-" in expr and "*" and expr and "/" in expr )
            with self.subTest("operator = " + oper):
                self.assertTrue("+" == oper)
            count +=1    
                 
    def test_expression_2(self):
        """test to make sure that expressions generated for level 2 contain only addition and subtraction
        since expressions are generated randomly, we will use a loop to test multiple questions"""
        count = 0
        while count < 100: 
            m = MathQuestions.MathQuestion(2)
            expr = m.getExpr()
            oper = m.getOper()
            with self.subTest("expression =" + expr):
                self.assertTrue("+" in expr or "-" in expr)
                self.assertFalse( "*" in expr and "/" in expr )
            with self.subTest("operator = " + oper):
                self.assertTrue("+" == oper or "-" == oper)
            count +=1  
            
    def test_expression_3(self):
        """test to make sure that expressions generated for level 1 contain only addition, subtraction, multiplication
        since expressions are generated randomly, we will use a loop to test multiple questions"""
        count = 0
        while count < 100:  
            m = MathQuestions.MathQuestion(3)
            expr = m.getExpr()
            oper = m.getOper()
            with self.subTest("expression =" + expr):
                self.assertTrue("+" in expr or "-" in expr or "*" in expr )
                self.assertFalse("/" in expr )
            with self.subTest("operator = " + oper):
                self.assertTrue("+" == oper or "-" == oper or "*" == oper)
            count +=1  
            
    def test_expression_4(self):
        """test to make sure that expressions generated for level 1 contain only addition, subtraction, multiplication, division
        since expressions are generated randomly, we will use a loop to test multiple questions"""
        count = 0
        while count < 100:
            m = MathQuestions.MathQuestion(4)
            expr = m.getExpr()
            oper = m.getOper()
            with self.subTest("expression =" + expr):
                self.assertTrue("+" in expr or "-" in expr or "*" in expr or "/" in expr)
            with self.subTest("operator = " + oper):
                self.assertTrue("+" == oper or "-" == oper or "*" == oper or "/" == oper)
            count +=1 
            
    def test_answer_add(self):
        """test to make sure the answers being generated for adding are correct
        relies on previous tests to be correct
        use a while loop to test many possibilities"""
        count = 0
        while count < 100:
            m = MathQuestions.MathQuestion(4)
            num1,num2 = m.getNums()
            oper,expr, ans = m.add()
            self.assertEqual(ans,str(num1+num2))
            count += 1
        
    def test_answer_sub(self):
        """test to make sure the answers being generated for subtracting are correct
        relies on previous tests to be correct
        use a while loop to test many possibilities"""
        count = 0
        while count < 100:
            m = MathQuestions.MathQuestion(4)
            num1,num2 = m.getNums()
            oper,expr, ans = m.sub()
            self.assertEqual(ans,str(num1-num2))
            count += 1
        
    def test_answer_mul(self):
        """test to make sure the answers being generated for multiplying are correct
        relies on previous tests to be correct
        use a while loop to test many possibilities"""
        count = 0
        while count < 100:
            m = MathQuestions.MathQuestion(4)
            num1,num2 = m.getNums()
            oper,expr, ans = m.mul()
            self.assertEqual(ans,str(num1*num2))
            count += 1

    def test_answer_div(self):
        """test to make sure the answers being generated for dividing are correct
        relies on previous tests to be correct
        use a while loop to test many possibilities"""
        count = 0
        while count < 100:
            m = MathQuestions.MathQuestion(4)
            num1,num2 = m.getNums()
            oper,expr, ans = m.div()
            if num2 == 0:
                self.assertEqual(ans,"error")
            else:
                self.assertEqual(ans,str(round(num1/num2,1)))
            count += 1
    

if __name__ == '__main__':
    unittest.main()