'''Post application model'''

from django.apps import AppConfig


class PostsConfig(AppConfig):
    '''Post applications setings'''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'
    varbose_name = 'Posts'
