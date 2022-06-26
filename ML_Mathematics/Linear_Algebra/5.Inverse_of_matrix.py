'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-16 18:32:27
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-16 18:32:27
    @Title : Inverse of Matrix
'''
import sys

def minor_elements(m, i, j):
    """ 
        Description: 
            This function is finding minors of given matrix 
        Parameter:
            It takes matrix , i(row_no) and j(column_no)
        Return:
            returns minors
    """
    try:
        return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")

def find_determinant(m):
    """ 
        Description: 
            This function is calculating determinant of matrix
        Parameter:
            It takes matrix 
        Return:
            returns determinant
    """
    #base case for 2x2 matrix
    try: 
        if len(m) == 2:
            return m[0][0]*m[1][1]-m[0][1]*m[1][0]

        determinant = 0
        for c in range(len(m)):
            determinant = determinant + ((-1)**c) * m[0][c] * find_determinant(minor_elements(m, 0, c))
            
        return determinant
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")

def find_adjoint(matrix):
    """ 
        Description: 
            This function is finding cofactors and adjoint of matrix
        Parameter:
            It takes matrix 
        Return:
            returns cofactors and adjoint
    """
    try:
        cofactor = []
        for i in range(len(matrix)):
            list_cof = []
            for j in range(len(matrix)):
                minors = minor_elements(matrix, i, j)
                list_cof.append((-1) ** j * find_determinant(minors))
            cofactor.append(list_cof)
        adjoint = [[cofactor[j][i] for j in range(len(cofactor))] for i in range(len(cofactor[0]))]
        
        return adjoint,cofactor
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")

def display(matrix):
    """ 
        Description: 
            This function is displaying matrix
        Parameter:
            It takes matrix 
        Return:
            None
    """
    for row in matrix:
        for i in row:
            print(i,end = " ")
        print()
        
def main():
    """ 
        Description: 
            This function is finding inverse of matrix
        Parameter:
            None
        Return:
            None
    """
    try :
        matrix = [[12, 7, 3], [4, 5, 6], [7, 8 ,9]]
        det = find_determinant(matrix)
        print(f"Determinant of matrix : {det}")
        if det == 0:
            print("Inverse is not possible")
        else : 
            adjoint,cofactor = find_adjoint(matrix)
            print("Cofactor matrix : ")
            display(cofactor)
            print("Adjoint of matrix : ")
            display(adjoint)
            print("Inverse of matrix : ")
            print(f"{adjoint} * 1/{det}")
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")

if __name__=="__main__":
    main()