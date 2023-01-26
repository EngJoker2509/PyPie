from django.shortcuts import render, redirect
from .models import *
from django.db.models import Count


def dashboard(request):
    if not 'userid' in request.session:
        return redirect('/')
    if request.method == 'POST':
        name = request.POST['name']
        filling = request.POST['filling']
        crust = request.POST['crust']
        user_id = int(request.session['userid'])
        pypie.add_pypie(name, filling, crust, user_id)
        return redirect('/dashboard')
    else:
        user_id = int(request.session['userid'])
        context = {
            'pypie_by_user_id': pypie.display_pypie_by_user_id(user_id)
        }
        return render(request, 'dashboard.html', context=context)


def edit(request, id):
    if not 'userid' in request.session:
        return redirect('/')
    if request.method == 'POST':
        if pypie.objects.filter(id=id).exists():
            name = request.POST['name']
            filling = request.POST['filling']
            crust = request.POST['crust']
            user_id = int(request.session['userid'])
            pypie._update(id, name, filling, crust, user_id)
    return redirect('/dashboard')


def edit_pypie(request, id):
    if not 'userid' in request.session:
        return redirect('/')
    context = {
        'pypie': pypie.objects.get(id=id)
    }
    return render(request, 'edit_pypie.html', context=context)


def delete(request, id):
    if not 'userid' in request.session:
        return redirect('/')
    pypie._delete(id)
    return redirect('/dashboard')


def show(request, id):
    if not 'userid' in request.session:
        return redirect('/')
    context = {
        'show_pypie': pypie.objects.get(id=id)
    }
    return render(request, 'show.html', context=context)


def vote(request, id):
    if not 'userid' in request.session:
        return redirect('/')
    user_id = int(request.session['userid'])
    pypie.vote_thispypie_to_this_user(id, user_id)
    return redirect('/dashboard')


def add_pies(request):
    if not 'userid' in request.session:
        return redirect('/')
    all_pies = pypie.display_all_pies()
    number = []
    for pies in all_pies:
        count = [pies.id, pypie.objects.get(id=pies.id).vote.all().count()]
        number.append(count)
    context = {
        'all_pies': pypie.display_all_pies(),
        'number': number
    }
    return render(request, 'dispaly_pies.html', context=context)


def destroy(request):
    del request.session['userid']
    return redirect('/')
