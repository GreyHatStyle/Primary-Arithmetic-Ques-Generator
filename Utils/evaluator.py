
class Evalutator():

    def __init__(self) -> None:
        pass

    def evaluate(self, attempt_list: list, answer_list: list) -> list:

        """
        Will return Boolean list of Write and wrong answers\n
        - correct answer: 1
        - Incorrect answer: 0
        - empty answer: 2
        \n
        List example: [0,1,1,0,1,2,0,1,0]
        \n
        Will change color based on these bool values
        """
        bool_list = []
        print(attempt_list)
        for i in range(0,9):
            
            if attempt_list[i] == "":
                bool_list.append(2)
            elif attempt_list[i] == str(answer_list[i]):
                bool_list.append(1)
            else:
                bool_list.append(0)

        
        return bool_list
