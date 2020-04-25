import _datetime

from sandra.handler.handler import Handler

class DateTimeHandler(Handler):
    HANDLER_PATTERN = "(.*?)(time|date)(.*?)"

    def __init__(self):
        super().__init__()

    def __suffix(self, d):
        return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')

    def __custom_strftime(self, format, t):
        return t.strftime(format).replace('{S}', str(t.day) + self.__suffix(t.day))

    def handle(self, command):
        date_command, time_command, conjunction = "", "", ""
        now = _datetime.datetime.now()
        if 'date' in command:
            date_command = self.__custom_strftime('Todays date is %B {S}, %Y', now)
        if 'time' in command:
            time_command = "the time is " + now.strftime("%-I:%M %p")
        if date_command and time_command:
            conjunction = " and "
        return "%s%s%s" % (date_command, conjunction, time_command)
