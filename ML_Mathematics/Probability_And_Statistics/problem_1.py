'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-15 19:16:36
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-15 19:16:36
    @Title : Write a program to find probability of drawing an ace from pack of cards
'''
import sys

def main():
    """ 
        Description: 
            This function is finding probability of drawing an ace from pack of cards
        Parameter:
            None
        Return:
            None
    """
    try:
        total_aces_cards = 4
        total_cards = 52
        probability = total_aces_cards/total_cards
        print("Probability of drawing an ace from pack of cards = ", probability)
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")
        
if __name__=="__main__":
    main()