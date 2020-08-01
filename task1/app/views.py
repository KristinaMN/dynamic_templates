from django.shortcuts import render
from django.conf import settings
import csv

path_file = settings.INFLATION


def read_file(path):
    result = []
    with open(path, 'r', encoding='utf-8') as file:
        read = csv.reader(file, delimiter=';')
        for i in read:
            result.append(i)
    return result


def inflation_view(request):
    template_name = 'inflation.html'
    # чтение csv-файла и заполнение контекста
    file = read_file(path_file)
    table_title = file[0]
    table_data = file[1:]
    modify_float = [[float(i) if len(i) > 0 else '-' for i in one_list] for one_list in table_data]
    modify_int = [([int(float_list[0]), ] + float_list[1:]) for float_list in modify_float]
    return render(request, template_name,
                  context = {'table_t': table_title, 'table_data': modify_int})




