import datetime
import pars_file

def print_today(week):
    time = datetime.datetime.today()

    out_string = lesson_string = ''
    split_string = '————————————————————————\n'

    for key in week.keys():
        #09 == 09    
        if str(key)[0:2] == str(time)[8:10]:
            for subject in week[key]:
                subject_name = subject 
                subject_time = week[key][subject][0]
                subject_type = week[key][subject][1]
                subject_teacher = week[key][subject][2]
                subject_place = week[key][subject][3]
                
                lesson_string += 'Предмет: ' + subject_name + '\n' + 'Время: ' + subject_time + '\n' + 'Тип: ' + subject_type + '\n' + 'Препод: ' + subject_teacher + '\n' + 'Где: ' + subject_place + '\n'
                out_string += lesson_string + split_string
                
                subject_name = subject_type  = subject_teacher = lesson_string = ''

    return out_string

def lessons_in_day(week):
    time = datetime.datetime.today()

    count = 0
    
    for key in week.keys():    
        if str(key)[0:2] == str(time)[8:10]:
            for subject in week[key]:
                count += 1

    if count > 2:
        out_string = 'Сегодня ' + str(count) + ' пары(((' + '\n'
    else:
        out_string = 'Сегодня ' + str(count) + ' пары)' + '\n'
    return out_string


def main():
    text = pars_file.get_html_file(95, 27651)
    week = pars_file.schedule_week(text)

    print(print_today(week))
    print(lessons_in_day(week))
    
if __name__ == '__main__':
    main()    
    