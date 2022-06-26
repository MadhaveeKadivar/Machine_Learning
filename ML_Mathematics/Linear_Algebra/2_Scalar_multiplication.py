'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-09 10:20:31
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-09 10:20:52
    @Title : Scalar Multiplication of matrix
'''
import sys


def scalar_mul(x,y):
    """ 
        Description: 
            This function is multipyting one value to matrix
        Parameter:
            It takes one matrix(list of list) and one number as argument
        Return:
            returns result matrix
    """
    try:
        result = [[x[i][j]*y for j in range(len(x[0]))] for i in range(len(x))]
        return result
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")

def main():
    """ 
        Description: 
            This function is defining one matrix and one scalar value and print the scalar multiplication
        Parameter:
            None
        Return:
            None
    """
    try:
        x = [[12,7,3],[4,5,6],[7,8,9]]
        y = 9
        result_matrix = scalar_mul(x,y)
        print("scalar multiplication of matrix and a number : \n ")
        for i in result_matrix:
            for j in i:
                print(j, end = " ")
            print()
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")

if __name__=="__main__":
    main()

    
   
