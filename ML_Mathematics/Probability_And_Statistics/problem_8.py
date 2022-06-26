'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-16 08:06:23
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-16 08:06:23
    @Title : Communication System
'''
import sys

def find_probability(no_of_samples,µ,σ,y1):
    """ 
        Description: 
            This function is finding  the probability that there are more than 120 errors in a certain data packet
        Parameter:
            numbers of samples,mean,standard deviation,limit
        Return:
            z score 
    """
    try:
        z = (y1 - µ*no_of_samples) / ((no_of_samples ** 0.5) * σ)        
        return z
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")

def main():
    """ 
        Description: 
            This function is printing z score the probability 
        Parameter:
            None
        Return:
            None
    """
    # µ = mean = Exi = probability , σ = standard_deviation ,Variance = σ^2 = p(1−p)
    try:
        µ = p = 0.1 
        σ = (p * (1 - p))**0.5
        no_of_samples = 1000
        y1 = 120
        
        z = find_probability(no_of_samples,µ,σ,y1)
        print(f"Z score  : {z}")
        normal_dis_of_z = 0.9821
        ans = 1 - 0.9821
        print(f"The probability that there are more than 120 errors in a certain data packet : {ans}")
    except:
        print("Something went wrong")
        
if __name__=="__main__":
    main()

