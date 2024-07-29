import random

class Number_generator():

    def __init__(self, sign) -> None:
        
        self.sign_str = sign


    def generate_number(self) -> list:
        """
        Generates 
        5, two digit random numbers -> "   76\n+ 34"
        3, three digit random numbers  -> "   760\n+ 314"
        1, four digit random number  -> "   76111\n+ 34534"

        retunr list
        """

        question_list = []

        # Two digits
        for i in range(0,5):
            up_num = random.randint(10, 99)
            dw_num = random.randint(10, 99)

            strr = f"   {up_num}\n{self.sign_str} {dw_num}"
            question_list.append(strr)


        # Three digits
        for i in range(0,3):
            up_num = random.randint(100, 999)
            dw_num = random.randint(100, 999)

            strr = f"   {up_num}\n{self.sign_str} {dw_num}"
            question_list.append(strr)
        

        # Four digit
        up_num = random.randint(1000, 9999)
        dw_num = random.randint(1000, 9999)

        strr = f"   {up_num}\n{self.sign_str} {dw_num}"
        question_list.append(strr)


        return question_list
        

