import json
from constants import DAYS

FILE = "Tasks.json"

def Reading_tasks() -> dict:  
    
    try:
       with open (FILE, "r", encoding = "utf-8") as file:
        return json.load(file)
    
    except FileNotFoundError:
         return {day: [] for day in DAYS}
     
    except json.JSONDecodeError:
        return {day: [] for day in DAYS}
    
    
def save_tasks(tasks: dict) -> None:
    with open (FILE, "w", encoding = "utf-8" ) as file:
        json.dump(tasks, file, ensure_ascii= False, indent = 4)
        

