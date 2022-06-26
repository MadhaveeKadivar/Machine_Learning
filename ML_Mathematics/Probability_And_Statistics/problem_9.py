'''
    @Author: Madhavee Kadivar
    @Date: 2022-06-16 14:06:39
    @Last Modified by: Madhavee Kadivar
    @Last Modified time: 2022-06-16 14:06:39
    @Title : Clinic Patient Problem
'''
import sys

def find_probability(prob_of_prescribed_pain_killers,prob_of_addict,prob_of_addict_based_on_prescribed_pain_killers):
    """ 
        Description: 
            This function is finding probability of patient will be prescribed pain pills if patient is addicted to narcotics pills
        Parameter:
            p(prescribed_pain_killers),,p(addict),p(addict|prescribed_pain_killers)
        Return:
            Result probability
    """
    try:
        # By using bayes' theorem        
        prob_of_prescribed_pain_killers_based_on_addited_patient = (prob_of_prescribed_pain_killers *
        prob_of_addict_based_on_prescribed_pain_killers)/prob_of_addict
        return prob_of_prescribed_pain_killers_based_on_addited_patient
    
    except:
        exception_type, exception_object, exception_traceback = sys.exc_info()       
        line_number = exception_traceback.tb_lineno
        print(f"Exception type : {exception_type}")
        print(f"Error on line number : {line_number}")

        
def main():
    """ 
        Description: 
            This function is printing the probability 
        Parameter:
            None
        Return:
            None
    """
    prob_of_prescribed_pain_killers = 0.1
    prob_of_addict = 0.05
    prob_of_addict_based_on_prescribed_pain_killers = 0.08
    result = find_probability(prob_of_prescribed_pain_killers,prob_of_addict,prob_of_addict_based_on_prescribed_pain_killers)

    print(f"If a patient is an addict,find the probability that they will be prescribed pain pills : {result}")

if __name__=="__main__":
    main()