import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):


    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,301))
    
    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,302))

    def test_multi_rules_6(self):
        """test multiple parser rules"""

        input =""" ** Function to sort an array of size n **
                Function: sort 
                    Parameter: a, n
                    Body:
                        Var: i, j, tmp;
                        For (i = 0, i < n - 1, 1) Do
                            For (j = i, j < n - 1, 1) Do
                                If a[j] > a[j + 1] Then
                                  ** Make a swap **
                                    tmp = a[j + 1];
                                    a[j + 1] = a[j];
                                    a[j] = tmp;
                                EndIf.
                            EndFor.
                        EndFor.
                        Return a;
                    EndBody.
                Function: main
                    Body:
                        Var: arr[5] = {5, 4, 3, 2, 1};
                        print(sort(arr));
                    EndBody.
            """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 303))

    def test_(self):
        input =""""""
        expect = ""
        self.assertTrue(TestParser.checkParser(input,expect,3))

#ANTLR_JARD:\hoc\college\3hk1\PPL\antlr-4.8-complete.jar