from django.db import models

class Post(models.Model):
    user          = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='posts')
    creation_time = models.DateTimeField(auto_now_add=True)
    image         = models.URLField()
    post          = models.TextField()

    class Meta:
        db_table  = 'posts'

class Comment(models.Model):
    user          = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='comments')
    post          = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    creation_time = models.DateTimeField(auto_now_add=True)
    comment       = models.TextField()

    class Meta:
        db_table  = 'comments'

class Like(models.Model):
    user          = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='likes')
    post          = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')

    class Meta:
        db_table  = 'likes'

class Follow(models.Model):
    follow        = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='follow')
    followed      = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='followed')

    class Meta:
        db_table  = 'follows'