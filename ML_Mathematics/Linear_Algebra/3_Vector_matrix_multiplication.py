'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-09 10:38:17
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-09 10:38:28
    @Title : Vector matrix multiplication
'''
import sys


def vector_mul(x,y):
    """ 
        Description: 
            This function is multipyting vector to matrix
        Parameter:
            It takes one matrix(list of list) and one vector(list) as argument
        Return:
            returns result matrix
    """
    try:
        result = []
        for i in range(len(x)):
            total = 0
            for j in range(len(y)):
                total += x[i][j]*y[j]
            result.append(total)
        return result
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")

def main():
    """ 
        Description: 
            This function is defining one matrix and one vector and print the vector matrix multiplication
        Parameter:
            None
        Return:
            None
    """
    try:
        x =  [[ 5, 1 ,3], [ 1, 1 ,1], [ 1, 2 ,1]]
        y = [1, 2 ,3]
        result_matrix = vector_mul(x,y)
        print("Multiplication of vector and matrix : ")
        print(result_matrix)
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")

if __name__=="__main__":
    main()

    
    
