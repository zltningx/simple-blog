from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from django.core.mail import send_mail
from .models import Post, Comment
from .form import EmailPostForm, CommentForm
from taggit.models import Tag
from haystack.query import SearchQuerySet


def post_list(request, tag_slug=None):
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 5)  # 一页 3片文章
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # 若page不是一个整数 返回第一页
        posts = paginator.page(1)
    except EmptyPage:
        # 超出页码 置最后一页
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post/list.html',
                  {'page': page, 'posts': posts, 'tag': tag})


class PostMyselfView(ListView):
    queryset = Post.published.all().filter(owner='myself')
    context_object_name = 'my_posts'
    paginate_by = 5
    template_name = 'blog/post/list_myself.html'

# class PostListView(ListView):
#     queryset = Post.published.all()
#     context_object_name = 'posts'
#     paginate_by = 3
#     template_name = 'blog/post/list.html'


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    comments = post.comments.filter(active=True)  # 通过审核评论
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        print(request.POST)
        if comment_form.is_valid():
            # 创建评论但先不存入数据库
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            # 保存
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'comment_form': comment_form})


def post_share(request, post_id):
    # 通过post id 检索
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False  # 初始化为未发送

    if request.method == 'POST':
        # 表单提交后
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            # 包括 http 在内完整的链接: build_absolute_uri
            post_url = request.build_absolute_uri(post.get_absolute_url())
            title = "Hello! {}({}) 推介您阅读这篇文章 {}".format(cd['name'],
                                                        cd['email'],
                                                        post.title)
            content = "我发现了一篇很nice文章 {}\n 推介给您: {} \n {}"\
                .format(post.title, post_url, cd['comments'])
            send_mail(title, content, "zltningx@163.com", [cd['to']])
            sent = True
            form.clean()
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post, 'form': form,
                                                    'sent': sent})


class SearchView(ListView):
    template_name = 'blog/post/search.html'
    context_object_name = 'post_search_list'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        kwargs['s'] = self.request.GET.get('s', '')
        return super(SearchView, self).get_context_data(**kwargs)

    def get_queryset(self):
        s = self.request.GET.get('s', '')
        post_search_list = SearchQuerySet().models(Post).\
            filter(content=s).load_all()

        return post_search_list