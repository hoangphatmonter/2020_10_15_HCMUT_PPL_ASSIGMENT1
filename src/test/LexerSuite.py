import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
    '''
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))

    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.checkLexeme("Var","Var,<EOF>",102))

    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?svn","ab,Error Token ?",103))

    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.checkLexeme("Var x;","Var,x,;,<EOF>",104))

    def test_illegal_escape(self):
        """test illegal escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",105))

    def test_unterminated_string(self):
        """test unclosed string"""
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,106))

    def test_normal_string_with_escape(self):
        """test normal string with escape"""
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",107))
    '''
    '''
    def test_float_token_1(self):
        """test numbers of token"""
        self.assertTrue(TestLexer.checkLexeme("012.e5","0,12.e5,<EOF>",2001))

    def test_float_token_2(self):
        """test numbers of token"""
        self.assertTrue(TestLexer.checkLexeme("0e5","0e5,<EOF>",2002))

    def test_string_token_1(self): #???????
        """test numbers of token"""
        self.assertTrue(TestLexer.checkLexeme("t'h","Illegal Escape In String: t'h",2003))

    def test_vari_declare_1(self):
        """test variable declaration"""
        self.assertTrue(TestLexer.checkLexeme("Var: a;","Var, :, a, ;, <EOF>", 1001))


    def test_vari_declare_2(self):
        """test variable declaration"""
        self.assertTrue(TestLexer.checkLexeme("Var: a, b, c;", "Var, :, a, b, c, ;, <EOF>", 1002))


    def test_vari_declare_3(self):  #need some output declaration
        """test variable declaration"""
        self.assertTrue(TestLexer.checkLexeme("Var a;", "", 1003))


    def test_vari_declare_4(self):  # need some output declaration
        """test variable declaration"""
        self.assertTrue(TestLexer.checkLexeme("Var a,b,c", "", 1004))


    def test_vari_declare_5(self):  # need some output declaration
        """test variable declaration"""
        self.assertTrue(TestLexer.checkLexeme("Var ,a,b;", "", 1005))


    def test_vari_declare_6(self):  # need some output declaration
        """test variable declaration with same variable name"""
        self.assertTrue(TestLexer.checkLexeme("Var a,a;", "", 1006))


    def test_vari_declare_7(self):  # need some output declaration
        """test variable declaration with initial value"""
        self.assertTrue(TestLexer.checkLexeme("Var : a = 5;", "Var, :, a, =, 5, ;, <EOF>", 1007))


    def test_vari_declare_8(self):  # need some output declaration
        """test variable declaration with many dimensions"""
        self.assertTrue(TestLexer.checkLexeme("Var : a[2][3][4] = { { {1,2,3,4},{1,2,3,4},{1,2,3,4} }, { {1,2,3,4},{1,2,3,4},{1,2,3,4} } };", "", 1008))


    def test_vari_declare_9(self):  # need some output declaration
        """test variable declaration with dimension"""
        self.assertTrue(TestLexer.checkLexeme("Var :a,b[10];", "", 1001))

        # need some error cases about dimension, dimension declaration

    def test_vari_declare_10(self):  # need some output declaration
        """test wrong variable declaration with dimension"""
        self.assertTrue(TestLexer.checkLexeme("Var :b[0];", "", 1001))
    '''
    def test_vari_declare_10(self):  # need some output declaration
        """test wrong variable declaration with dimension"""
        self.assertTrue(TestLexer.checkLexeme("True", "True,<EOF>", 1001))