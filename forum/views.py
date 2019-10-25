from django.shortcuts import render,redirect,get_object_or_404
from django.utils import timezone
from .models import Post
# Create your views here.
def forum(request):
    posts= Post.objects.order_by('-pub_date').filter(is_published=True)
    return render(request,'forum/forum.html',{'posts':posts})


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
    details = get_object_or_404(Post,pk=post_id)
    return render(request,'forum/details.html',{'details':details})