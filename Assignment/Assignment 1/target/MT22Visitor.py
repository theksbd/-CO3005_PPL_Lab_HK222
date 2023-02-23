# Generated from main/mt22/parser/MT22.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MT22Parser import MT22Parser
else:
    from MT22Parser import MT22Parser

# This class defines a complete generic visitor for a parse tree produced by MT22Parser.

class MT22Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by MT22Parser#program.
    def visitProgram(self, ctx:MT22Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#decls.
    def visitDecls(self, ctx:MT22Parser.DeclsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#array_type.
    def visitArray_type(self, ctx:MT22Parser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimesion.
    def visitDimesion(self, ctx:MT22Parser.DimesionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimesion_type_int.
    def visitDimesion_type_int(self, ctx:MT22Parser.Dimesion_type_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#dimesion_type_float.
    def visitDimesion_type_float(self, ctx:MT22Parser.Dimesion_type_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#var_decl.
    def visitVar_decl(self, ctx:MT22Parser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#identifier_list.
    def visitIdentifier_list(self, ctx:MT22Parser.Identifier_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#typ.
    def visitTyp(self, ctx:MT22Parser.TypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#equal_exp.
    def visitEqual_exp(self, ctx:MT22Parser.Equal_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#equal_func_call.
    def visitEqual_func_call(self, ctx:MT22Parser.Equal_func_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_list.
    def visitExpression_list(self, ctx:MT22Parser.Expression_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_list_type_int.
    def visitExp_list_type_int(self, ctx:MT22Parser.Exp_list_type_intContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_list_type_float.
    def visitExp_list_type_float(self, ctx:MT22Parser.Exp_list_type_floatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_list_type_string.
    def visitExp_list_type_string(self, ctx:MT22Parser.Exp_list_type_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter.
    def visitParameter(self, ctx:MT22Parser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression.
    def visitExpression(self, ctx:MT22Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_1.
    def visitExpression_1(self, ctx:MT22Parser.Expression_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_2.
    def visitExpression_2(self, ctx:MT22Parser.Expression_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_3.
    def visitExpression_3(self, ctx:MT22Parser.Expression_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_4.
    def visitExpression_4(self, ctx:MT22Parser.Expression_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_5.
    def visitExpression_5(self, ctx:MT22Parser.Expression_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_6.
    def visitExpression_6(self, ctx:MT22Parser.Expression_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_7.
    def visitExpression_7(self, ctx:MT22Parser.Expression_7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#expression_8.
    def visitExpression_8(self, ctx:MT22Parser.Expression_8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#factor.
    def visitFactor(self, ctx:MT22Parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#function_call.
    def visitFunction_call(self, ctx:MT22Parser.Function_callContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exps_list.
    def visitExps_list(self, ctx:MT22Parser.Exps_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#exp_list.
    def visitExp_list(self, ctx:MT22Parser.Exp_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#statement.
    def visitStatement(self, ctx:MT22Parser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#assign_stmt.
    def visitAssign_stmt(self, ctx:MT22Parser.Assign_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#lhs.
    def visitLhs(self, ctx:MT22Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#if_stmt.
    def visitIf_stmt(self, ctx:MT22Parser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#for_stmt.
    def visitFor_stmt(self, ctx:MT22Parser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#scala_val.
    def visitScala_val(self, ctx:MT22Parser.Scala_valContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#init_expr.
    def visitInit_expr(self, ctx:MT22Parser.Init_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#condition_expr.
    def visitCondition_expr(self, ctx:MT22Parser.Condition_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#update_expr.
    def visitUpdate_expr(self, ctx:MT22Parser.Update_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#while_stmt.
    def visitWhile_stmt(self, ctx:MT22Parser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#do_while_stmt.
    def visitDo_while_stmt(self, ctx:MT22Parser.Do_while_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#call_stmt.
    def visitCall_stmt(self, ctx:MT22Parser.Call_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#block_stmt.
    def visitBlock_stmt(self, ctx:MT22Parser.Block_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#break_stmt.
    def visitBreak_stmt(self, ctx:MT22Parser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#continue_stmt.
    def visitContinue_stmt(self, ctx:MT22Parser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_stmt.
    def visitReturn_stmt(self, ctx:MT22Parser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#func_decl.
    def visitFunc_decl(self, ctx:MT22Parser.Func_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#return_type.
    def visitReturn_type(self, ctx:MT22Parser.Return_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter_list.
    def visitParameter_list(self, ctx:MT22Parser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#parameter_prime.
    def visitParameter_prime(self, ctx:MT22Parser.Parameter_primeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MT22Parser#inheritance_subpart.
    def visitInheritance_subpart(self, ctx:MT22Parser.Inheritance_subpartContext):
        return self.visitChildren(ctx)



del MT22Parser