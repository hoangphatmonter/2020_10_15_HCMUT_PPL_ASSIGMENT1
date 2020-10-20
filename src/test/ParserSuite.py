import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

    def test_global_declare_1(self):
        input = """Var:;"""
        expect = "Error on line 1 col 4: ;"
        self.assertTrue(TestParser.checkParser(input,expect,301))
    def test_global_declare_2(self):
        input ="""Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,302))

    def test_global_declare_3(self):
        input ="""Var: x,y,z;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,303))

    def test_global_declare_4(self):
        input ="""Var: x,y[5],z[6][4];"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,304))

    def test_global_declare_5(self):
        input ="""Var: x=4,y[5] = 8;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,305))

    def test_gloval_declare_6(self):
        input ="""Var: x={4,5}, y[1]= {5,{6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,306))

    def test_global_declare_7(self):
        input ="""Var: x=True, a_t = "mchd"; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,307))

    def test_global_declare_8(self):
        input ="""Var: c,d=6,e,f;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,308))

    def test_global_declare_9(self):
        input ="""Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input,expect,309))

    def test_program_structure_1(self):
        input =""""""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,310))

    def test_program_structure_2(self):
        input ="""Function: main Body: EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,311))

    def test_program_structure_3(self):
        input ="""Var: x; Function: main Body: EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,312))

    def test_program_structure_4(self):
        input ="""Function: main Body: EndBody. Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,313))

    def test_program_structure_5(self):
        input ="""Var: x;
        Function: aA_ Body: EndBody.
        Var:y;
        Function: a_ Body: EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,314))

    def test_func_declare(self):
        input ="""Var: x;
        Function: fact
            Parameter: n
            Body:
                If n == 0 Then
                    Return 1;
                Else
                    Return n * fact (n - 1);
                EndIf.
            EndBody.
        Function: main
            Body:
                x = 10;
                fact (x);
            EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,315))

    def test_fuc_declare_2(self):
        """easiest case"""
        input ="""Function: a_b
        Parameter:y,v
        Body:
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,316))

    def test_func_declare_3(self):
        input ="""Function:
        Parameter: t
        Body:
        EndBody."""
        expect = "Error on line 2 col 8: Parameter"
        self.assertTrue(TestParser.checkParser(input,expect,317))

    def test_func_declare_4(self):
        input ="""Function: a
        Parameter: t[6]=5
        Body:
        EndBody."""
        expect = "Error on line 2 col 23: ="
        self.assertTrue(TestParser.checkParser(input,expect,318))

    def test_func_declare_5(self):
        input ="""Function: a
        Body:
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,319))

    def test_func_declare_6(self):
        input ="""Function: 456
        Body:
        EndBody."""
        expect = "Error on line 1 col 10: 456"
        self.assertTrue(TestParser.checkParser(input,expect,320))

    def test_func_declare_7(self):
        input ="""Function: a_9
        Parameter:
        Body:
        EndBody."""
        expect = "Error on line 3 col 8: Body"
        self.assertTrue(TestParser.checkParser(input,expect,321))

    def test_comment(self):
        input ="""** This is single-line comment. **
        ** This is a
        * multi-line
        * comment.
        **"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,322))

    def test_array_1(self):
        input ="""Var: a[5] = {1,4,3,2,0};
        Var: b[2][3]={{1,2,3},{4,5,6}};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,323))

    def test_local_vari_1(self):
        """bo Do thi nat"""
        input ="""Function: foo
        Parameter: a[5], b
        Body:
            Var: i = 0;
            While(i < 5) Do
                a[i] = b +. 1.0;
                i = i+1;
            EndWhile.
        EndBody."""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,324))

    def test_local_vari_2(self):
        input ="""Function: foo
        Body:
            Var: i = 3;
            While (True) Do
            EndWhile.
            Var: z = 5;
        EndBody."""
        expect = "Error on line 6 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,325))

    def test_local_vari_3(self):
        input ="""Function: foo
        Body:
            Var: x[i] = 5;
            While(False) Do
                Var: t= 5;
            EndWhile.
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,326))

    def test_index_op_1(self):###############
        """fail on global"""
        input ="""Var: a[3 + foo(2)] = 4;"""
        expect ="Error on line 1 col 9: +"
        self.assertTrue(TestParser.checkParser(input,expect,327))

    def test_index_op_2(self):
        input ="""Function: a
        Body:
            Var: a[3+foo(2)] = a[b[2][3]] +4;
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,328))

    def test_func_call_1(self):
        input ="""Function: t
        Body:
            foo();
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,329))

    def test_func_call_2(self):
        input ="""foo(5,6)"""
        expect ="Error on line 1 col 0: foo"
        self.assertTrue(TestParser.checkParser(input,expect,330))

    def test_local_vari_4(self):
        input ="""Function: t
        Body:
            Var: r = 10., v;
            v = (4. \. 3.) *. 3.14 *. r *. r *. r;
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,331))

    def test_local_vari_5(self):
        input ="""Function: aT
        Body:
            Var: rtx = (4. +. 3.) * foo();
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,332))

    def test_assign_1(self):
        input ="""Function: t
        Body:
            variable = expression;"""
        expect ="Error on line 3 col 12: variable"
        self.assertTrue(TestParser.checkParser(input,expect,333))

    def test_assign_2(self):
        input ="""Function: z9
        Body:
            man=t=x;
        EndBody."""
        expect ="Error on line 3 col 17: ="
        self.assertTrue(TestParser.checkParser(input,expect,334))

    def test_assign_3(self):
        input ="""Function: t5
        Body:
            body = foo() +. 5;"""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,335))

    def test_assign_4(self):
        input ="""Function: x_5
        Body:
            foo() = body;
        EndBody."""
        expect ="Error on line 3 col 18: ="
        self.assertTrue(TestParser.checkParser(input,expect,336))

    def test_assign_5(self):
        input ="""Function: x_6
        Body:
            vari = vari;
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,337))

    def test_assign_6(self):
        input ="""Function: tamG
        Body:
            vari = +;
        EndBody."""
        expect ="Error on line 3 col 19: +"
        self.assertTrue(TestParser.checkParser(input,expect,338))

    def test_assign_7(self):
        input ="""Function: x9
        Body:
            vari = (5+6);
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,339))

    def test_assign_8(self):
        input =r"""Function: y8_com
        Body:
            vari = "Hello\nworld";
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,340))

    def test_if_1(self):
        input ="""Function: q9
        Body:
            If expression Then statement=5;
            ElseIf expression Then statement=4;
            ElseIf expression Then statement=3;
            Else statement;
            EndIf.
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,341))

    def test_if_2(self):
        input ="""Function: q9
        Body:
            If True Then t=5.6;
            EndIf.
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,342))

    def test_if_3(self):
        input ="""Function:z5_
        Body:
            If False Then ;
            ElseIf True Then t=g;
            EndIf.
        EndBody."""
        expect ="Error on line 3 col 26: ;"
        self.assertTrue(TestParser.checkParser(input,expect,343))

    def test_if_4(self):
        input ="""Function:g5
        Body:
            If False Then
            ElseIf True Then t[4] = {5};
            ElseIf True Then t[4] = {5};
            Else 
            EndIf.
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,344))

    def test_if_5(self):
        input ="""Function:g5
        Body:
            If False Then
            Else If True Then t[4] = {5} ; EndIf.
            Else If True Then t[4] = {5};
            Else 
            EndIf.
        EndBody."""
        expect ="Error on line 8 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,345))

    def test_for_1(self):
        input ="""Function: for
        Body:
            For (scalar = init, condi, update) Do
                statement = 5;
            EndFor.
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,346))

    def test_for_2(self):
        input ="""Function: for
        Body:
            For () Do
                statement;
            EndFor.
        EndBody."""
        expect ="Error on line 3 col 17: )"
        self.assertTrue(TestParser.checkParser(input,expect,347))

    def test_for_3(self):
        input ="""Function: for
        Body:
            For (t=4, t<10) Do
                t = t+1;
            EndFor.
        EndBody."""
        expect ="Error on line 3 col 26: )"
        self.assertTrue(TestParser.checkParser(input,expect,348))

    def test_for_4(self):
        input ="""Function: for
        Body:
            For (c=t*6, c*0 > 1, -c) Do
                c[6] = 5;
            EndFor.
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,349))

    def test_for_5(self):
        input ="""Function: for
        Body:
            For(z=5,z,z) Do
                foo();
                z=5;
            EndFor.
        EndBody."""
        expect ="Error on line 5 col 17: ="
        self.assertTrue(TestParser.checkParser(input,expect,350))

    def test_for_6(self):
        input ="""Function: for
        Body:
            For(a=5,z,a) Do
            EndFor
        EndBody."""
        expect ="Error on line 5 col 8: EndBody"
        self.assertTrue(TestParser.checkParser(input,expect,351))

    def test_for_7(self):
        input ="""Function: for
        Body:
            For(a=5, a!= 6, a-1)
            EndFor.
        EndBody."""
        expect ="Error on line 4 col 12: EndFor"
        self.assertTrue(TestParser.checkParser(input,expect,352))

    def test_for_8(self):
        input ="""For(t=9, (t<9), t+1) Do
        EndFor."""
        expect ="Error on line 1 col 0: For"
        self.assertTrue(TestParser.checkParser(input,expect,353))

    def test_while_2(self):
        input ="""While a!=5 Do statement;EndWhile."""
        expect ="Error on line 1 col 0: While"
        self.assertTrue(TestParser.checkParser(input,expect,354))

    def test_while_3(self):
        input ="""Function: while
        Body:
            While t!=5 Do t=5; EndWhile.
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,355))

    def test_parent_1(self):
        input ="""Function: while
        Body:
            While (t!=5) Do (t=5;) EndWhile.
        EndBody."""
        expect ="Error on line 3 col 28: ("
        self.assertTrue(TestParser.checkParser(input,expect,356))

    def test_parent_2(self):
        input ="""Function: while
        Body:
            While (t!=5) Do (t=5); EndWhile.
        EndBody."""
        expect ="Error on line 3 col 28: ("
        self.assertTrue(TestParser.checkParser(input,expect,357))

    def test_while_4(self):
        input ="""Function: while
        Body:
            While (t!=5) Do EndWhile.
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,358))

    def test_while_5(self):
        input ="""Function: while
        Body:
            While (t!=5) Do
                While (t!=5) Do t=5; EndWhile. 
            EndWhile.
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,359))

    def test_do_while_1(self):
        input ="""Do statement;While a!=5 EndWhile."""
        expect ="Error on line 1 col 0: Do"
        self.assertTrue(TestParser.checkParser(input,expect,360))

    def test_do_while_2(self):
        input ="""Function: while
        Body:
            Do t=5; While t!=5 EndDo.
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,361))

    def test_do_while_3(self):
        input ="""Function: while
        Body:
            Do While (t!=5) EndWhile.
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,362))

    def test_do_while_4(self):
        input ="""Function: while
        Body:
            Do
                Do t=5; While (t!=5) EndDo. 
            While (t!=5) EndWhile.
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,363))

    def test_break_1(self):
        input ="""Break;"""
        expect ="Error on line 1 col 0: Break"
        self.assertTrue(TestParser.checkParser(input,expect,364))

    def test_break_2(self):
        input ="""Function: a
        Body:
            Break;
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,365))

    def test_break_3(self):
        input ="""Function: b
        Body:
            Break t;
        EndBody."""
        expect ="Error on line 3 col 18: t"
        self.assertTrue(TestParser.checkParser(input,expect,366))

    def test_break_4(self):
        input ="""Function: c
        Body:
            For(t=5, t!=6, t+1) Do
                Break;
            EndFor.
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,367))

    def test_break_5(self):
        input ="""Function: c
        Body:
            For(t=5, t!=6, t+1) Do
                If(t==5 )Break; EndIf.
            EndFor.
        EndBody."""
        expect =""
        self.assertTrue(TestParser.checkParser(input,expect,368))

    def test_continue_1(self):
        input ="""Continue;"""
        expect ="Error on line 1 col 0: Continue"
        self.assertTrue(TestParser.checkParser(input,expect,369))

    def test_continue_2(self):
        input ="""Function: a
        Body:
            Continue;
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,370))

    def test_continue_3(self):
        input ="""Function: b
        Body:
            Continue c;
        EndBody."""
        expect ="Error on line 3 col 21: c"
        self.assertTrue(TestParser.checkParser(input,expect,371))

    def test_continue_4(self):
        input ="""Function: c
        Body:
            For(t=5, t!=6, t+1) Do
                Continue;
            EndFor.
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,372))

    def test_continue_5(self):
        input ="""Function: c
        Body:
            For(t=5, t!=6, t+1) Do
                If(t==5 )Continue; EndIf.
            EndFor.
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,373))

    def test_call_1(self):
        input ="""foo();"""
        expect ="Error on line 1 col 0: foo"
        self.assertTrue(TestParser.checkParser(input,expect,374))

    def test_call_2(self):
        input ="""Function: t
        Body:
            foo(9);
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,375))

    def test_call_3(self):
        input ="""Funtion: z
        Body:
            Var: t = foo(5+6);
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,376))

    def test_call_4(self):
        input ="""Var: x5 = foo()"""
        expect ="Error on line 1 col 31: ("
        self.assertTrue(TestParser.checkParser(input,expect,377))

    def test_call_5(self):
        input ="""Function: a
        Body:
            foo (2+x, 4. \. y);
            goo ();
        EndBody;"""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,378))

    def test_return_1(self):
        input ="""Return 5;"""
        expect ="Error on line 1 col 0: Return"
        self.assertTrue(TestParser.checkParser(input,expect,379))

    def test_return_2(self):
        input ="""Function: t
        Body:
            Return 5;
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,380))

    def test_return_3(self):
        input ="""Function: t
        Body:
            Return;
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,381))

    def test_return_4(self):
        input ="""Function: t
        Body:
            Return 2+x;
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,382))

    def test_return_5(self):
        input ="""Function: t
        Body:
            Return (x+5 * 6);
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,383))

    def test_all_1(self):
        input ="""Function: test
        Parameter: n
        Body:
            If n > 10 Then
                Return 5;
            Else
                Return True;
            EndIf.
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,384))

    def test_all_2(self):
        input ="""**comment**
        Var: x = 5;"""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,385))

    def test_all_3(self):
        input ="""Function: all
        Body:
            Var : t = t+5;
            While(t!= 5)Do
                t = t+1;
            EndWhile.
            Var : x = x+3"""
        expect ="Error on line 7 col 12: Var"
        self.assertTrue(TestParser.checkParser(input,expect,386))

    def test_all_4(self):
        input ="""Function: all
        Body:
            [5]t =6;
        EndBody."""
        expect ="Error on line 3 col 12: ["
        self.assertTrue(TestParser.checkParser(input,expect,387))

    def test_all_5(self):
        input ="""Function:all
        Body:
            a = t(6) + t[6] +. 6 \\. 3 +4;
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,388))

    def test_all_6(self):
        input ="""Function: all
        Body:
            a[6] = 7==5;
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,389))

    def test_all_7(self):
        input ="""Function: all
        Body:
            t[4][3] = 6\\3 % 4 + 5 - 4 ;
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,390))

    def test_all_8(self):####################
        input ="""Function: all
        Body:
            t = 5>6 <= 7 >=. 8 <=. 9 != t;
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,391))

    def test_all_9(self):
        input ="""Function: all
        Body:
            t = 5!;
        EndBody."""
        expect ="Error on line 3 col 18: ;"
        self.assertTrue(TestParser.checkParser(input,expect,392))

    def test_all_10(self):
        input ="""Function: all
        Body:
            t = !(t+1);
        EndBody."""
        expect ="successful"
        self.assertTrue(TestParser.checkParser(input,expect,393))

    def test_all_11(self):
        input ="""Function: all
        Body:
            True&&False;
        EndBody."""
        expect ="Error on line 3 col 12: True"
        self.assertTrue(TestParser.checkParser(input,expect,394))

    def test_all_12(self):
        input ="""Function: all
        Body:
            t= [6]
        EndBody."""
        expect ="Error on line 3 col 15: ["
        self.assertTrue(TestParser.checkParser(input,expect,395))

    def test_all_13(self):
        input ="""Function: all
        Body:
            t = 5-;
        EndBody."""
        expect ="Error on line 3 col 18: ;"
        self.assertTrue(TestParser.checkParser(input,expect,396))

    def test_all_14(self):
        input ="""Function: all
        Body:
            t = ==6;"""
        expect ="Error on line 3 col 16: =="
        self.assertTrue(TestParser.checkParser(input,expect,397))

    def test_all_15(self):
        input ="""Function: all
        Body:
            arr[] = 4;"""
        expect ="Error on line 3 col 16: ]"
        self.assertTrue(TestParser.checkParser(input,expect,398))

    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 399))

    def test_wrong_miss_close(self):
        """Miss variable"""
        input = """Var: ;"""
        expect = "Error on line 1 col 5: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 400))

#ANTLR_JARD:\hoc\college\3hk1\PPL\antlr-4.8-complete.jar