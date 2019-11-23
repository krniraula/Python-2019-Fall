#Name: Khem Niraula
#Student ID: 0644115
#Due Date: November 24, 2019
#MSITM 6341

class Date:
  def __init__(self):
    self.day = int
    self.month = " "
    self.year = int

  def print_date(self):
    print("{} {}, {}".format(self.month,self.day,self.year))
  
  def change_date(self,day, month, year):
    print("{} {}, {}".format(month, day, year))


my_date = Date()
my_date.day = 19
my_date.month = "June"
my_date.year = 2019
my_date.print_date()
my_date.change_date(3, "August", 2019)