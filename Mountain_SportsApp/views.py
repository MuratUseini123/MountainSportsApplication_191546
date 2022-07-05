from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def mountain_sports_user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('starting_page')
        else:
            return redirect('login')

    context = {"logged_user": request.user.username.__str__()}
    return render(request, 'login.html', context=context)


@login_required(login_url='login')
def startingPage(request):
    context = {"logged_user": request.user.username.__str__()}
    return render(request, 'starterPage.html', context=context)


def mountain_sports_user_logout(request):
    logout(request)
    return redirect('login')


def weather_now(request):
    context = {"logged_user": request.user.username.__str__()}
    return render(request, 'weather_now.html', context=context)


def trips_page(request):
    context = {"logged_user": request.user.username.__str__()}
    return render(request, 'trips_page.html', context=context)


def learning_section(request):
    context = {"logged_user": request.user.username.__str__()}
    return render(request, 'learning_section.html', context=context)


def discoverMore_section(request):
    context = {"logged_user": request.user.username.__str__()}
    return render(request, 'discover_more.html', context=context)
