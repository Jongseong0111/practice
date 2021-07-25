import json

from django.http     import JsonResponse
from django.views    import View

from users.models    import User
from posts.models    import Post, Comment, Like, Follow

# Create your views here.

class PostView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not User.objects.filter(email = data['email']).exists():
                return JsonResponse({"MESSAGE":"INVALID_USER"}, status=400)

            Post.objects.create(
                user            = User.objects.get(email=data['email']),
                image           = data['image'],
                post            = data['post'],
            )
        
            return JsonResponse({"MESSAGE":"SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status=400)
    def get(self, request):
        posts = Post.objects.all()
        results = []

        for post in posts:
            results.append(
                {
                    "user"          : post.user.nickname,
                    "image"         : post.image,
                    "post"          : post.post,
                    "creation_time" : post.creation_time
                }

            )
        return JsonResponse({'resutls':results}, status=200)

class CommentView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({"MESSAGE":"INVALID_USER"}, status=400)

            if not Post.objects.filter(id = data['post']).exists():
                return JsonResponse({"MESSAGE":"NO_POST"}, status=400)

            Comment.objects.create(
                user            = User.objects.get(email=data['email']),
                post_id         = data['post'],
                comment         = data['comment']         
            )

            return JsonResponse({"MESSAGE":"SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status=400)
    def get(self, request):
        comments = Comment.objects.filter(post_id=1)
        results = []

        for comment in comments:
            results.append(
                {
                    "user"          : comment.user.nickname,
                    "comment"       : comment.comment,
                    "creation_time" : comment.creation_time
                }
            )
        return JsonResponse({'resutls':results}, status=200)

class LikeView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not User.objects.filter(email=data['email']).exists():
                return JsonResponse({"MESSAGE":"INVALID_USER"}, status=400)
            
            if not Post.objects.filter(id = data['post']).exists():
                return JsonResponse({"MESSAGE":"NO_POST"}, status=400)

            like, is_like = Like.objects.get_or_create(
                user = User.objects.get(email=data['email']),
                post_id = data['post']
            )

            if not is_like:
                like.delete()
                return JsonResponse({"MESSAGE":"DELETE"}, status=200)
            
            return JsonResponse({"MESSAGE":"SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status=400)

class FollowView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            if not User.objects.filter(email=data['follow']).exists():
                return JsonResponse({"MESSAGE":"INVALID_USER"}, status=400)

            if not User.objects.filter(email=data['follow']).exists():
                return JsonResponse({"MESSAGE":"INVALID_USER"}, status=400)
            
            follow, is_follow = Follow.objects.get_or_create(
                follow   = User.objects.get(email=data['follow']),
                followed = User.objects.get(email=data['followed'])
            )

            if not is_follow:
                follow.delete()
                return JsonResponse({"MESSAGE":"DELETE"}, status=200)

            return JsonResponse({"MESSAGE":"SUCCESS"}, status=201)
        except KeyError:
            return JsonResponse({"MESSAGE":"KEY_ERROR"}, status=400)
