from django.http import JsonResponse
from .models import Post, Comment
from datetime import datetime

def add_post(request): 
    post_text = request.POST.get('text')
    
    try: 
        post = Post(author=request.user, text=post_text, pub_date=datetime.now())
        post.save()
        
        return JsonResponse({'status': 'ok'})
    except Exception as e: 
        print(e)
        return JsonResponse({'status': 'server fail'})

def add_comment(request):
    post_id = request.POST.get('post_id')
    comment_text = request.POST.get('text')
    try:
        comment = Comment(author_id=request.user, post_id=post_id, text=comment_text)
        comment.save()

        return JsonResponse({"status": 'ok'})
    except Exception as e:
        print(e)
        return JsonResponse({'status': 'server fail'})


def get_comments(request): 
    post_id = request.GET.get('post_id')
    print(Comment.objects.filter(post_id=post_id))
    data = {
        'post_id': post_id
    }
    return JsonResponse(data)