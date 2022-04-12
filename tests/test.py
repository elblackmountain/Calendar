from meeting import Meeting
from datetime import datetime
from cal import Calendar


def test_add_meeting():
    calendar = Calendar()
    meeting1 = Meeting(datetime(2021, 5, 11, 10), 'Pierwsze')
    meeting2 = Meeting(datetime(2021, 5, 11, 11), 'Drugie')
    meeting3 = Meeting(datetime(2021, 5, 11, 12), 'Trzecie')
    calendar.add_meeting(meeting1)
    calendar.add_meeting(meeting2)
    calendar.add_meeting(meeting3)
    assert len(calendar.meetings) == 3


def test_add_2_meetings_at_the_same_time():
    calendar = Calendar()
    meeting1 = Meeting(datetime(2021, 5, 11, 10, 30), 'Pierwsze')
    meeting2 = Meeting(datetime(2021, 5, 11, 10, 30), 'Drugie')
    calendar.add_meeting(meeting1)
    calendar.add_meeting(meeting2)
    assert len(calendar.meetings) == 1


def test_next_available():
    calendar = Calendar()
    meeting1 = Meeting(datetime(2021, 5, 11, 10), 'Pierwsze')
    meeting2 = Meeting(datetime(2021, 5, 11, 11), 'Drugie')
    meeting3 = Meeting(datetime(2021, 5, 11, 12), 'Trzecie')
    calendar.add_meeting(meeting1)
    calendar.add_meeting(meeting2)
    calendar.add_meeting(meeting3)
    next_time_slot = calendar.next_available(datetime(2021, 5, 11, 10))
    assert next_time_slot == (datetime(2021, 5, 11, 11))


def test_is_given_datetime_is_available():
    calendar = Calendar()
    meeting1 = Meeting(datetime(2021, 5, 11, 10), 'Pierwsze')
    meeting2 = Meeting(datetime(2021, 5, 11, 11), 'Drugie')
    calendar.add_meeting(meeting1)
    calendar.add_meeting(meeting2)

    assert calendar.is_available(datetime(2021, 5, 11, 12)) == True
