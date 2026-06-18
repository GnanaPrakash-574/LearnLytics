import pandas as pd
from datetime import datetime
import storage
import analytics

def start_quiz(subject,topic=None,difficulty=None,num_questions =5):
    Date = datetime.now().date().isoformat()
    subject = subject.lower().strip()
    if topic != None:
        topic = topic.lower().strip()
    if difficulty != None:
        difficulty = difficulty.lower().strip()
    if difficulty is None:
        difficulty = analytics.recommended_difficulty(subject)

    questions_df = storage.load_questions()
    
    if questions_df.empty:
        print("questions unavailable")
        return {}

    if subject not in questions_df["subject"].values:
        print("subject not available")
        return {}
    if topic != None:
        if topic not in questions_df["topic"].values:
            print("topic not available")
            return {}
    if difficulty != None:
        if difficulty not in questions_df["difficulty"].values:
            print("difficulty not available")
            return {}
    
    filtered_questions = questions_df[questions_df["subject"]== subject]
    if topic is not None:
        filtered_questions = filtered_questions[filtered_questions["topic"] == topic]
    if difficulty is not None:
        filtered_questions = filtered_questions[filtered_questions["difficulty"] == difficulty]

    if filtered_questions.empty:
        print("questions not available")
        return {}
    
    correct = 0 

    if len(filtered_questions) < num_questions:
        num_questions = len(filtered_questions)
        print(f"only {num_questions} questions avialable on you requirements")

    shuffled_questions= filtered_questions.sample(n=num_questions) 
    
    for row in shuffled_questions.itertuples():
        print(row.question)
        ans = input("Enter The Answer: ").lower().strip()

        if ans == row.answer:
            print("correct answer \n")
            correct+=1
        else:
            print("wrong answer \n")
            

    accuracy = (correct/num_questions)*100

    return {"date":Date,
            "subject":subject,
            "topic":topic,
            "total_questions":num_questions
            ,"correct":correct
            ,"wrong":num_questions-correct
            ,"accuracy":accuracy}

    


        






    
    

    

    

