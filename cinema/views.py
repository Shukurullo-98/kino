from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from .models import Cinema, Category, Comment, Profile
from .forms import CinemaForm, LoginForm, RegisterForm, CommentForm, EditProfileForm, EditAccountForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib import messages


class CinemaListView(ListView):
    model = Cinema
    template_name = 'cinema/index.html'
    context_object_name = 'cinema'
    extra_context = {
        'title': 'Bosh saxifa: KinoTV'
    }


class CinemaListByCategory(CinemaListView):

    def get_queryset(self):
        cinema = Cinema.objects.filter(category_id=self.kwargs["pk"])
        return cinema

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = f'Film: {category.title}'
        return context


import random


class CinemaDetailView(DetailView):
    model = Cinema
    context_object_name = 'cinema'
    template_name = 'cinema/cinema_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        cinema = Cinema.objects.get(pk=self.kwargs['pk'])
        profile = Profile.objects.get(user_id=cinema.author.pk)
        cinema.views += 1
        cinema.save()
        items = list(Cinema.objects.all()[::-1][:100])
        cinemas = random.sample(items, 3)
        context['title'] = f'Film: {cinema.title}'
        context['cinemas'] = cinemas
        context['profile'] = profile
        context['comments'] = Comment.objects.filter(cinema=cinema)
        if self.request.user.is_authenticated:
            context['forms'] = CommentForm()
        return context


class AddCinema(CreateView):
    form_class = CinemaForm
    template_name = 'cinema/add_cinema.html'
    extra_context = {
        'title': 'Film qo\'shish'
    }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CinemaUpdateView(UpdateView):
    model = Cinema
    form_class = CinemaForm
    template_name = 'cinema/add_cinema.html'
    extra_context = {
        'title': 'Filmni taxrirlash'
    }


class CinemaDelete(DeleteView):
    model = Cinema
    context_object_name = 'cinema'
    success_url = reverse_lazy('index')


def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            if user:
                login(request, user)
                messages.success(request, 'Akkauntga muvaffaqiyatli kirildi !')
                return redirect('index')
            else:
                messages.error(request, 'Parol yoki Login xato !')
                return redirect('login')
        else:
            messages.error(request, 'Parol yoki Login xato !')
            return redirect('login')
    else:
        login_form = LoginForm
    context = {
        'title': 'Akkauntga kirish',
        'login_form': login_form
    }
    if not request.user.is_authenticated:
        return render(request, 'cinema/login.html', context)
    else:
        return redirect('index')


def user_logaut(request):
    if not request.user.is_authenticated:
        return redirect('index')
    else:
        logout(request)
        messages.warning(request, 'Siz profildan chiqdingiz !')
        return redirect('index')


def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user)
            profile.save()
            messages.success(request, 'Ro\'yxatdan o\'tish muvaffaqiyatli yakunlandi')
            return redirect('login')
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
                return redirect('register')
    else:
        form = RegisterForm
    context = {
        'title': "Ro'yxatdan o'tish",
        'form': form
    }
    if not request.user.is_authenticated:
        return render(request, 'cinema/register.html', context)
    else:
        return redirect('index')


def save_comment(request, pk):
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.cinema = Cinema.objects.get(pk=pk)
        comment.user = request.user
        comment.save()
        return redirect('cinema', pk)


def profile_view(request, pk):
    profile = Profile.objects.get(user_id=pk)
    cinemas = Cinema.objects.filter(author_id=pk)
    most_viewed = cinemas.order_by('-views')[:1][0]
    recent_cinema = cinemas.order_by('-created_at')[:1][0]

    context = {
        'title': f'Profil: {request.user.username}',
        'profile': profile,
        'most_viewed': most_viewed,
        'recent_cinema': recent_cinema,
    }
    return render(request, 'cinema/profile.html', context)


def edit_account_view(request):
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'Bu akkaunt taxrirlandi')
            return redirect('profile', request.user.pk)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
                return redirect('change')
    else:
        form = EditAccountForm(instance=request.user)
    context = {
        'title': f'Akkauntni taxrirlash {request.user.username}',
        'form': form
    }
    return render(request, 'cinema/change.html', context)


def edit_profile_view(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Bu akkaunt taxrirlandi')
            return redirect('profile', request.user.pk)
        else:
            for field in form.errors:
                messages.error(request, form.errors[field].as_text())
                return redirect('change')
    else:
        form = EditProfileForm(instance=request.user.profile)
    context = {
        'title': f'Profil taxrirlash {request.user.username}',
        'form': form
    }
    return render(request, 'cinema/change.html', context)
