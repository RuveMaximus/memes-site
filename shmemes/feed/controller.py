from django.http import JsonResponse
from .models import Post, Comment

def add_comment(request):
    post_id = request.GET.get('post_id')
    comment_text = request.GET.get('text')
    data = {
        'post_id': post_id,
        'comment_text': comment_text
    }
    return JsonResponse(data)


def get_comments(request): 
    post_id = request.GET.get('post_id')
    data = {
        'post_id': post_id
    }
    return JsonResponse(data)