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

        if self.sign_str == "÷":
            return self.generate_division()
        


        question_list = []
        answer_list = []


        # Two digits
        for i in range(0,5):
            num1 = random.randint(10, 99)
            num2 = random.randint(10, 99)
            up_num = max(num1, num2)
            dw_num = min(num1, num2)
            answer_list.append(self.evaluate(up_num, dw_num, self.sign_str))

            strr = f"   {up_num}\n{self.sign_str} {dw_num}"
            question_list.append(strr)


        # Three digits
        for i in range(0,3):
            num1 = random.randint(100, 999)
            num2 = random.randint(100, 999)
            up_num = max(num1, num2)
            dw_num = min(num1, num2)
            answer_list.append(self.evaluate(up_num, dw_num, self.sign_str))

            strr = f"   {up_num}\n{self.sign_str} {dw_num}"
            question_list.append(strr)
        

        # Four digit
        num1 = random.randint(1000, 9999)
        num2 = random.randint(1000, 9999)
        up_num = max(num1, num2)
        dw_num = min(num1, num2)
        answer_list.append(self.evaluate(up_num, dw_num, self.sign_str))

        strr = f"   {up_num}\n{self.sign_str} {dw_num}"
        question_list.append(strr)

        return {"question_list": question_list, "answer_list": answer_list}
    


    
    def generate_division(self):
        """
        Generate small divisions:  76\n÷  2"
        """

        question_list = []
        answer_list = []
        # Two digits
        for i in range(0,9):
            num1 = random.randint(2, 11)
            num2 = random.randint(4, 999)
            up_num = max(num1, num2)
            dw_num = min(num1, num2)
            answer_list.append(self.evaluate(up_num, dw_num, self.sign_str))

            strr = f"   {up_num}\n{self.sign_str}   {dw_num}"
            question_list.append(strr)

        return {"question_list": question_list, "answer_list": answer_list}
    

    def evaluate(self, num1: int, num2: int, sign: str):
        
        if sign == "+":
            ans = num1 + num2

        elif sign == "-":
            ans = num1 - num2

        elif sign == "x":
            ans = num1 * num2

        elif sign == "÷":
            ans = num1//num2


        return ans

        

