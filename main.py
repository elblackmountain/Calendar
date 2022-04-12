from meeting import Meeting
from cal import Calendar
from datetime import datetime
from json import dump, load


calendar = Calendar()

with open("Meetings.json",encoding="utf8") as file:
    data = load(file)
    for item in data:
        meeting = Meeting(
            datetime.strptime(item['date'], '%Y-%m-%d %H:%M'),
            item['title'])
        calendar.add_meeting(meeting)

if __name__ == '__main__':
    while True:
        option = input('Co chcesz zrobić - L - lista, D - dodaj, Q - wyjdź ')
        if option in ('L','l'):
            for _, meeting in calendar.meetings.items():
                print(f'{meeting.meeting_date} : {meeting.title}')
        elif option in('D', 'd'):
            title = input('Tytuł: ')
            meeting_date = datetime.strptime(input('Data spotkania yyyy-mm-dd hh:mm '), '%Y-%m-%d %H:%M')
            calendar.add_meeting(Meeting(meeting_date, title))

            with open('Meetings.json', 'w') as file:
                data = []
                for meeting in calendar.meetings.values():
                    data.append({
                        'title': meeting.title,
                        'date': datetime.strftime(meeting_date,'%Y-%m-%d %H:%M')})
                dump(data, file)

        elif option in ('Q', 'q'):
            break
        else:
            print('Nie rozumiem')


