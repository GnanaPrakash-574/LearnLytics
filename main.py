import storage
import quiz
import analytics

def show_menu():
    print("****------AI STUDY ASSISTANT------****\n")
    print("Instructions : Enter The Number Beside The Function You Need To Access \n")
    print(" 1.Start Quiz \n" \
    " 2.OverAll Stats \n" \
    " 3.ALL SUbjects performance \n" \
    " 4.Individual Subject Performance \n" \
    " 5.Best Subject \n" \
    " 6.Weak Subject \n" \
    " 7.stop \n")

subject = None
Functions = {"1": "Quiz",
             "2": analytics.overall_stats,
             "3": analytics.all_subjects_performance,
             "4": "Subject Perfromance",
             "5":analytics.best_subject,
             "6":analytics.weak_subject,
             "7":"stop"}

def get_instruction():
    Access = input("Enter your Function Number :").strip()
    if Access == 7:
        return None
    if Access not in Functions:
        print("please enter a valid number")
        return get_instruction()
    return Access

def access_function(access):

    if access == "1":
        subject = input("enter the subject: ")
        topic = input("enter any topic (enter no If not Specific): ").lower().strip()
        difficulty = input("enter any difficulty (enter no If not specific): ").lower().strip()
        if topic == "no":
            topic = None
        if difficulty == "no":
            difficulty = None
        
        performance = quiz.start_quiz(subject,topic,difficulty,num_questions =5)
        if performance:
            print(performance)
            storage.save_performance(performance)

    elif access == "4":
        subject = input("enter the subject")
        topic = input("enter any topic (enter no If not Specific): ").lower().strip()
        if topic == "no":
            topic = None

        analytics.subject_performance(subject,topic)
    else: 
        Functions[access]()


# MAIN FLOW
while True:
    show_menu()
    option = get_instruction()
    if option == None:
        print("Exiting AI Study Assistant ... ")
        break
        
    access_function(option)
