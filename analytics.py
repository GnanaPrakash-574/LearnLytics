import storage
import pandas as pd
from datetime import date, timedelta

def overall_stats():
    performance = storage.load_performance()

    if performance.empty:
        return[0,0,0,0]
    tot_quizzes = len(performance)  # total quizzes
    
    tot_correct = 0
    tot_wrong = 0
    for rows in performance.itertuples():    #  for total no.of corrects and wrongs  and directly we can use performance["correct"].mean() function instead of looping
        tot_correct += rows.correct
        tot_wrong += rows.wrong

    avg_accuracy = performance["accuracy"].mean()  # for accuracy measuring

    print(f"Total no.of Quizzes Taken : {tot_quizzes} \n Total no.of Questions Answered Correctly : {tot_correct} \n"  +
          f"Total no.of Questions Answered Wrongly : {tot_wrong} \n Total Overall Average Accuracy : {avg_accuracy}")
    
    return [tot_quizzes,tot_correct,tot_wrong,avg_accuracy]

def all_subjects_performance():
     
    performance = storage.load_performance()

    if performance.empty:
        return None

    print(performance.groupby("subject")["accuracy"].mean())

    return performance.groupby("subject")["accuracy"].mean()

def subject_performance(subject,topic = None):
    performance = storage.load_performance() 

    if performance.empty:
        return None
    
    subject = subject.lower().strip()
    if topic is not None:
        topic = topic.lower().strip()

    if subject not in performance["subject"].values:
        print("subject not available")
        return None
    if topic != None:
        if topic not in performance["topic"].values:
            print("topic not availablle")
            return None
    
    filtered_performance = performance[performance["subject"] == subject]
    if topic is not None:
        filtered_performance = filtered_performance[filtered_performance["topic"] == topic]

    if filtered_performance.empty:
        print("performance data not available")
        return None

    print(f"subject : {subject} \n topic : {topic} \n accuracy: {filtered_performance["accuracy"].mean()}")

    return [subject,topic,filtered_performance["accuracy"].mean()]

def most_attempted_subject():
    
    performance = storage.load_performance()
    if performance.empty:
        return None

    filtered_performance = performance["subject"].value_counts()

    print(f"most attempted subject : {filtered_performance.idxmax()}")
    print(f"Attempts : {filtered_performance.max()}")

    return [filtered_performance.idxmax(),filtered_performance.max()]

def best_subject():

    performance = storage.load_performance()
    if performance.empty:
        return [None,0]

    subject_accuracy = performance.groupby("subject")["accuracy"].mean()

    print(f"Best Subject Is {subject_accuracy.idxmax()} with Accuracy {subject_accuracy.max()}")
    return [subject_accuracy.idxmax(),subject_accuracy.max()]

def weak_subject():

    performance = storage.load_performance()
    if performance.empty:
        return [None,0]

    subject_accuracy = performance.groupby("subject")["accuracy"].mean()

    print(f"Weakest Subject Is {subject_accuracy.idxmin()} with Accuracy {subject_accuracy.min()}")
    return [subject_accuracy.idxmin(),subject_accuracy.min()]

def recommended_difficulty(subject):
    
    performance = storage.load_performance()
    if performance.empty:
        return None
    subject = subject.lower().strip()

    if performance.empty:
        return None
    if subject not in performance["subject"].values:
        return None

    filtered_subject= performance[performance["subject"] == subject]

    if filtered_subject.empty:
        print("no entry recorded on that subject")
        return None
    
    subject_accuracy = filtered_subject["accuracy"].mean()

    if subject_accuracy >= 80:
        return "hard"
    elif 80>subject_accuracy>=40:
        return "medium"
    else:
        return "easy"
    
def topics_strenght(level):
    performance = storage.load_performance()

    if performance.empty:
        return None
    
    topic_accuracy = performance.groupby("topic")["accuracy"].mean()

    if topic_accuracy.empty:
        return None
    weak_topics = topic_accuracy[topic_accuracy<=40]
    strong_topics = topic_accuracy[topic_accuracy>=80]

    if level == "strong":
        if strong_topics.empty:
            return None
        return strong_topics
    elif level == "weak":
        if weak_topics.empty:
            return None
        return weak_topics

def study_streak():
    streak  = 0 
    performance = storage.load_performance()

    if performance.empty:
        return 0
    
    dates = pd.to_datetime(performance["date"]).dt.date.unique()
    dates = set(dates)
    current_day = date.today()

    while current_day in dates:
        streak +=1
        current_day -= timedelta(days=1)

    return streak


def overall_accuracy_trend():
    performance = storage.load_performance()

    if performance.empty:
        return None
    
    daily_accuracy=(performance.groupby("date")["accuracy"].mean().sort_index())

    return daily_accuracy