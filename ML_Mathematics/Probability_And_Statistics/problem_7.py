'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-16 07:15:45
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-16 07:15:45
    @Title : Bank seller problem 
'''
import sys

def find_probability(no_of_samples,µ,σ,y1,y2):
    """ 
        Description: 
            This function is finding the probability in given range
        Parameter:
            numbers of samples,mean,standard deviation,lower limit,upper limit
        Return:
            z score 1, z score 2
    """
    try:
        z1 = (y1 - µ*no_of_samples) / ((no_of_samples ** 0.5) * σ)
        z2 = (y2 - µ*no_of_samples) / ((no_of_samples ** 0.5) * σ)
        return z1,z2
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
    # µ = mean = Exi, σ = standard_deviation ,variance (σ^2)= 1
    µ = 2
    σ = 1**0.5
    no_of_samples = 50
    y1 = 90
    y2 = 110
    z1,z2 = find_probability(no_of_samples,µ,σ,y1,y2)
    print(f"Z score 1 : {z1}")
    print(f"Z score 2 : {z2}")
    normal_dis_of_z1 = 0.9207
    normal_dis_of_z2 = 0.0793
    ans = normal_dis_of_z1 - normal_dis_of_z2
    print(f"P(90<Y<110) : {ans}")

if __name__=="__main__":
    main()

