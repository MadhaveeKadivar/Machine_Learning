'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-16 15:44:13
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-16 15:44:13
    @Title : Probability of random number from given interval
'''
def main():
    """ 
        Description: 
            This function is finding probability of random number from interval
        Parameter:
            None
        Return:
            None
    """
    try:
        lower_limit = 7
        upper_limit = 2
        random_number = 1 / (lower_limit - upper_limit)
        print(f"Probability of getting a random number from the interval [2, 7] : {random_number}")
    except:
        print("Something went wrong")
        
if __name__=="__main__":
    main()