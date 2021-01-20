import pandas as pd

data = pd.read_csv('movie_bd_v5.csv')
data.describe()
print(data.info())  # Проверяем, есть ли пропуски в данных

answers = {}  # создадим словарь для ответов

data['profit'] = data['revenue'] - data['budget']  # Добавление колонки с прибылью
data['len_title'] = data['original_title'].apply(lambda x: len(x))  # Добавление колонки с длиной названия фильма

# разделение данных в колонках с несколькими строковыми значениями

data['genres'] = data['genres'].str.split('|')
data['cast'] = data['cast'].str.split('|')
data['director'] = data['director'].str.split('|')
data['production_companies'] = data['production_companies'].str.split('|')
data['words_in_overview'] = data['overview'].apply(lambda x: len(x.split(' ')))


def month(x):
    """Функция для преобразования номера месяца (из типа str) в название месяца"""
    if x == '1':
        return 'January'
    elif x == '2':
        return 'February'
    elif x == '3':
        return 'March'
    elif x == '4':
        return 'April'
    elif x == '5':
        return 'May'
    elif x == '6':
        return 'June'
    elif x == '7':
        return 'July'
    elif x == '8':
        return 'August'
    elif x == '9':
        return 'September'
    elif x == '10':
        return 'October'
    elif x == '11':
        return 'November'
    else:
        return 'December'


data['month'] = data['release_date'].str.split('/').apply(
    lambda x: month(x[0]))  # Добавление колонки с названием месяца

var = data[data['budget'] == data['budget'].max()]['original_title']

answers['1'] = data[data['budget'] == data['budget'].max()].original_title.iloc[0]  # "+"
