'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-15 22:30:16
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-15 22:30:17
    @Title : Write a program to find the probability of different events
'''
import sys

sample_space = ["HHH", "HHT", "HTH", "THH", "THT", "TTH","TTT", "HTT"]
total_possible_events = len(sample_space)

def three_heads():
    """ 
        Description: 
            This function is finding the probability of three heads
        Parameter:
            None
        Return:
            None
    """
    try:
        global sample_space
        global total_possible_events  
        event_1 = [sample_space[i] for i in range(total_possible_events) if sample_space[i].count("H") == 3]
        probability_of_event1 = len(event_1)/total_possible_events
        print(f"The probability of three heads : {probability_of_event1}")    
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")
        
def exactly_one_head():
    """ 
        Description: 
            This function is finding the probability of exactly one heads
        Parameter:
            None
        Return:
            None
    """
    try:
        global sample_space
        global total_possible_events
        event_2 = [sample_space[i] for i in range(total_possible_events) if sample_space[i].count("H") == 1]
        probability_of_event2 = len(event_2)/total_possible_events
        print(f"The probability of exactly one heads : {probability_of_event2}")    
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")
        
def atleast_two_heads():
    """ 
        Description: 
            This function is finding the probability of at least two heads if observed at least one heads
        Parameter:
            None
        Return:
            None
    """
    # event_3 : at least one heads
    # event_4 : at least two heads after observing atleast one heads
    try:
        global sample_space
        global total_possible_events
        event_3 = [sample_space[i] for i in range(total_possible_events) if sample_space[i].count("H") >= 1]
        event_4 = [event_3[i] for i in range(len(event_3)) if event_3[i].count("H") >= 2]
        probability_of_event4 = len(event_4)/len(event_3)
        print(f"The probability of at least two heads after observing atleast one heads : {probability_of_event4}")
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")
        
def main():
    """ 
        Description: 
            This function is finding the probability of events
        Parameter:
            None
        Return:
            None
    """
    three_heads()
    exactly_one_head()
    atleast_two_heads()

if __name__=="__main__":
    main()

