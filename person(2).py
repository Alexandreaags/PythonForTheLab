class Person():
    
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