from icalendar import Calendar, Event, vCalAddress, vText
import pytz
from datetime import datetime
import os
from pathlib import Path

dates = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}
cal = Calendar()

with open('modern tools stuff/tesseract2.txt') as f:
    for line in f:
        month, day, *summary = line.strip().split()
        summary = ' '.join(summary)
        month = dates[month]
        day = int(day)
        print(summary, month, day)

        event = Event()
        event.add('summary', summary)
        event.add('dtstart', datetime(2022, month, day, tzinfo=pytz.utc))
        event.add('dtend', datetime(2022, month, day, tzinfo=pytz.utc))
        cal.add_component(event)


f = open('modern tools stuff/example3.ics', 'wb')
f.write(cal.to_ical())
f.close
