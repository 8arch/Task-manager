
def valid_task(tasks, vers_add: bool) -> set:
    
    normalized = set()
    
    for name in tasks:
            if isinstance(name, str):
                name = name.strip()
                if name != "":
                    if vers_add:
                       normalized.add(name)
                    if not vers_add:
                        normalized.add(name.lower())
            
    return normalized


def valid_day(day: str) -> str:
    day = day.strip()
    day = day.lower()
    return day


def checking_for_issues(tasks: dict[str, list: [dict]], full_result = False) -> bool | dict:
    len_tasks = {}
    for day in tasks:
        len_tasks[day] = len(tasks[day])
    
    if len_tasks:
        return len_tasks
    
    if not full_result:
        return any(x for x in len_tasks if x > 0)