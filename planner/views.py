from django.shortcuts import render, redirect
from .data import COUNTRIES, TOUR_TYPES, LANGUAGES

def index(request):
    theme = request.COOKIES.get("theme", "light")
    lang = request.COOKIES.get("lang", "ru")
    last_country = request.COOKIES.get("last_country", "")

    context = {
        "countries": COUNTRIES,
        "tour_types": TOUR_TYPES,
        "languages": LANGUAGES,
        "theme": theme,
        "lang": lang,
        "last_country": last_country,
    }
    return render(request, "planner/index.html", context)

def save_preferences(request):
    if request.method == "POST":
        theme = request.POST.get("theme", "light")
        lang = request.POST.get("lang", "ru")
        # Получаем ID страны, а не название (чтобы не было ошибки с русскими буквами)
        country_id = request.POST.get("country", "")

        response = redirect("planner:index")
        
        # Сохраняем в куки на 30 дней
        response.set_cookie("theme", theme, max_age=2592000)
        response.set_cookie("lang", lang, max_age=2592000)
        response.set_cookie("last_country", country_id, max_age=2592000)
        
        return response
    return redirect("planner:index")

def reset_preferences(request):
    response = redirect("planner:index")
    response.delete_cookie("theme")
    response.delete_cookie("lang")
    response.delete_cookie("last_country")
    return response

def countries_list(request):
    theme = request.COOKIES.get("theme", "light")
    lang = request.COOKIES.get("lang", "ru")
    return render(request, "planner/countries.html", {
        "countries": COUNTRIES,
        "lang": lang,
        "theme": theme,
    })