# As in the previous question, when a task is added into expression classes, new methods are added into these classes. Please change the way these classes are implemented in such a way that these classes do not change their contents when new tasks are added into these classes:

# - Define class Eval to calculate the value of an expression.

# - Define class PrintPrefix to return the string corresponding to the expression in prefix format.

# - Define class PrintPostfix to return the string corresponding to the expression in postfix format.

# All arithmetic classes in previous questions have just been defined as follows:

# class Exp(ABC):pass
# class BinExp(Exp):
#     def __init__(self,o1,op,o2):
#         self.left = o1
#         self.op = op
#         self.right = o2
#     def accept(self,v): return v.visitBinExp(self)
# class UnExp(Exp):
#     def __init__(self,op,o1):
#         self.op = op
#         self.operand = o1
#     def accept(self,v): return v.visitUnExp(self)
# class IntLit(Exp):
#     def __init__(self,v):
#         self.value = v
#     def accept(self,v): return v.visitIntLit(self)
# class FloatLit(Exp):
#     def __init__(self,v):
#         self.value = v
#     def accept(self,v): return v.visitFloatLit(self)

# Let v1, v2, v3 be an object of Eval, PrintPrefix, Postfix and x be an object expressing an expression, x.accept(v1) will return the value of the expression x, x.accept(v2) will return the expression in prefix format and x.accept(v3) will return the expression in postfix format.

# For testing, given some following objects:

# x1 = IntLit(1)
# x2 = FloatLit(2.0)
# x3 = BinExp(x1,"+",x1)
# x4 = UnExp("-",x1)
# x5 = BinExp(x4,"+",BinExp(IntLit(4),"*",x2))
# Be careful that you should not allowed to use type(), isinstance() when implementing this exercise.

# Tip: Use Visitor pattern.
