from slugify import slugify
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Room, Message
from .forms import RoomCreateForm
from django.contrib import messages


@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/rooms.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)

    return render(request, 'room/room.html', {'room': room, 'messages': messages})

@login_required
def room_create(request):
    if request.method == 'POST':
        all_rooms = Room.objects.all()

        all_rooms_slugs = []
        for room in all_rooms:
            all_rooms_slugs.append(room.slug)

        form = RoomCreateForm(request.POST)
        if form.is_valid():
            new_room = form.save(commit=False)
            new_room.slug = slugify(form.data['name'])
            if new_room.slug in all_rooms_slugs:
                messages.error(request, f'Room "{new_room.slug}" is exists')
                return redirect('new_room')
            else:
                new_room.save()
                return  redirect('room', slug=new_room.slug)
    else:
        form = RoomCreateForm()

    return render(request, 'room/new_room.html', {'form': form})