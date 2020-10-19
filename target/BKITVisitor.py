# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#glo_vari_declare.
    def visitGlo_vari_declare(self, ctx:BKITParser.Glo_vari_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#glo_variable_list.
    def visitGlo_variable_list(self, ctx:BKITParser.Glo_variable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vari_intval.
    def visitVari_intval(self, ctx:BKITParser.Vari_intvalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable.
    def visitVariable(self, ctx:BKITParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#array.
    def visitArray(self, ctx:BKITParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#list_literal.
    def visitList_literal(self, ctx:BKITParser.List_literalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#t.
    def visitT(self, ctx:BKITParser.TContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#fun_declare.
    def visitFun_declare(self, ctx:BKITParser.Fun_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#fun_para_struct.
    def visitFun_para_struct(self, ctx:BKITParser.Fun_para_structContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#fun_para_list.
    def visitFun_para_list(self, ctx:BKITParser.Fun_para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#fun_body.
    def visitFun_body(self, ctx:BKITParser.Fun_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement_list.
    def visitStatement_list(self, ctx:BKITParser.Statement_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement_not_declare.
    def visitStatement_not_declare(self, ctx:BKITParser.Statement_not_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#local_vari_declare.
    def visitLocal_vari_declare(self, ctx:BKITParser.Local_vari_declareContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#local_variable_list.
    def visitLocal_variable_list(self, ctx:BKITParser.Local_variable_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#vari_intval_id.
    def visitVari_intval_id(self, ctx:BKITParser.Vari_intval_idContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assign_stm.
    def visitAssign_stm(self, ctx:BKITParser.Assign_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#if_stm.
    def visitIf_stm(self, ctx:BKITParser.If_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#for_stm.
    def visitFor_stm(self, ctx:BKITParser.For_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_stm.
    def visitWhile_stm(self, ctx:BKITParser.While_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#do_while_stm.
    def visitDo_while_stm(self, ctx:BKITParser.Do_while_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#break_stm.
    def visitBreak_stm(self, ctx:BKITParser.Break_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continue_stm.
    def visitContinue_stm(self, ctx:BKITParser.Continue_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stm.
    def visitCall_stm(self, ctx:BKITParser.Call_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#call_stm_para_list.
    def visitCall_stm_para_list(self, ctx:BKITParser.Call_stm_para_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stm.
    def visitReturn_stm(self, ctx:BKITParser.Return_stmContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#relational_op.
    def visitRelational_op(self, ctx:BKITParser.Relational_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#logical_op.
    def visitLogical_op(self, ctx:BKITParser.Logical_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#adding_op.
    def visitAdding_op(self, ctx:BKITParser.Adding_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#multiplying_op.
    def visitMultiplying_op(self, ctx:BKITParser.Multiplying_opContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp.
    def visitExp(self, ctx:BKITParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp1.
    def visitExp1(self, ctx:BKITParser.Exp1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp2.
    def visitExp2(self, ctx:BKITParser.Exp2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp3.
    def visitExp3(self, ctx:BKITParser.Exp3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp4.
    def visitExp4(self, ctx:BKITParser.Exp4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp5.
    def visitExp5(self, ctx:BKITParser.Exp5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp6.
    def visitExp6(self, ctx:BKITParser.Exp6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#index_operators.
    def visitIndex_operators(self, ctx:BKITParser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#exp7.
    def visitExp7(self, ctx:BKITParser.Exp7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#operand.
    def visitOperand(self, ctx:BKITParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#constants.
    def visitConstants(self, ctx:BKITParser.ConstantsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#literal.
    def visitLiteral(self, ctx:BKITParser.LiteralContext):
        return self.visitChildren(ctx)



del BKITParser