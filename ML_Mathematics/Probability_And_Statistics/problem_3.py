'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-15 19:28:08
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-15 19:28:08
    @Title : Write a program to find probability of drawing an ace after drawing an ace on the first draw
'''
import sys

def main():
    """ 
        Description: 
            This function is finding the probability of drawing an ace after drawing an ace on the first draw
        Parameter:
            None
        Return:
            None
    """
    try:        
        total_ace_cards = 4
        total_cards = 52
        probability_of_ace= total_ace_cards/total_cards
        print(f"Probability of drawing ace in first drawn : {probability_of_ace}")
        print(f"Number of cards in deck : {total_cards-1}")
        no_of_cards = total_cards-1
        new_aces_cards = total_ace_cards - 1
        print(f"Now total ace cards in deck : {new_aces_cards}")
        ace_probability = new_aces_cards/no_of_cards
        probability_of_ace_after_drawn_ace = probability_of_ace * ace_probability
        print(f"Probability of drawing an ace after drawing an ace on the first draw : {probability_of_ace_after_drawn_ace}")
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")
        
if __name__=="__main__":
    main()