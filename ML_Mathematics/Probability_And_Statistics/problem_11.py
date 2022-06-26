'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-16 14:56:17
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-16 14:56:17
    @Title : Radar problem using Standard Normal Distribution 
'''

def find_z_score(µ,σ,x):
    """ 
        Description: 
            This function is finding z score of x value
        Parameter:
            mean,standard deviation,value of x
        Return:
            Result z score
    """
    try:
        z_score = (x - µ)/σ
        return z_score
    except:
        print("Something went wrong")

def main():
    """ 
        Description: 
            This function is printing probability of car picked at random is travelling at more than 100 km/hr
        Parameter:
            None
        Return:
            None
    """
    # µ = mean , σ = standard deviation
    try:
        µ = 90
        σ = 10
        x = 100
        z = find_z_score(µ,σ,x)
        print(f"z-score of p(x>100) : {z}")
        print(f"The probability that a car picked at random is travelling at more than 100 km/hr = 0.1587")        
    except:
        print("Something went wrong")

if __name__=="__main__":
    main()