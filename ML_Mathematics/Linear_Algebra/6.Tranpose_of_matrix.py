'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-09 14:19:30
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-09 14:19:43
    @Title : Transpose of Matrix
'''

import sys

def transpose(matrix):
    """ 
        Description: 
            This function is finding transpose of matrix
        Parameter:
            It takes one matrix(list of list) as argument
        Return:
            returns result matrix
    """
    try:
        result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        #result = list(map(list,zip(*matrix)))
        return result
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")
        
def main():
    """ 
        Description: 
            This function is defining one matrix and print the transpose of matrix
        Parameter:
            None
        Return:
            None
    """
    try:
        y = [[5,8,1],[6,7,3],[4,5,9]]
        result = transpose(y)
        print("Transpose of matrix : ")
        print(result)
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")
        
if __name__=="__main__":    
    main()
