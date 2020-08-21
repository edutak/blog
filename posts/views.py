from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post
from posts.forms import PostForm


def p_list(request):
    my_list = Post.objects.all().order_by('-id')
    context = {'posts': my_list}
    return render(request, 'list.html', context)


def p_create(request):
    # POST 방식으로 호출될때
    if request.method == 'POST':
        post_form = PostForm(request.POST)

        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')

    # GET 방식으로 호출될때
    else:
        post_form = PostForm()

    return render(request, 'create.html', {'post_form': post_form})


def p_delete(request,post_id):
    post = Post.objects.get(id=post_id)
    post.delete()

    return redirect('posts:list')


def p_update(request, post_id):

    post = get_object_or_404(Post, pk=post_id)

    # POST 방식으로 호출될때
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)

        if post_form.is_valid():
            post_form.save()
            return redirect('posts:list')

    # GET 방식으로 호출될때
    else:
        post_form = PostForm(instance=post)

    return render(request, 'create.html', {'post_form': post_form})

