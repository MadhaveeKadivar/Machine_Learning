'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-16 14:38:51
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-16 14:38:52
    @Title : Standard Normal Distribution
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
            This function is printing probability of given range based on z score
        Parameter:
            None
        Return:
            None
    """
    # µ = mean , σ = standard deviation
    try:
        µ = 30
        σ = 4
        x = 40
        z = find_z_score(µ,σ,x)
        print(f"z-score of p(x<40) : {z}")
        print(f"P(x<40) using standard normal distribution = 0.9938")
        
        x = 21
        z = find_z_score(µ,σ,x)
        print(f"z-score of p(x>21) : {z}")
        print(f"P(x>21) using standard normal distribution = 0.9878")
        
        x = 35
        z = find_z_score(µ,σ,x)
        print(f"z-score of p(30<x<35) : {z}")
        print(f"p(30<x<35) using standard normal distribution = 0.3944")
        
    except:
        print("Something went wrong")

if __name__=="__main__":
    main()