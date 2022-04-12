from datetime import datetime


class Meeting:
    def __init__(self, meeting_date: datetime, title:str):
        self.title = title
        self.meeting_date = meeting_date
