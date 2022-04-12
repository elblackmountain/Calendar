from datetime import datetime, timedelta
from meeting import Meeting


class Calendar:
    def __init__(self):
        self.meetings = {}

    def is_available(self, meeting_date: datetime):
        return meeting_date not in self.meetings

    def add_meeting(self, meeting: Meeting):
        if self.is_available(meeting.meeting_date):
            self.meetings[meeting.meeting_date] = meeting
        else:
            self.next_available(meeting.meeting_date)

    def next_available(self, date: datetime):
        # stworzenie zmiennej potencjalnej godziny spotkania
        # while - dopóki potencjalna godzina spotkania nie jest wolna
        # dodawaj po 1 h do potencjalnej h spotkania
        meeting_date = date
        while not self.is_available(meeting_date):
            # print("ten termin jest zajęty, może późniejsza godzina? ")
            meeting_date += timedelta(minutes=60)
            print(f'Ten termin jest już zajęty. Najbliższy wolny termin to {meeting_date}')
            return meeting_date




