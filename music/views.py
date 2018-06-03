from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
# from .forms import AlbumForm, SongForm, UserForm
from .forms import SongForm
from .forms import UserForm
from .models import Subject, File, Forum, Question
from students.models import User

# file_TYPES = ['wav', 'mp3', 'ogg']
# IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


# def create_album(request):
#     if not request.user.is_authenticated():
#         return render(request, 'music/login.html')
#     else:
#         form = AlbumForm(request.POST or None, request.FILES or None)
#         if form.is_valid():
#             album = form.save(commit=False)
#             album.user = request.user
#             album.logo = request.FILES['logo']
#             file_type = album.logo.url.split('.')[-1]
#             file_type = file_type.lower()
#             if file_type not in IMAGE_FILE_TYPES:
#                 context = {
#                     'album': album,
#                     'form': form,
#                     'error_message': 'Image file must be PNG, JPG, or JPEG',
#                 }
#                 return render(request, 'music/create_album.html', context)
#             album.save()
#             return render(request, 'music/detail.html', {'album': album})
#         context = {
#             "form": form,
#         }
#         return render(request, 'music/create_album.html', context)


def create_song(request, album1_id):
    form = SongForm(request.POST or None, request.FILES or None)
    album = get_object_or_404(Forum, pk=album1_id)
    if form.is_valid():
        albums_songs = album.question_set.all()
        for s in albums_songs:
            if s.name == form.cleaned_data.get("name"):
                context = {
                    'album': album,
                    'form': form,
                    'error_message': 'You already added that song',
                }
                return render(request, 'music/create_song.html', context)
        song = form.save(commit=False)
        song.forum = album
        song.user = request.user
        # song.file = request.FILES['file']
        # file_type = song.file.url.split('.')[-1]
        # file_type = file_type.lower()
        # if file_type not in file_TYPES:
        # context = {
        #     'album': album,
        #     'form': form,
        #     # 'error_message': 'Audio file must be WAV, MP3, or OGG',
        # }
        # return render(request, 'music/create_song.html', context)

        song.save()
        questions = album.question_set.filter(user=request.user)
        return render(request, 'music/detail3.html', {'album': album, 'questions': questions})
    context = {
        'album': album,
        'form': form,
    }
    return render(request, 'music/create_song.html', context)


# def delete_album(request, album_id):
#     album = Album.objects.get(pk=album_id)
#     album.delete()
#     albums = Album.objects.filter(user=request.user)
#     return render(request, 'music/index.html', {'albums': albums})


def delete_song(request, album1_id, song_id):
    album = get_object_or_404(Forum, pk=album1_id)
    song = Question.objects.get(pk=song_id)
    song.delete()
    questions = album.question_set.filter(user=request.user)
    return render(request, 'music/detail3.html', {'album': album, 'questions': questions})


def detail(request, album_id):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        user = request.user
        album = get_object_or_404(Subject, pk=album_id)
        return render(request, 'music/detail.html', {'album': album, 'user': user})

def detail1(request, album1_id):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        user = request.user
        album = get_object_or_404(Forum, pk=album1_id)
        # album = Forum.objects.filter(user=request.user, pk=album1_id)
        # album = Question.objects.filter(album__id = album1_id)

        return render(request, 'music/detail1.html', {'album': album, 'user': user})

def detail3(request, album1_id):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        user = request.user
        album = get_object_or_404(Forum, pk=album1_id)
        # album = Forum.objects.get(pk=album1_id)
        # album = Question.objects.filter(album__id = album1_id)
        # questions = Question.objects.filter(user = request.user)
        questions = album.question_set.filter(user=request.user)
        # questions = album.question_set.all()
        # questions = album.question_set.all()
        # questions = questions.filter(user = request.user)
        return render(request, 'music/detail3.html', {'album': album, 'questions': questions, 'user': user})

def detail2(request, album2_id):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        user = request.user
        song = get_object_or_404(Question, pk=album2_id)
        # album = get_object_or_404(Question, pk=album2_id)

        # song = Question.objects.get(pk=album2_id)
        # album = Question.objects.get(name = request.user.quest.name)
        # album = Question.objects.filter(user=user)



        # album = Question.objects.fiter(user = request.user)

        return render(request, 'music/detail2.html', {'song': song, 'user': user})
# def favorite(request, song_id):
#     song = get_object_or_404(Song, pk=song_id)
#     try:
#         if song.is_favorite:
#             song.is_favorite = False
#         else:
#             song.is_favorite = True
#         song.save()
#     except (KeyError, Song.DoesNotExist):
#         return JsonResponse({'success': False})
#     else:
#         return JsonResponse({'success': True})


# def favorite_album(request, album_id):
#     album = get_object_or_404(Album, pk=album_id)
#     try:
#         if album.is_favorite:
#             album.is_favorite = False
#         else:
#             album.is_favorite = True
#         album.save()
#     except (KeyError, Album.DoesNotExist):
#         return JsonResponse({'success': False})
#     else:
#         return JsonResponse({'success': True})


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        albums = Subject.objects.all()
        song_results = File.objects.all()
        query = request.GET.get("q")
        if query:
            albums = albums.filter(
                Q(name__icontains=query) |
                Q(university__icontains=query)
            ).distinct()
            song_results = song_results.filter(
                Q(name__icontains=query)
            ).distinct()
            return render(request, 'music/index.html', {
                'albums': albums,
                'songs': song_results,
            })
        else:
            return render(request, 'music/index.html', {'albums': albums})

def forum(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        # albums = Album.objects.filter(user=request.user)
        albums = Forum.objects.all()
        song_results = Question.objects.all()
        query = request.GET.get("q1")
        if query:
            albums = albums.filter(
                Q(name__icontains=query)
                # Q(artist__icontains=query)
            ).distinct()
            song_results = song_results.filter(
                Q(name__icontains=query)
            ).distinct()
            return render(request, 'music/index1.html', {
                'albums': albums,
                'songs': song_results,
            })
        else:
            return render(request, 'music/index1.html', {'albums': albums})

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/login.html', context)


def login_user(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(email=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                albums = Subject.objects.all()
                return render(request, 'music/index.html', {'albums': albums})
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')


# def register(request):
#     form = UserForm(request.POST or None)
#     if form.is_valid():
#         user = form.save(commit=False)
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         user.set_password(password)
#         user.save()
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 albums = Album.objects.filter(user=request.user)
#                 return render(request, 'music/index.html', {'albums': albums})
#     context = {
#         "form": form,
#     }
#     return render(request, 'music/register.html', context)


# def songs(request, filter_by):
#     if not request.user.is_authenticated():
#         return render(request, 'music/login.html')
#     else:
#         try:
#             song_ids = []
#             for album in Album.objects.filter(user=request.user):
#                 for song in album.song_set.all():
#                     song_ids.append(song.pk)
#             users_songs = Song.objects.filter(pk__in=song_ids)
#             if filter_by == 'favorites':
#                 users_songs = users_songs.filter(is_favorite=True)
#         except Album.DoesNotExist:
#             users_songs = []
#         return render(request, 'music/songs.html', {
#             'song_list': users_songs,
#             'filter_by': filter_by,
#         })
