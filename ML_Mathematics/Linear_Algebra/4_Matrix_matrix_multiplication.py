'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-09 11:02:29
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-09 11:02:43
    @Title : Vector matrix multiplication
'''
import sys
def matrix_mul(x,y):
    """ 
        Description: 
            This function is multipyting matrix to matrix
        Parameter:
            It takes two matrix(list of list) as argument
        Return:
            returns result matrix
    """
    try : 
        #result = [[sum(a*b for a,b in zip(x_row,y_col)) for y_col in zip(*y)] for x_row in x]
        result = []
        for i in range(len(x)):        
            sum = []
            for j in range(len(y[0])):
                total = 0
                for k in range(len(x[0])):
                    total += x[i][k]*y[k][j]
                sum.append(total)      
            result.append(sum)
        return result
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")
def main():
    """ 
        Description: 
            This function is defining two matrix print the matrix - matrix multiplication
        Parameter:
            None
        Return:
            None
    """
    try:
        x = [[12,7,3],[4,5,6],[7,8,9]]
        y = [[5,8,1],[6,7,3],[4,5,9]]
        result_matrix = matrix_mul(x,y)
        print("Multiplication of two matrices : ")
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
