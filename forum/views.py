from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Post,Comment
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .forms import CommentForm
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect 
# Create your views here.
def forum(request):

    search_query = request.GET.get('search', '')
    if search_query:
        posts = Post.objects.filter(Q(title__icontains=search_query) | Q(body__icontains=search_query))
        #posts = Post.objects.filter(title__icontains=search_query)
    else:
        posts = Post.objects.order_by('-pub_date').filter(is_published=True)
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
    comments = Comment.objects.all()

    return render(request,'forum/details.html',{'post':post,'comments':comments})

@login_required(login_url='/accounts/signup')
def upvote(request,post_id):               #Это надо исправить 
    if post_id in request.COOKIES:          
        return redirect('/forum/' + post_id)
    else:
        if request.method == 'POST':
            post = get_object_or_404(Post,pk=post_id)
            post.votes_total +=1
            post.save()
            response = redirect('/forum/' + post_id)
            response.set_cookie(post_id, 'voted')
            return response


@login_required(login_url='/accounts/signup')
def downvote(request,post_id):      #Тоже надо исправить // ок пока так, оставим этот способ, если ничего не придумается больше
    if post_id in request.COOKIES:          
        return redirect('/forum/' + post_id)
    else:
        if request.method == 'POST':
            post = get_object_or_404(Post,pk=post_id)
            post.votes_total -=1
            post.save()
            response = redirect('/forum/' + post_id)
            response.set_cookie(post_id, 'voted')
            return response #так получается, если ты однажды проголосовал, назад дороги нет 



@require_http_methods(["POST"])
@login_required(login_url='/accounts/signup/')
def add_comment(request, post_id):
    #form = CommentForm(request.POST)
    post = get_object_or_404(Post, id=post_id)
                                                #Кривая хурма ,надо будет исправить... Пока что так
    if True:
        comment = Comment()
        comment.path = []
        comment.post_id = post
        comment.user_id = auth.get_user(request)
        comment.content = request.POST['comment']
        comment.user = request.user
        comment.save()
    #вроде и так работает, хотя хз... 
        try:
           comm = get_object_or_404(Comment,pk=request.user.id)
           comment.path.extend(comm.path)
           comment.path.append(comment.id)
        except ObjectDoesNotExist:
           comment.path.append(comment.id)
    comment.save()

    return redirect('/forum/' + str(post_id))