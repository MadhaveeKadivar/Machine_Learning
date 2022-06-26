'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-09 10:03:24
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-09 10:03:47
    @Title : Addition of two matrices
'''
import sys


def add(x,y):
    """ 
        Description: 
            This function is adding correspondence element of two matrix
        Parameter:
            It takes two matrix(list of list) as argument
        Return:
            returns result matrix
    """
    try:
        result = [[x[i][j] + y[i][j]  for j in range(len(x[0]))] for i in range(len(x))]
        #result = [map(sum, zip(*i)) for i in zip(x, y)]
        return result
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")

def main():
    """ 
        Description: 
            This function is defining two matrix and print the addition of two matrix
        Parameter:
            None
        Return:
            None
    """
    try:
        x = [[12,7,3],[4,5,6],[7,8,9]]
        y = [[5,8,1],[6,7,3],[4,5,9]]
        result_matrix = add(x,y)
        print("Addition of matrices x and y is : \n")
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
    
