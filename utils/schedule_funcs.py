import datetime
import json
import requests
sys.path.insert(1, '/*MyPath*/code/utils/')

import group_funcs

PERSONAL_SCHEDULES = {}


class Lesson:
    '''Class containing info about one lesson'''
    forms = {
        0: 'практическое занятие',
        1: 'лабораторная работа',
        2: 'лекция',
        3: 'семинар',
        4: 'консультация',
        5: 'внеучебное занятие',
        6: 'зачет',
        7: 'экзамен',
        8: 'доп. экзамен'
    }

    def __init__(self, api_response: dict):
        # Implement response parsing
        self.name = api_response['subject']
        self.time = api_response['time_start'] + '-' + api_response['time_end']
        self.form = api_response['type']
        self.groups = []
        for group in api_response['groups']:
            self.groups.append(group['name'])
        teachers = api_response['teachers']
        if teachers is not None:
            self.teacher = teachers[0]['full_name']
        else:
            self.teacher = 'Неизвестен'
        auditory = api_response['auditories'][0]
        self.location = auditory['name'] + ', ' + auditory['building']['name']

    def __str__(self) -> str:
        representation = '{}\n'.format(self.name)
        representation += 'Время: {}\n'.format(self.time)
        representation += '{}\n'.format(Lesson.forms[self.form])
        groups_str = ''
        for group in self.groups[:-1]:
            groups_str += group + ', '
        groups_str += self.groups[-1]
        representation += 'Группы: {}\n'.format(groups_str)
        representation += 'Преподаватель: {}\n'.format(self.teacher)
        representation += 'Аудитория {}'.format(self.location)
        return representation


class Schedule:
    def __init__(self, group_id: int):
        # Implement response parsing
        self.group_id = group_id
        self.update()

    def ensure_up_to_date(self):
        if datetime.datetime.today().date() - self.week_end > datetime.timedelta(days=0):
            self.update()

    def update(self):
        '''Reinitialize self variables on creation or in case they get outdated'''
        # TODO: upon api_link separation from code replace with smth uniform
        self.week = {}
        response = requests.get('http://ruz.spbstu.ru/api/v1/ruz/scheduler/' + str(self.group_id))
        days = json.loads(response.text)['days']
        week = json.loads(response.text)['week']
        self.week_end = datetime.date(*list(map(int, week['date_end'].split('.'))))

        for day in days:
            day_str = day['date']
            # Split date string by '-' to get smth like '2019-12-17' -> ['2019','12','17']
            # Map int to this sequence and pass result to create dateobject
            date = datetime.date(*list(map(int, day_str.split('-'))))
            one_day_lessons = []
            for lesson in day['lessons']:
                one_day_lessons.append(Lesson(lesson))
            self.week[date] = one_day_lessons

    def day_to_str(self, date: str) -> str:
        '''Returns string representation of a single day'''
        out_string = ''
        for lesson in self.week[date]:
            out_string += str(lesson) + '————————————————————————\n'
        return out_string

    def get_today(self):
        '''Returns a single day'''
        self.ensure_up_to_date()
        today = datetime.datetime.today().date()
        for day in self.week:
            if day == today:
                return today

    def for_today(self) -> str:
        '''Returns a string with today's schedule'''
        today = self.get_today()
        return self.day_to_str(date=today)

    def count_lessons_today(self) -> int:
        '''Returns amount of lessons for today'''
        today = self.get_today()
        return len(self.week[today])

    def for_current_week(self):
        '''Returns string represenation of a schedule for a week'''
        if not self.ensure_up_to_date():
            self.update()
        return str(self)

    def save_offline(self):
        '''Saves schedule offline for later cached access'''
        raise NotImplementedError

    def __str__(self):
        out_string = ''
        for day in sorted(self.week):
            out_string += '\n' + str(day) + '\n'
            out_string += self.day_to_str(day)
        return out_string


def personal_schedule(user_id: int) -> Schedule:
    '''Get group id by user id'''
    # KeyError may be risen here, but to be processed in bot's main file
    group_id = group_funcs.GROUP_IDS[group_funcs.USER_GROUPS[user_id]][1]
    return PERSONAL_SCHEDULES[group_id]


def update_schedule_list(group_id: int):
    '''Ensures a schedule exists for specified group'''
    if group_id not in PERSONAL_SCHEDULES.keys():
        PERSONAL_SCHEDULES[group_id] = Schedule(group_id)
