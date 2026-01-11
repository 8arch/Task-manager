import json
from constants import DAYS

FILE = "Tasks.json"

def Reading_tasks() -> None | dict:  
    
    """ чтение сохраненых задач из файла """
    
    try:
       with open (FILE, "r", encoding = "utf-8") as file:
        return json.load(file)
    
    except FileNotFoundError:
         return {day: [] for day in DAYS}
        
    except json.JSONDecodeError:
        return {day: [] for day in DAYS}
    
    
def save_tasks(tasks: dict) -> None:
    
    """запись изменненых задач"""
    
    with open (FILE, "w", encoding = "utf-8" ) as file:
        json.dump(tasks, file, ensure_ascii= False, indent = 4)
        

