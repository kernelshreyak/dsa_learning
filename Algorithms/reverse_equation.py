# https://practice.geeksforgeeks.org/problems/reversing-the-equation2205/1

class Solution:
    def reverseEqn(self, eq_str):
        def is_operator(s):
            return s == '+' or s == '-' or s == '*' or s == '/'
        reversed_eq = ""
        operands = []
        operators = []
       
        current_operand = ""
        
        for s in eq_str:
            if is_operator(s):
                operators.append(s)
                operands.append(current_operand)
                current_operand = ""
            else:
                current_operand += s
        
        
        i = len(eq_str)-1
        j = len(operators)-1
        
        k = 0
        while(i >= 0):
            k += 1
            if is_operator(eq_str[i]):
                break
            i -= 1

        operands.append(eq_str[-(k-1):]) 

        i = len(operands)-1

        # print(operands)

        while(i >= 0):
            reversed_eq += str(operands[i])
            if j >= 0 :
                reversed_eq += operators[j]
                
            j -= 1
            i -= 1
            
        return reversed_eq
    

equation_str = "5-67-7/47/35*10-96"
sol = Solution()
print(sol.reverseEqn(equation_str))