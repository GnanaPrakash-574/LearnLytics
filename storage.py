import json
import pandas as pd 
import quiz

def load_questions():      # JSON --> DICTIONARY --> DATAFRAME
    try:
        with open('data/questions.json',encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("file not found")
        return pd.DataFrame()
    except json.JSONDecodeError:
        print("invalid json file")
        return pd.DataFrame()
    
    
    #converting to dataframe

    return pd.DataFrame(data)
    

def load_performance():
    try:
        with open('data/performance.json', encoding='utf-8') as f:
            raw_data = json.load(f)
    except FileNotFoundError:
        print("file not found")
        return pd.DataFrame()
    except json.JSONDecodeError:
        print("invalid json file")
        return pd.DataFrame()

    return pd.DataFrame(raw_data)
    

def save_performance(result):
    try:
        with open('data/performance.json', encoding='utf-8') as f:
            raw_data = json.load(f)
    except FileNotFoundError:
        print("file not found")
        raw_data=[]
    except json.JSONDecodeError:
        print("invalid json file")
        raw_data=[]
    
    raw_data.append(result)

    with open('data/performance.json','w', encoding='utf-8') as f:
        json.dump(raw_data,f,indent=4)

    
    
    





    
     


    


