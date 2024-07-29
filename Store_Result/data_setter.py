import os
from datetime import date
import json
import time
import calendar


class Data_Dir_Manager():

    def __init__(self) -> None:
        self.date = date.today()
        self.month = calendar.month_name[self.date.month]
        self.day = self.date.day

    def create_year_dir(self):
        year = self.date.year
        print(year)

        path = f"Data\\{year}"

        if os.path.exists(path):
            return
        
        else:
            os.mkdir(path)


    def take_json_content(self, name: str):

        path = f"Data\\{self.date.year}\\{name}.json"

        if not os.path.exists(path):
            return {}
        
        with open(path, "r") as fp:

            dct = json.load(fp)

        return dct
            


    
    def create_month_json(self, data: dict):

        """
        Creates new Json file with month name (if not exist)
        - adds daily progress with time
        - event stores date of the progress
        """

        data = { "Ques1": 0, "Ques2": 1}
        
        curr = time.localtime()
        curr_time = f"{curr.tm_hour % 12}-{curr.tm_min}-{curr.tm_sec}"

        dct = self.take_json_content(self.month)

        content = self.take_json_content(self.month)

        new_dct = {curr_time: data}

        dct[self.day] = new_dct

        path = f"Data\\{self.date.year}\\{self.month}.json"

        obj = json.dumps(dct, indent=4)

        with open(path, "w") as fp:
            fp.write(obj)

        




if __name__ == "__main__":
    print(Data_Dir_Manager().create_month_json("yo"))