from django.shortcuts import render, HttpResponseRedirect
from .models import Clients, Notifications, Filterwords
from .forms import AddUserForm, NotificationForm, FilterWordsForm, UserLoginForm
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def index(request):
    users = Clients.objects.all()
    paginator = Paginator(users, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"users": users, "page_obj": page_obj}
    return render(request, "admin_panel/index.html", context)


@login_required
def add_client(request):
    if request.method == "POST":
        form = AddUserForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        form = AddUserForm()
    context = {"form": form}
    return render(request, "admin_panel/add_client.html", context)


@login_required
def delete_client(request, client_id):
    client = get_object_or_404(Clients, id=client_id)
    filter_words = Filterwords.objects.filter(clientid=client_id)
    filter_words.delete()
    client.delete()

    return HttpResponseRedirect(reverse("index"))


def login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("index"))
    else:
        form = UserLoginForm
    context = {
        "form": form,
    }
    return render(request, "admin_panel/login.html", context)


@login_required
def edit_client(request, client_id):
    if request.method == "GET":
        client = get_object_or_404(Clients, id=client_id)
        form = AddUserForm(instance=client)
        try:
            notification = client.notificationid
        except:
            notification = None
        context = {"form": form, "client": client, "notification": notification}
        return render(request, "admin_panel/edit_client.html", context)
    elif request.method == "POST":
        client = get_object_or_404(Clients, id=client_id)
        form = AddUserForm(instance=client, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("index"))


@login_required
def add_notification(request, client_id):
    client = get_object_or_404(Clients, id=client_id)
    if request.method == "POST":
        form = NotificationForm(data=request.POST)
        if form.is_valid():
            form.save()
            notification = Notifications.objects.last()
            client.notificationid = notification
            client.save()
            return HttpResponseRedirect(reverse("index"))
    else:
        notification = client.notificationid
        form = NotificationForm(instance=notification)
        context = {"form": form, "client_id": client_id}
        return render(request, "admin_panel/add_notification_channels.html", context)


@login_required
def edit_notification_channels(request, client_id):
    if request.method == "GET":
        client = get_object_or_404(Clients, id=client_id)
        notification = client.notificationid
        form = NotificationForm(instance=notification)
        context = {"form": form, "client": client, "client_id": client_id}
        return render(request, "admin_panel/add_notification_channels.html", context)
    elif request.method == "POST":
        client = get_object_or_404(Clients, id=client_id)
        notification = client.notificationid
        form = NotificationForm(instance=notification, data=request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("index"))


@login_required
def filter_word_list(request, client_id):
    filter_words = Filterwords.objects.filter(clientid=client_id)
    paginator = Paginator(filter_words, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        "filter_words": filter_words,
        "client_id": client_id,
        "page_obj": page_obj,
    }
    return render(request, "admin_panel/filterwords.html", context)


@login_required
def add_filter_words(request, client_id):
    client = get_object_or_404(Clients, id=client_id)
    if request.method == "POST":
        form = FilterWordsForm(data=request.POST)
        if form.is_valid():
            form.save()
            filter_word = Filterwords.objects.last()
            filter_word.clientid = client.id
            filter_word.save()
            return HttpResponseRedirect(
                reverse("filter_word_list", kwargs={"client_id": client_id})
            )
    else:
        form = FilterWordsForm()
        context = {"form": form, "client_id": client_id}
        return render(request, "admin_panel/add_edit_filter_word.html", context)


@login_required
def edit_filter_word(request, client_id, word_id):
    client = get_object_or_404(Clients, id=client_id)
    word = get_object_or_404(Filterwords, id=word_id)
    if request.method == "GET":
        form = FilterWordsForm(instance=word)
        context = {"form": form, "client": client, "word_id": word_id}
        return render(request, "admin_panel/add_edit_filter_word.html", context)
    elif request.method == "POST":
        form = FilterWordsForm(data=request.POST, instance=word)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(
                reverse("filter_word_list", kwargs={"client_id": client_id})
            )


@login_required
def delete_filter_word(request, word_id, client_id):
    word = get_object_or_404(Filterwords, id=word_id)
    word.delete()
    context = {"client_id": client_id}
    return render(request, "admin_panel/filterwords.html", context)


def error(request, exception):
    return render(request, "admin_panel/404.html", status=404)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("login"))
