'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-16 07:15:45
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-16 07:15:45
    @Title : Rain problem
'''
import sys
        
def find_probability():
    """ 
        Description: 
            This function is finding the probability of different events
        Parameter:
            None
        Return:
            probability of even1 ,event2 and event 3
    """
    try:
        # event A = It's not raining and there is heavy traffic and I am not late 
        # event B =  I am late 
        # event C = It's rainy day if arrived late      

        prob_of_rain = 1/3
        prob_of_no_rain = 2/3
        prob_of_rain_traffic = prob_of_rain * (1/2) 
        prob_of_rain_no_traffic = prob_of_rain * (1/2)
        prob_of_no_rain_traffic = prob_of_no_rain * (1/4)
        prob_of_no_rain_no_traffic = prob_of_no_rain * (3/4)
        prob_of_rain_traffic_late = prob_of_rain_traffic * (1/2)
        prob_of_no_rain_no_traffic_late = prob_of_no_rain_no_traffic * (1/8)
        prob_of_rain_no_traffic_late = prob_of_rain_no_traffic * 0.25
        prob_of_no_rain_traffic_late = prob_of_no_rain_traffic * 0.25
        prob_of_no_rain_traffic_no_late = prob_of_no_rain_traffic * (1-0.25)

        prob_of_event_A = prob_of_no_rain_traffic_no_late
        prob_of_event_B = prob_of_rain_traffic_late + prob_of_no_rain_no_traffic_late + prob_of_rain_no_traffic_late + prob_of_no_rain_traffic_late
        prob_of_rain_late = prob_of_rain_traffic_late + prob_of_rain_no_traffic_late
        prob_of_event_C = prob_of_rain_late / prob_of_event_B

        return prob_of_event_A ,prob_of_event_B,prob_of_event_C
    
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")

def main():
    """ 
        Description: 
            This function is printing the probability of events
        Parameter:
            None
        Return:
            None
    """
    prob_of_event_A ,prob_of_event_B,prob_of_event_C = find_probability()
    print(f"The probability that it's not raining and there is heavy traffic and I am not late : {prob_of_event_A}")
    print(f"The probability that I am late : {prob_of_event_B}")
    print(f"I arrived late at work,the probability that it rained that day : {prob_of_event_C}")

if __name__=="__main__":
    main()