import requests
from bs4 import BeautifulSoup
from lxml import html

def get_html_file(faculty, group):
    url = 'http://ruz.spbstu.ru/faculty/%d/groups/%d' % (faculty, group)
    r = requests.get(url)
    return r.text

def schedule_week(text):
    
    schedule_week_dict = {} # {date : {subject : [time, type, groups, teacher, place]}}
    subject_dict = {}       # {subject : [time, type, groups, teacher, place]}

    soup = BeautifulSoup(text, 'lxml')

    week = soup.find_all('li', {'class','schedule__day'})

    for day in week:
        subject_dict = {}
        day_list = []
        lessons = day.find_all('li', {'class', 'lesson'})
        date = day.find('div', {'class': 'schedule__date'}).text
        for lesson in lessons:

            subject_name = ''

            #subject in day, it comes from a site like --- lesson_time lesson_name. We have to split it up 
            lesson_subject = lesson.find('div', {'class', 'lesson__subject'}).text

            for i in range(len(lesson_subject.split())):
                subject_time = lesson_subject.split()[0]
                if i > 0:
                    subject_name += lesson_subject.split()[i] + ' '

            #subject type: lecture / practice
            subject_type = lesson.find('div', {'class', 'lesson__type'}).text

            #subject teacher
            subject_teacher = lesson.find('div', {'class', 'lesson__teachers'})
            if subject_teacher == None:
                subject_teacher = 'Но преподо ин сайто'
            else:
                subject_teacher = subject_teacher.text

            #lesson place
            subject_place = lesson.find('div', {'class', 'lesson__places'}).text

            day_list.extend((subject_time, subject_type, subject_teacher, subject_place))
            subject_dict[subject_name] =  day_list
            day_list = []

        schedule_week_dict[date] =  subject_dict
    
    return schedule_week_dict

def main():
    text = get_html_file(95, 27651)
    week = schedule_week(text)

    curr_day = '09 окт., ср'
    for subject in week[curr_day]:
        print(subject)
        for subject_param in week[curr_day][subject]:
            print(subject_param)

if __name__ == '__main__':
    main()
