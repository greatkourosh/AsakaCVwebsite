from django.urls import path
from blog.views import blog, single_blog

app_name = 'blog'
urlpatterns = [
    path('', blog, name='weblog'),
    path('post-<post_id>', single_blog, name='singleblog')
]
