from college import *
class Department(college):
    def __init__(self, dep_name, dep_code):
        self.dep_name = dep_name
        self.dep_code = dep_code

    def put_info(self):
        super().get_info()
        print(self.dep_name, self.dep_code)