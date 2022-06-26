'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-16 15:18:40
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-16 15:18:40
    @Title : Correlation coefficient
'''
import sys

def find_correlation_coefficient(x,y):
    """ 
        Description: 
            This function is finding correlation coefficient of x and y
        Parameter:
            value of x(list),value of y(list)
        Return:
            return correlation coefficient value
    """
    try:
        sum_of_x = sum(x)
        sum_of_y = sum(y)
        n = len(x)

        sum_of_xy = sum([x[i]*y[i] for i in range(len(x))])
        sum_of_square_of_x = sum([x[i] * x[i] for i in range(len(x))])
        sum_of_square_of_y = sum([y[i] * y[i] for i in range(len(y))])  
        # r = correlation coefficient      
        r = (n * sum_of_xy - sum_of_x * sum_of_y) / ((n * sum_of_square_of_x - sum_of_x ** 2) 
            * (n * sum_of_square_of_y - sum_of_y ** 2)) ** 0.5
        return r
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")

def main():
    """ 
        Description: 
            This function is printing correlation coefficient of x and y
        Parameter:
            None
        Return:
            None
    """
    x = [68, 72, 65, 70, 62, 75, 78, 64, 68]
    y = [90, 85, 88, 100, 105, 98, 70, 65, 72]
    r = find_correlation_coefficient(x,y)
    print(f"The correlation coefficient of x and y : {r}")
if __name__=="__main__":
    main()