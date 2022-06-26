'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-16 07:15:45
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-16 07:15:45
    @Title : Write a program to find the probability of woman has cancer if she has a positive mammogram result
'''

import sys

def find_probability():
    """ 
        Description: 
            This function is finding the probability of given event
        Parameter:
            None
        Return:
            probability of cancer if positive mmg
    """
    try:
        prob_of_cancer = 0.01
        prob_of_no_cancer = 0.99
        prob_of_positive_mmg_cancer = 0.90
        prob_of_positive_mmg_no_cancer = 0.08

        # By applying Bayes' Theorem
        denominator = prob_of_cancer * prob_of_positive_mmg_cancer + prob_of_no_cancer * prob_of_positive_mmg_no_cancer
        numerator = prob_of_cancer * prob_of_positive_mmg_cancer
        prob_of_cancer_if_positive_mmg = numerator/denominator

        return prob_of_cancer_if_positive_mmg
        
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")
    
def main():
    """ 
        Description: 
            This function is printing the probability 
        Parameter:
            None
        Return:
            None
    """
    prob_of_cancer_if_positive_mmg = find_probability()
    print(f"The probability of woman has cancer if she has a positive mammogram result : {prob_of_cancer_if_positive_mmg}")


if __name__=="__main__":
    main()