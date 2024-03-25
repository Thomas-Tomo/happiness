import time

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views import generic
import random
from .forms import PostForm
from .models import Post
from django.shortcuts import render




class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        context['user'] = self.request.user
        return context

    def post(self, request):
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, pk=post_id)
        if request.user.is_authenticated:
            if post.likes.filter(id=request.user.id).exists():
                post.likes.remove(request.user)
                messages.info(request, "Post unliked!")
            else:
                post.likes.add(request.user)
                messages.success(request, "Post liked!")
        else:
            messages.error(request, "You need to be logged in to like a post.")
        return redirect('allposts')


class AddPostPage(generic.CreateView):
    """
    Allows a logged-in user to create a new blog post.
    """

    form_class = PostForm
    template_name = "form.html"
    success_url = reverse_lazy('allposts')

    def form_valid(self, form):
        User = get_user_model()
        if self.request.user.is_authenticated:
            form.instance.author = self.request.user
        else:
            form.instance.author = User.objects.get_or_create(username='anonymous')[0]
        response = super().form_valid(form)
        messages.success(
            self.request,
            "Post created successfully! Review in progress!")
        time.sleep(6)
        return response

    def form_invalid(self, form):
        response = super().form_invalid(form)
        messages.error(
            self.request,
            "Post creation failed. Please check your input.")
        return response


class UpdatePostView(LoginRequiredMixin, SuccessMessageMixin, generic.UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('allposts')
    success_message = "Post updated successfully!"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, self.success_message)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Post update failed. Please check your input.")
        return super().form_invalid(form)


class DeletePostView(LoginRequiredMixin, SuccessMessageMixin, generic.DeleteView):
    model = Post
    success_url = reverse_lazy('allposts')
    template_name = 'delete_post.html'
    success_message = "Post deleted successfully!"

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class AboutView(TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        team_members = [
            {
                'name': 'Darrach',
                'photo': 'images/darrach.jpeg',
                'role': 'Emojis & Filters',
                'happiness': 'Cozy nights in by the fire makes me happy',
                'linkedin': 'https://www.linkedin.com/in/darrach-barneveld-2b493511b/',
                'github': 'https://github.com/DarrachBarneveld'
            },
            {
                'name': 'James',
                'photo': 'images/james.jpeg',
                'role': 'Scrum Manager',
                'happiness': 'I like to get out clearing up litter to make me feel happier',
                'linkedin': 'https://www.linkedin.com/in/james-evans-682ba29b/',
                'github': 'https://github.com/broken-helix'
            },
            {
                'name': 'Thomas',
                'photo': 'images/thomas.jpeg',
                'role': 'Troubleshooter & Navigation',
                'happiness': "Sharing life's great joys with others brings me genuine happiness.",
                'linkedin': 'https://www.linkedin.com/in/thomasdomitrovic/',
                'github': 'https://github.com/Thomas-Tomo'
            },
            {
                'name': 'Alina',
                'photo': 'images/teo-alina.png',
                'role': 'Hack Generator',
                'happiness': "I find joy in life's simple pleasures: basking in sunlight, appreciating nature's beauty, good company, and laughter over beer with positive people.",
                'linkedin': 'https://www.linkedin.com/in/alina-teodora-brinzac/',
                'github': 'https://github.com/TeodoraAlina'
            },
            {
                'name': 'Monica',
                'photo': 'images/monica.png',
                'role': 'Team Page',
                'happiness': 'Setting and achieving small goals gives me a sense of accomplishment and boosts my happiness.',
                'linkedin': 'https://www.linkedin.com/in/monica-iancu-362825137/',
                'github': 'https://github.com/Monicaular'
            },
            {
                'name': 'Fergal',
                'photo': 'images/fergal.jpeg',
                'role': 'Styles',
                'happiness': 'The exhilarating rush of riding the waves while surfing fills me with pure happiness and a deep sense of contentment.',
                'linkedin': 'https://www.linkedin.com/in/fergal-mulligan-100686168/',
                'github': 'https://github.com/fergal92'
            },
            {
                'name': 'Stefan',
                'photo': 'images/stefan-ruppe.png',
                'role': 'Styles',
                'happiness': "Wiggling your toes, feeling what that's like, and then moving on",
                'linkedin': 'https://www.linkedin.com/in/stefan-ruppe/',
                'github': 'https://github.com/CsClown'
            },
            {
                'name': 'Elvis',
                'photo': 'images/elvis.jpeg',
                'role': 'README.md',
                'happiness': 'The sunrise every day brings joy to my heart.',
                'linkedin': 'https://www.linkedin.com/in/elvisblessingeunice/',
                'github': 'https://github.com/Elvisthegreat'
            },
        ]

        context = super().get_context_data(**kwargs)
        context['team_members'] = team_members
        return context


class AllPostsView(TemplateView):
    template_name = 'allposts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = Post.objects.all()
        context['posts'] = posts

        emojis = set()
        for post in posts:
            for emoji in post.emoji:
                if emoji != ' ' and emoji != '':
                    emojis.add(emoji)
        context['emojis'] = emojis

        return context


class RandomPostView(TemplateView):
    template_name = 'random_posts.html'

    def generate_random_post(self):
        all_posts = Post.objects.all()
        random_post = random.choice(all_posts)
        return random_post

    def post(self, request, *args, **kwargs):
        random_post = self.generate_random_post()
        return JsonResponse({
            'title': random_post.title,
            'emoji': random_post.emoji,
            'author': random_post.author.username,
        })