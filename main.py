import questionary
import initiate_db

initiate_db.launch_db()

intro_message = "***************************************************************"\
                "Welcome to Habit Tracker!\n"\
                "You can use this app to track your habits for a mindful life.\n"\
                "*****************************************************************\n\n"

print(intro_message)

first_question = questionary.select("Pls Register if this is your first visit. Existing users pls Login.", choices = ["Register","Login"]).ask()

if first_question == "Login":
    user = initiate_db.login()
    print("Welcome back!\n")
elif first_question == "Register":
    print("\nWelcome! Let's set up your profile.\n")
    initiate_db.register_user()
    print("\nPlease log in:\n")
    user = initiate_db.login()

user.choose_predefined_habit()

def menu():
    
    second_question = questionary.select("What do you want to do?", choices = ["Edit User Profile","Create, Change or Mark a Habit","Activity Log","View Stats","Exit Program"]).ask()
    
    if second_question == "Edit User Profile":
        print("No problem. Let's edit your profile.\n")
        initiate_db.get_user(user)
        user.update_profile()
        print("\nPlese select next task.\n")
        menu()

    elif second_question == "Create, Change or Mark a Habit":
        habit_question = questionary.select("Do you want to: ",choices = ["Create a new habit","Delete habit", "Change an existing habit","Mark a habit as completed"]).ask()

        if habit_question == "Create a new habit":
            print("Let's create a habit.\n")
            new_habit = user.create_habit()
            user.store_habit_in_db(new_habit)
            print("\nWhat do you want to do?\n")
            menu()

        elif habit_question == "Delete habit":
            user.delete_habit()
            print("\nWhat do you want to do?")
            menu()

        elif habit_question == "Change an existing habit":
            print("Let's edit an existing habit!")
            user.update_habit()
            print("\nWhat do you want to do now?\n")
            menu()
        
        else:
            print("Let's mark a habit as completed.")
            user.is_completed()
            print("\nWhat do you want to do now?\n")
            menu()

    elif second_question == "Activity Log":
        activity_question = questionary.select("Which Activity Log do you want to see?", choices = ["all habits","all weekly habits","all daily habits"]).ask()

        if activity_question == "all habits":
            print("\nYou currently have these habits saved:\n")
            user.show_all()
            print("\nWhat do you want to do now?")
            menu()

        elif activity_question == "all weekly habits":
            print("Your weekly habits are: \n")
            user.show_weekly_habits()
            print("\nWhat do you want to do now?\n")
            menu()

        else:
            print("Your daily habits are: \n")
            user.show_daily_habits()
            print("\nWhat do you want to do now?\n")
            menu()

    if second_question == "View Stats":
        stats_question = questionary.select("What would you like to see?", choices = ["Current streak overview","Current streak per habit","Longest streak per habit","Longest streak overview."]).ask()

        # "Current streak overview","Current streak per habit","Longest streak per habit","Longest streak overview."
        if stats_question == "Current streak overview":
            user.current_streak_overview()
        elif stats_question == "Current streak per habit":
            user.current_streak_habit()
        elif stats_question == "Longest streak per habit":
            user.longest_streak_habit()
        else:
            user.longest_streak_overview()
        print("\nWhat would you like to do now?\n")
        menu()
    
    if second_question == "Exit Program":
        print(f"\nSee you later, {user.firstname}!\n")

menu()