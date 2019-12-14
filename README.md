# Schedule SPbSTU telegram bot

Телеграм бот для получения расписания студентам СПбПУ

<img src="https://github.com/LeonidVolohov/telebot_poly_schedule/blob/master/screenshot/schedule_logo.png" align="right"
     title="Polytech schedule logo">

## Описание проекта

Как часто студенты спешат на пару и им нужно быстро посмотреть информацию о следующей паре? По своему личному опыту знаю, что очень часто. Благодаря этому боту можно за одну команду узнать основную информацию о следующей паре или о целом учебном дне

### Требования к проекту

* Выбор любой группы с [сайта с расписанием](http://ruz.spbstu.ru/)
* Показ расписания для текущего дня
* Количество предметов за день
* Названия следующей пары

### Аудитория бота

* Студенты и сотрудники СПбПУ
* Абитуриенты

### Используемные инструменты для написания

* python3.7
* pyTelegramBotApi
* python requests module
* python BeautifulSoup module
* python datetime module
* python html module

### Установка инструментов

```
sudo apt-get install python3.7
```

```
pip install pyTelegramBotAP
```

```
pip install requests
```

```
pip install BeautifulSoup
```

```
pip install datetime
```

```
pip install html
```

## Примеры запуска

* Стартовое сообщение

![Start message](https://github.com/LeonidVolohov/telebot_poly_schedule/blob/master/screenshot/start_message.png)

* Сообщение о предментах за текущий день

![Lessons](https://github.com/LeonidVolohov/telebot_poly_schedule/blob/master/screenshot/lessons.png)

* Сообщение о количестве предметах за день

![Count lessons](https://github.com/LeonidVolohov/telebot_poly_schedule/blob/master/screenshot/count_lessons.png)


## Тестирование

*TODO: Добавить тестирование*

## Авторы

[Волохов Леонид](https://github.com/LeonidVolohov)
[Крамаров Евгений](https://github.com/kramarov-evg)


