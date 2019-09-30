from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
import datetime as dt

def welcome(request):
    return render(request, 'welcome.html')


def convert_dates(dates):
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)
    days =['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', "Sunday"]
    
    # Returning the actual day of the week
    day =days[day_number]
    return day

def news_of_day(request):
    date = dt.date.today()
    return render(request, 'all-news/today-news.html', {'date':date})

def past_days_news(request, past_date):
    # Convert date from string the Url
    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        # Raise 404 when ValueError is thrown
        raise Http404()
    # day = convert_dates(date)
    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-news/past-news.html',{"date":date})