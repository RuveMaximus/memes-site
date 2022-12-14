from django.http import JsonResponse
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

from django.contrib.auth.models import User

@login_required(login_url='/user/login/')
@csrf_exempt
def add_comment(request):
    data = json.loads(request.body.decode('utf-8'))

    post_id = data.get('post_id')
    comment_text = data.get('text')
    try:
        comment = Comment(author=request.user, post_id=post_id, text=comment_text)
        comment.save()

        return JsonResponse({"status": 'ok'})
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'fail'})

@csrf_exempt
def get_comments(request): 
    data = json.loads(request.body.decode('utf-8'))
    post_id = data.get('post_id')
    post_comments = list(Comment.objects.filter(post_id=post_id).values('author', 'text'))
    
    for comment in post_comments: 
        comment['author'] = {'id': comment['author'], 'name': str(User.objects.get(pk=comment['author']))}
    
    return JsonResponse({'status': 'ok', 'comments': post_comments})

@csrf_exempt
def like(request): 
    data = json.loads(request.body.decode('utf-8'))
    post_id = data.get('post_id')
    post = Post.objects.get(pk=post_id)
    post.likes += 1
    post.save()

    return JsonResponse({'status': 'ok'})

@csrf_exempt
def dislike(request):
    data = json.loads(request.body.decode('utf-8'))
    post_id = data.get('post_id')
    post = Post.objects.get(pk=post_id)
    post.dislikes += 1
    post.save()

    return JsonResponse({'status': 'ok'})
