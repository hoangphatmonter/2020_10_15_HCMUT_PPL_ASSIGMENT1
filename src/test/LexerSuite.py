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

    def test_float_token_1(self):
        """test numbers of token"""
        self.assertTrue(TestLexer.checkLexeme("""012.e5""","""012.e5,<EOF>""",101))

    def test_float_token_2(self):
        """test numbers of token"""
        self.assertTrue(TestLexer.checkLexeme("""0e5""","""0e5,<EOF>""",102))

    def test_random_char_1(self):  # ???????
        """test numbers of token"""
        self.assertTrue(TestLexer.checkLexeme("""t'h""", """t,Error Token '""", 103))

    def test_random_char_2(self): #???????
        """test identifiers of token"""
        self.assertTrue(TestLexer.checkLexeme("""Pazz""","""Error Token P""",104))

    def test_random_char_3(self): #???????
        """test numbers of token"""
        self.assertTrue(TestLexer.checkLexeme("""t_____t""","""t_____t,<EOF>""",105))

    def test_vari_declare_1(self):
        """test variable declaration"""
        self.assertTrue(TestLexer.checkLexeme("""Var: a;""","""Var,:,a,;,<EOF>""", 106))


    def test_vari_declare_2(self):
        """test variable declaration"""
        self.assertTrue(TestLexer.checkLexeme("""Var: a, b, c;""", """Var,:,a,,,b,,,c,;,<EOF>""", 107))


    def test_vari_declare_3(self):  #need some output declaration
        """test variable declaration"""
        self.assertTrue(TestLexer.checkLexeme("""Var a;""", """Var,a,;,<EOF>""", 108))


    def test_vari_declare_4(self):  # need some output declaration
        """test variable declaration"""
        self.assertTrue(TestLexer.checkLexeme("""Var a,b,c""", """Var,a,,,b,,,c,<EOF>""", 109))


    def test_vari_declare_5(self):  # need some output declaration
        """test variable declaration"""
        self.assertTrue(TestLexer.checkLexeme("""Var ,a,b;""", """Var,,,a,,,b,;,<EOF>""", 110))


    def test_vari_declare_6(self):  # need some output declaration
        """test variable declaration with same variable name"""
        self.assertTrue(TestLexer.checkLexeme("""Var a,a;""", """Var,a,,,a,;,<EOF>""", 111))


    def test_vari_declare_7(self):  # need some output declaration
        """test variable declaration with initial value"""
        self.assertTrue(TestLexer.checkLexeme("""Var : a = 5;""", """Var,:,a,=,5,;,<EOF>""", 112))


    #def test_vari_declare_8(self):  # need some output declaration
    #    """test variable declaration with many dimensions"""
    #    self.assertTrue(TestLexer.checkLexeme("Var : a[2][3][4] = { { {1,2,3,4},{1,2,3,4},{1,2,3,4} }, { {1,2,3,4},{1,2,3,4},{1,2,3,4} } };", "", 1008))


    def test_vari_declare_9(self):  # need some output declaration
        """test variable declaration with dimension"""
        self.assertTrue(TestLexer.checkLexeme("""Var :a,b[10];""", """Var,:,a,,,b,[,10,],;,<EOF>""", 113))

        # need some error cases about dimension, dimension declaration

    def test_vari_declare_10(self):  # need some output declaration
        """test wrong variable declaration with dimension"""
        self.assertTrue(TestLexer.checkLexeme("""Var :b[0];""", """Var,:,b,[,0,],;,<EOF>""", 114))

    def test_vari_declare_11(self):  # need some output declaration
        """test wrong variable declaration with dimension"""
        self.assertTrue(TestLexer.checkLexeme("""True""", """True,<EOF>""", 115))
        
    def test_func_declare_1(self):
        """test some keyword about function"""
        self.assertTrue(TestLexer.checkLexeme("""Function Parameter   EndBody.""","""Function,Parameter,EndBody,.,<EOF>""",116))

    def test_fuc_declare_2(self):
        """test some keyword about function"""
        self.assertTrue(TestLexer.checkLexeme("""Body:EndBody.""", """Body,:,EndBody,.,<EOF>""",117))

    def test_comment_1(self):
        """correct comment"""
        self.assertTrue(TestLexer.checkLexeme(""" **This is** ""","""<EOF>""",118))

    def test_comment_2(self):
        """error comment"""
        self.assertTrue(TestLexer.checkLexeme("""*****""","""*,<EOF>""",119))

    def test_comment_3(self):
        """correct comment"""
        self.assertTrue(TestLexer.checkLexeme("""** * **""", """<EOF>""",120))

    def test_comment_4(self):
        """wrong comment"""
        self.assertTrue(TestLexer.checkLexeme("""** * * ""","""Unterminated Comment""",121))

    def test_comment_5(self):
        """correct case"""
        self.assertTrue(TestLexer.checkLexeme("""adf_xyz****,""","""adf_xyz,,,<EOF>""",122))

    def test_comment_6(self):
        """correct case"""
        self.assertTrue(TestLexer.checkLexeme("""Body**Body**""","""Body,<EOF>""",123))

    def test_comment_7(self):
        """double comment"""
        self.assertTrue(TestLexer.checkLexeme("""**,**.**,**""",""".,<EOF>""",124))

    def test_comment_8(self):
        """string in comment"""
        self.assertTrue(TestLexer.checkLexeme(""" **"abc"** ""","""<EOF>""",125))

    def test_comment_9(self):
        """error case"""
        self.assertTrue(TestLexer.checkLexeme(""" **"abc**"** ""","""Unclosed String: ** """,126))

    def test_comment_10(self):

        self.assertTrue(TestLexer.checkLexeme(""" **"**abc**"** ""","""abc,<EOF>""",127))

    def test_comment_11(self):
        """comment in string"""
        self.assertTrue(TestLexer.checkLexeme(""" "****" ""","""****,<EOF>""",128))

    def test_comment_12(self):
        """string with comment"""
        self.assertTrue(TestLexer.checkLexeme(""" "**"** ""","""**,Unterminated Comment""",129))

    def test_id_1(self):
        """normal id"""
        self.assertTrue(TestLexer.checkLexeme(""" z ""","""z,<EOF>""",130))

    def test_id_2(self):
        """normal id"""
        self.assertTrue(TestLexer.checkLexeme(""" aZ ""","""aZ,<EOF>""",131))

    def test_id_3(self):
        """normal id"""
        self.assertTrue(TestLexer.checkLexeme("""aZ_9""","""aZ_9,<EOF>""",132))

    def test_id_4(self):
        """Sensitive"""
        self.assertTrue(TestLexer.checkLexeme("""Error""","""Error Token E""",133))

    def test_id_5(self):
        """underscore"""
        self.assertTrue(TestLexer.checkLexeme("""_0945""","""Error Token _""",134))

    def test_id_6(self):
        """2 id"""
        self.assertTrue(TestLexer.checkLexeme("""a____Ba9 adf""","""a____Ba9,adf,<EOF>""",135))

    def test_id_7(self):
        """special char"""
        self.assertTrue(TestLexer.checkLexeme(""" #abc ""","""Error Token #""",136))

    def test_id_8(self):
        """lower case only"""
        self.assertTrue(TestLexer.checkLexeme(""" xpuewr ""","""xpuewr,<EOF>""",137))

    def test_id_9(self):
        """number and lower case"""
        self.assertTrue(TestLexer.checkLexeme("""x99934""","""x99934,<EOF>""",138))

    def test_id_10(self):
        """full case"""
        self.assertTrue(TestLexer.checkLexeme("""a9_8b_""","""a9_8b_,<EOF>""",139))

    def test_keyword_1(self):
        """common keywords"""
        self.assertTrue(TestLexer.checkLexeme("""Body Break""","""Body,Break,<EOF>""",140))

    def test_keyword_2(self):

        self.assertTrue(TestLexer.checkLexeme(""" Continue Do Else ""","""Continue,Do,Else,<EOF>""",141))

    def test_keyword_3(self):

        self.assertTrue(TestLexer.checkLexeme("""ElseIf EndBody EndIf""","""ElseIf,EndBody,EndIf,<EOF>""",142))

    def test_keyword_4(self):

        self.assertTrue(TestLexer.checkLexeme("""EndFor EndWhile For""","""EndFor,EndWhile,For,<EOF>""",143))

    def test_keyword_5(self):

        self.assertTrue(TestLexer.checkLexeme("""Function If Parameter""","""Function,If,Parameter,<EOF>""",144))

    def test_keyword_6(self):

        self.assertTrue(TestLexer.checkLexeme("""Return Then Var""","""Return,Then,Var,<EOF>""",145))

    def test_keyword_7(self):

        self.assertTrue(TestLexer.checkLexeme("""While True""","""While,True,<EOF>""",146))

    def test_keyword_8(self):

        self.assertTrue(TestLexer.checkLexeme("""False EndDo""","""False,EndDo,<EOF>""",147))

    def test_keyword_9(self):

        self.assertTrue(TestLexer.checkLexeme("""End For""","""Error Token E""",148))

    def test_keyword_10(self):

        self.assertTrue(TestLexer.checkLexeme("""TrueFalse""","""True,False,<EOF>""",149))

    def test_operator_1(self):

        self.assertTrue(TestLexer.checkLexeme("""++.-""","""+,+.,-,<EOF>""",150))

    def test_operation_2(self):
        self.assertTrue(TestLexer.checkLexeme("""-.**.""", """-.,Unterminated Comment""", 151))

    def test_operation_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" \ \. %""", """\,\.,%,<EOF>""", 152))

    def test_operation_4(self):
        self.assertTrue(TestLexer.checkLexeme("""!&&||""", """!,&&,||,<EOF>""", 153))

    def test_operation_5(self):
        self.assertTrue(TestLexer.checkLexeme("""==!=<""", """==,!=,<,<EOF>""", 154))

    def test_operation_6(self):
        self.assertTrue(TestLexer.checkLexeme("""><=>=""", """>,<=,>=,<EOF>""", 155))

    def test_operation_7(self):
        self.assertTrue(TestLexer.checkLexeme("""=/=<.>.""", """=/=,<.,>.,<EOF>""", 156))

    def test_operation_8(self):
        self.assertTrue(TestLexer.checkLexeme("""<=.>=.""", """<=.,>=.,<EOF>""", 157))

    def test_operation_9(self):
        self.assertTrue(TestLexer.checkLexeme("""<=/=""", """<=,Error Token /""", 158))

    def test_operation_10(self):
        self.assertTrue(TestLexer.checkLexeme(""">==""", """>=,=,<EOF>""", 159))

    def test_separator_1(self):
        self.assertTrue(TestLexer.checkLexeme("""()""", """(,),<EOF>""", 160))

    def test_separator_2(self):
        self.assertTrue(TestLexer.checkLexeme("""[]""", """[,],<EOF>""", 161))

    def test_separator_3(self):
        self.assertTrue(TestLexer.checkLexeme(""":.""", """:,.,<EOF>""", 162))

    def test_separator_4(self):
        self.assertTrue(TestLexer.checkLexeme(""",;""", """,,;,<EOF>""", 163))

    def test_separator_5(self):
        self.assertTrue(TestLexer.checkLexeme("""{}""", """{,},<EOF>""", 164))

    def test_literal_1(self):
        self.assertTrue(TestLexer.checkLexeme("""0000""", """0000,<EOF>""", 165))

    def test_literal_2(self):
        self.assertTrue(TestLexer.checkLexeme("""123456""", """123456,<EOF>""", 166))

    def test_literal_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0x65AF """, """0x65AF,<EOF>""", 167))

    def test_literal_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0X65BDE """, """0X65BDE,<EOF>""", 168))

    def test_literal_5(self):#
        self.assertTrue(TestLexer.checkLexeme(""" 0x065 """, """0,x065,<EOF>""", 169))

    def test_literal_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0XG897 """, """0,Error Token X""", 170))

    def test_literal_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0o567 """, """0o567,<EOF>""", 171))

    def test_literal_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0O157 """, """0O157,<EOF>""", 172))

    def test_literal_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0O157987 """, """0O157,987,<EOF>""", 173))

    def test_literal_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" 0O1579 87 """, """0O157,9,87,<EOF>""", 174))

    def test_float_literal_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" 12.45e+456 """, """12.45e+456,<EOF>""", 175))

    def test_float_literal_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" 12.45 ""","""12.45,<EOF>""",176))

    def test_float_literal_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" 12e456 ""","""12e456,<EOF>""",177))

    def test_float_literal_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" 12e-45 ""","""12e-45,<EOF>""",178))

    def test_float_literal_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" 12.0e3 ""","""12.0e3,<EOF>""",179))

    def test_float_literal_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" 12.e5 ""","""12.e5,<EOF>""",180))

    def test_float_literal_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" 12000. ""","""12000.,<EOF>""",181))

    def test_float_literal_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" 120000e-1 ""","""120000e-1,<EOF>""",182))

    def test_float_literal_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" 00012e5 ""","""00012e5,<EOF>""",183))

    def test_float_literal_10(self):#
        self.assertTrue(TestLexer.checkLexeme(""" 12e05 ""","""12e05,<EOF>""",184))

    def test_string_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \t" ""","""This is a string containing tab \t,<EOF>""",185))

    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He asked me: '"Where is John?'"" ""","""He asked me: '"Where is John?'",<EOF>""",186))

    def test_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "He is 007" ""","""He is 007,<EOF>""",187))

    def test_string_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "my name 's P." ""","""my name 's P.,<EOF>""",188))

    def test_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "mat mat ""","""Unclosed String: mat mat """,189))

    def test_string_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ta la" " ""","""ta la,Unclosed String:  """,190))

    def test_string_7(self):
        self.assertTrue(TestLexer.checkLexeme(""" "tala"" ""","""tala,Unclosed String:  """,191))

    def test_string_8(self):
        self.assertTrue(TestLexer.checkLexeme(r""" "my\b\f\r\n\t\'\\name" """,r"""my\b\f\r\n\t\'\\name,<EOF>""",192))

    def test_string_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "my\ name" ""","""Illegal Escape In String: my\ """,193))

    def test_string_10(self):#
        self.assertTrue(TestLexer.checkLexeme(""" "abc'"def" ""","""abc'"def,<EOF>""",194))

    def test_string_11(self):
        self.assertTrue(TestLexer.checkLexeme(""" "cao\ccon" ""","""Illegal Escape In String: cao\c""",195))

    def test_string_12(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\b""","""Unclosed String: abc""",196))
    #ket hop giua string va number
    # "skldfjdls => Unclosed string skldfjdls
    #string with comment in string ?
    # sau moi mot phan can lien ket voi phan cu