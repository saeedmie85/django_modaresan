from . import jalali
from django.utils import timezone


def english_number_to_persian(date):
    numbers = {
        "0": "۰",
        "1": "۱",
        "2": "۲",
        "3": "۳",
        "4": "۴",
        "5": "۵",
        "6": "۶",
        "7": "۷",
        "8": "۸",
        "9": "۹",
    }
    for k,v in numbers.items():
        date = date.replace(k,v)
    return date


def jalali_convertor(time):
    time = timezone.localtime(time)
    jalali_month = [
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند",
    ]
    time_to_str = f"{time.year},{time.month},{time.day}"
    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()
    time_to_list = list(time_to_tuple)
    for index, month in enumerate(jalali_month):
        if time_to_list[1] == index + 1:
            time_to_list[1] = month
    output = f"{time_to_list[2]} {time_to_list[1]} {time_to_list[0]} ساعت {time.hour}:{time.minute}"
    return english_number_to_persian(output)
