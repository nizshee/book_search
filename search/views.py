from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def find_city(request, city_name):
    return JsonResponse({'list' : city_by_prefix(city_name)})

def find_book(request, city_name):
    return JsonResponse({'list' : book_by_city(city_name)})


def city_by_prefix(name):
    res = filter(lambda x: x.lower().startswith(name.lower()), cities)
    return [i for i, j in zip(res, range(20))]
cities = ["London", "Paris", "Berlin", "Moscow", "Tokyo", "Tomsk"]

def book_by_city(name):
    return list(map(lambda x: {"title" : name + x["title"], "quote" : x["quote"]}, books))

books = [
    {
    "title" : "1",
    "quote" : 
"""Secondary line text Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Nam massa quam. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. 
Quisque volutpat condimentum velit. 
Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos."""
    },
    {
    "title" : "2",
    "quote" : 
"""Secondary line text Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Nam massa quam. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. 
Quisque volutpat condimentum velit. 
Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos."""
    },
    {
    "title" : "3",
    "quote" : 
"""Secondary line text Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Nam massa quam. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. 
Quisque volutpat condimentum velit. 
Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos."""
    },
    {
    "title" : "4",
    "quote" : 
"""Secondary line text Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Nam massa quam. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. 
Quisque volutpat condimentum velit. 
Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos."""
    },
    {
    "title" : "5",
    "quote" : 
"""Secondary line text Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Nam massa quam. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. 
Quisque volutpat condimentum velit. 
Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos."""
    },
    {
    "title" : "6",
    "quote" : 
"""Secondary line text Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Nam massa quam. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. 
Quisque volutpat condimentum velit. 
Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos."""
    },
    {
    "title" : "7",
    "quote" : 
"""Secondary line text Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Nam massa quam. Nulla metus metus, ullamcorper vel, tincidunt sed, euismod in, nibh. 
Quisque volutpat condimentum velit. 
Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos."""
    }
]