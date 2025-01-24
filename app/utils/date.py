from datetime import datetime

class DateManager:
    @staticmethod
    def get_today_date():
        now = datetime.now().date()
        months = [
        'janvier', 'février', 'mars', 'avril', 'mai', 'juin', 
        'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'
        ]
        return f"{now.day} {months[now.month - 1]} {now.year}"
    
    @staticmethod
    def check_time_difference(date1:datetime, date2:datetime):
        return date1 - date2

    @staticmethod
    def get_now_date():
        # strftime = string format time. Convertit un objet datetime en str
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # strptime = string parse time. Convertit la chaine formatée en objet datetime
        return  datetime.strptime(now, "%Y-%m-%d %H:%M:%S")
    