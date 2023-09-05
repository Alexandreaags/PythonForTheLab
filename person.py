class Person():
    birthday = '2010-10-10'
    def __init__(self, name = ''):
      self.stored_name = name
      if name == '':
          print('WARNING: The name is not set')
      else:
        pass  
    
    def echo_name(self, name):
        return name 
    def echo_True(self):
        return "True"
    def store_name(self, name):
        self.stored_name = name

    def get_name(self):
        return self.stored_name 


class Teacher(Person):
    def __init__(self, course):
        super().__init__('Jae') #to have direct access to the class from which you are inheriting
        self.course = course
    
    def get_course(self):
        return self.course 
    def set_course(self, new_course):
        self.course = new_course
