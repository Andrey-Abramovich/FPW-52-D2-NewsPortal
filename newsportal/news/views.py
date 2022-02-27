from .models import Post
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from .filters import PostFilter
from .forms import PostForm
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


# def index(request):
#     posts = Post.objects.all()
#     return render(request, 'index.html', context={'posts': posts})


# def detail(request, id):
#     post = Post.objects.get(id=id)
#     return render(request, 'detail.html', context={'post': post})


class Posts(ListView):
    model = Post
    template_name = 'news/template/news/index.html'
    context_object_name = 'posts'
    ordering = ['-dateCreation']
    paginate_by = 10
    # form_class = PostForm

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class Postsearch(ListView):
    model = Post
    template_name = 'news/template/news/search.html'
    context_object_name = 'search'
    ordering = ['-dateCreation']
    paginate_by = 10
    # form_class = PostForm

    def get_filter(self):
        return PostFilter(self.request.GET, queryset=super().get_queryset())

    def get_queryset(self):
        return self.get_filter().qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context


class PostDetailView(DetailView):
    # model = Post
    template_name = 'news/template/news/detail.html'
    queryset = Post.objects.all()


class PostCreateView(CreateView):
    # model = Post
    template_name = 'news/template/news/post_create.html'
    form_class = PostForm
    success_url = '/'


class PostUpdateView(UpdateView):
    template_name = 'news/template/news/post_create.html'
    form_class = PostForm
    success_url = '/'

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


class PostDeleteView(DeleteView):
    template_name = 'news/template/news/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/'

    # def get_object(self, **kwargs):
    #     id = self.kwargs.get('pk')
    #     return Post.objects.get(pk=id)