
# coding: utf-8

# In[16]:

class Person:   
    def __init__(self,name,age,height_cm):
        self.name = name
        self.age = age
        self.height_cm = height_cm #in centimeters
    
    def print_name(self):
        print(self.name)
    
    def print_age(self):
        print(self.age)
    
    def print_height_cm(self):
        print(self.height_cm)
    
    def height_ftin(self):
        inches = self.height_cm/2.54
        feet = inches//12
        inches = inches%12
        return feet,inches

adam = Person('Adam Levine',38,190)
adam.print_name()
adam.print_age()
adam.print_height_cm()

feet,inches = adam.height_ftin()
print('Height is ',feet,' ft and ',
      "{:.1f}".format(inches),' in')


# In[24]:

class Student(Person):
    def __init__(self,name,age,height_cm,GPA,level):
        Person.__init__(self,name,age,height_cm)
        self.GPA = GPA
        self.level = level
    
    def print_name(self,status='regular'):
        print(self.name,' STUDENT: ',status)
    
    def print_GPA(self):
        print(self.GPA)
    
    def print_level(self):
        print(self.level)

nicole = Student('Nicole Kidman',19,170,3.6,'freshman')

nicole.print_name('in absentia')
nicole.print_age()
nicole.print_height_cm()
nicole.print_GPA()
nicole.print_level()

feet,inches = nicole.height_ftin()
print('Height is ',feet,' ft and ',
      "{:.1f}".format(inches),' in')


# In[ ]:



