from django.urls import path

from posts.views import PostView, CommentView, LikeView, FollowView

urlpatterns = [
        path('/post', PostView.as_view()),
        path('/comment', CommentView.as_view()),
        path('/like', LikeView.as_view()),
        path('/follow', FollowView.as_view()),
]

