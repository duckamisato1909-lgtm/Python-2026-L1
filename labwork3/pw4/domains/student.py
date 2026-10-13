class Student:
    def __init__(self, s_id, name, dob):
        self.__id = s_id
        self.__name = name
        self.__dob = dob

    def get_id(self): return self.__id
    def get_name(self): return self.__name
    def get_dob(self): return self.__dob

    def describe(self):
        return f"Student: {self.__id} - {self.__name} - {self.__dob}"