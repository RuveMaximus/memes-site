from django.http import JsonResponse
from .models import Post, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

@login_required(login_url='/user/login/')
@csrf_exempt
def add_comment(request):
    data = json.loads(request.body.decode('utf-8'))

    post_id = data.get('post_id')
    comment_text = data.get('text')
    try:
        comment = Comment(author_id=request.user, post_id=post_id, text=comment_text)
        comment.save()

        return JsonResponse({"status": 'ok'})
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'fail'})

@csrf_exempt
def get_comments(request): 
    data = json.loads(request.body.decode('utf-8'))

    post_id = data.get('post_id')

    post_comments = Comment.objects.filter(post_id=post_id)
    return JsonResponse(post_comments)

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
