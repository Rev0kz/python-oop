import datetime

#Store the next available id for all new diaries or recent ones
last_id = 0  

class Diary:  
   '''Represent a diary in the diarybook.'''

   def __init__(self, memo, tags=' '):
       '''Initialize a new diary with memo and tags.creation date of new notes and id are automatically set'''  
      
       self.memo = memo
       self.tags = tags 
       self.creation_date = datetime.date.today()  
       global last_id
       last_id +=1
       self.id = last_id  
    
    
   def match(self, filter):
        '''checks if the diary matches the filter text.
         Return true if it matches exactly, false if it does not match. 
        
        Filter is case-sensitive'''

        return filter in self.memo or self.tags

class Diarybook:
    '''Represent a collection of diaries'''

    def __init__(self):
        ''' Initialize diarybook with an empty list'''

        self.diaries = []


    def new_diary(self, memo, tags=''):
       ''' Creates a new diary in the diarybook '''
       
       self.diaries.append(Diary(memo, tags))    
    
    def search_diary(self, filter):
      ''' searches all diary that match the filter '''

      return [ diary for diary in self.diaries if diary.match(filter)]


       
    
