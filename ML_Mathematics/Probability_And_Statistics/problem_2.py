'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-15 19:22:54
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-15 19:22:54
    @Title : Write a program to  find the probability of drawing an ace after drawing a king on the first draw
'''
import sys

def main():
    """ 
        Description: 
            This function is finding the probability of drawing an ace after drawing a king on the first draw
        Parameter:
            None
        Return:
            None
    """
    try:        
        total_king_cards = 4
        total_cards = 52
        probability_of_king= total_king_cards/total_cards
        print(f"Probability of drawing king : {probability_of_king}")
        print(f"Number of cards in deck : {total_cards-1}")
        no_of_cards = total_cards-1
        total_aces_cards = 4
        ace_probability = total_aces_cards/no_of_cards
        probability_of_ace_after_drawn_kig = probability_of_king * ace_probability
        print(f"Probability of drawing an ace after drawing a king on the first draw : {probability_of_ace_after_drawn_kig}")
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")
        
if __name__=="__main__":
    main()