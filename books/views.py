from django.shortcuts import render
from django.http import HttpResponse
import datetime
import random

def about_me(request):
    return HttpResponse("<h1>О себе</h1><p>Меня зовут Нурсеит. И я очень ленивая жопа!</p>")

def current_time(request):
    time_set = "12:00"
    spl = int(time_set.split(":"))
    hour = spl[0]
    if hour < 12:
        message = "Сейчас утро"
    elif 12 <= hour <= 14:
        message = "Сейчас обед"
    elif 15 <= hour <= 20:
        message = "Сейчас вечер"
    else:
        message = "Сейчас ночь"

    return HttpResponse(f"<h1>{message}</h1><p>Текущее время: {time_set}</p>")


def random_quote(request):
    quotes = [
        "Не откладывай на завтра то, что можно сделать сегодня. – Бенджамин Франклин",
        "Воображение важнее знания. – Альберт Эйнштейн",
        "Жизнь — это то, что с тобой происходит, пока ты строишь планы. – Джон Леннон",
        "Чтобы жить, нужно быть готовым к риску. – Эрнест Хемингуэй",
        "Пиши так, как будто никто не читает. – Эрнест Хемингуэй",
        "Чтение – это умение слушать с глазами. – Френсис Бэкон",
        "Слова – это инструмент, который может менять мир. – Вольтер",
        "Книги — корабли мысли, странствующие по волнам времени. – Фрэнсис Бэкон"
    ]
    return HttpResponse(f"<h1>Случайная цитата</h1><p>{random.choice(quotes)}</p>")