import sys

from diarybook import Diary, Diarybook

class Menu:
 ''' Displays a list of choices on the terminal for  the user to run '''

 def __init__(self):

      self.diarybook = Diarybook()

      self.choices = {
           "1" : self.show_diaries,
           "2" : self.add_diary,
           "3" : self.search_diaries,
           "4" : self.quit

        }



 def display_menu(self):
       print(""" 
              Notebook Menu  

             1. Show diaries
             2. Add diary
             3. Search diaries
             4. Quit program
             """)

 def run(self):
     ''' Display menu and respond to user choices '''

     while True:

          self.display_menu()
           choice = input("Enter an option: " )
           action = self.choices.get(choice)
           if action:
                action()
           else:
              print("{0} is not a valid choice".format(choice))

 def show_diaries(self, diaries=None):
     ''' Display all diaries in diarybook '''

     if not diaries:
        diaries = self.diarybook.diaries
     for diary in diaries:
       print("{0}".format(diary.memo)) 
       
 def add_diary(self):
     ''' Add a new diary in the diarybook '''

     memo = input("Enter a memo:         " )
     self.diarybook.new_diary(memo)
     print("Your note has been added")


 def search_diaries(self):
     ''' Search for a specific diary in the diarybook using the match filter '''

     filter = input("Search for:  ")
     diaries = self.diarybook.search_diary(filter)
     self.show_diaries(diaries)

 def quit(self):
      ''' quit or terminate the program '''  
      print("Thank you for using diarybook today")
      sys.exit(0)

if __name__ == "__main__":
    Menu().run()

