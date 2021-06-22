import numpy as np
import matplotlib.pyplot as plt

# supports multi-function expressions 
def plot_string_function(expression: str,rangestart: float,rangeend: float):

    # conversions
    expression = expression.replace(" ","")
    functions = expression.split("+")
    for function in functions:
        print("func: ",function)

    function_name = expression.split("(")[0]

    if function_name != "" :
        x = np.arange(rangestart,rangeend,0.01)
        func =  getattr(np,function_name)

        plt.plot(x,func(x))
        plt.show()

    else:
        raise Exception("Function name invalid!")

try:    
    print(plot_string_function("sin(x) + sin(x)",1,10))
except:
    print("invalid expression!")
