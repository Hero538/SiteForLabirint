from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Post,Comment
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .forms import CommentForm
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.
def forum(request):
    posts= Post.objects.order_by('-pub_date').filter(is_published=True)
    return render(request,'forum/forum.html',{'posts':posts})

@login_required(login_url='/accounts/signup')
def add(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body']:
            post = Post()
            post.title = request.POST['title']
            post.body = request.POST['body']
            post.pub_date = timezone.datetime.now()
            post.user = request.user
            post.save()
            return redirect('/forum/' + str(post.id))
        if request.POST['title'] and request.POST['body'] and request.POST['image']:
            post = Post()
            post.title = request.POST['title']
            post.image = request.POST['image']
            post.body = request.POST['body']
            post.pub_date = timezone.datetime.now()
            post.user = request.user
            post.save()
            return redirect('/forum/' + str(post.id))

        else:
            return render(request, 'forum/create.html', {{'error': 'All fields are required!'}})

    else:
        return render(request, 'forum/create.html')

def details(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    return render(request,'forum/details.html',{'post':post})

@login_required(login_url='/accounts/signup')
def upvote(request,post_id):

    if request.method == 'POST':
        post = get_object_or_404(Post,pk=post_id)
        if post!=0:
            return redirect('/forum/') #эм что работает??? это же смешно
        else:
            post.votes_total +=1
            post.save()
            return redirect('/forum/' + str(post_id))


@login_required(login_url='/accounts/signup')
def downvote(request,post_id):

    if request.method == 'POST':
        post = get_object_or_404(Post,pk=post_id) #вопрос: у нас будет счетчик минусов, или это будет - к общей карме??
        post.save()
        return redirect('/forum/' + str(post_id))



@require_http_methods(["POST"])
@login_required(login_url='/accounts/signup/')
def add_comment(request, post_id):
    form = CommentForm(request.POST)
    post = get_object_or_404(Post, id=post_id)

    if True:
        comment = Comment()
        comment.path = []
        comment.post_id = post
        comment.user_id = auth.get_user(request)
        comment.content = form.cleaned_data['comment_area']
        comment.save()


        try:
            comment.path.extend(Comment.objects.get(id=form.cleaned_data['parent_comment']).path)
            comment.path.append(comment.id)
        except ObjectDoesNotExist:
            comment.path.append(comment.id)

        comment.save()

    return redirect('/forum/' + str(post_id))