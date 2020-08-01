from django import template
from datetime import datetime


register = template.Library()


@register.filter
def format_date(value):
    # Ваш код
    if isinstance(value, float) or isinstance(value, int):
        total_date = (datetime.now() - datetime.fromtimestamp(value))
        if total_date.total_seconds() < 60*10+6000:
            return "Только что"
        elif total_date.total_seconds() < 60*60*24:
            hours = int(total_date.total_seconds()//3600)
            if (str(hours)[-1:] == '1') and (str(hours)[-2:-1] != '1'):
                text_hours = 'час'
            elif (str(hours)[-1:] in '234') and (str(hours)[-2:-1] != '1'):
                text_hours = 'часа'
            else:
                text_hours = 'часов'
            return f'{hours} {text_hours} назад'
        else:
            return datetime.fromtimestamp(value).strftime('%Y-%m-%d')
    else:
        return value

@register.filter
def format_selftext(text, count):
    if isinstance(text, str) and isinstance(count, int):
        lst = text.split()
        format_txt = ''
        if len(lst) > count*2:
            format_txt = ' '.join(lst[:count])+' ... '+' '.join(lst[-count:])
        elif len(lst) > 0:
            format_txt = text
        return format_txt


# необходимо добавить фильтр для поля `score`

@register.filter
def format_score(value):
    score = 'Скоро узнаем'
    if isinstance(value, int):
        if value < -5:
            score = 'Всё плохо'
        elif value <= 5:
            score = 'Нейтрально'
        elif value > 5:
            score = 'Хорошо'
    return score


@register.filter
def format_num_comments(value):
    if isinstance(value, int):
        if value > 50:
            return '50+'
        elif value > 0:
            return value
        return 'Оставьте комментарий'



