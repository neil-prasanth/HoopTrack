from django.shortcuts import render, redirect
from django.db.models import Q
from .models import PlayerStat
from .forms import PlayerStatForm


def home(request):
    if request.method == 'POST':
        form = PlayerStatForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PlayerStatForm()

    players = PlayerStat.objects.all().order_by('-game_date')

    search = request.GET.get('search', '')

    if search:
        players = players.filter(
            Q(player_name__icontains=search) |
            Q(team__icontains=search)
        )

    return render(request, 'tracker/home.html', {
        'form': form,
        'players': players,
        'search': search,
    })