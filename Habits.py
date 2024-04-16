import sqlite3 

class Habit:
    def __init__(self, habit_name, user_name, category, periodicity, datetime_of_creation):
        '''Parameters
        ----------
        :param habit_name: the habitname given by the user
        :param user_name: the username defined by the user
        :param category: the category of the habit defined by the user
        :param periodicity: the periodicity defined by the user
        :param datetime_of_creation: the datetime of when the habit was defined by the user
        '''
        self.habit_name = habit_name
        self.user_name = user_name
        self.category = category
        self.periodicity = periodicity
        self.datetime_of_creation = datetime_of_creation

        
        from os.path import dirname, join, abspath
        
        #Creating the absolute path to the SQLite database file "main_db.db"
        db_path = join(dirname(abspath(__file__)),'main_db.db')
        
        #Building a connection to the SQLite database usnig the connect() function from the module sqlite3 
        # The connect() function takes the absolute path to the database file as an argument
        self.connection_to_db = sqlite3.connect(db_path)
        
        # Creating a cursor object associated with the database connection
        # The cursor object is used to execute SQL queries and fetch results from the database
        self.cursor_of_connection = self.connection_to_db.cursor()
        