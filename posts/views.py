'''Posts views'''
from django.http import HttpResponse

# Utilities
from datetime import datetime

posts = [
    {
        'name': 'Kenyi Hancco',
        'user': 'kenyihq',
        'timestamp': datetime.now().strftime('%b, %dth, %Y - %H, %M hrs'),
        'pictures': 'https://picsum.photos/id/237/200/200'
    },
    {
        'name': 'Axel Hancco',
        'user': 'haxelhq',
        'timestamp': datetime.now().strftime('%b, %dth, %Y - %H, %M hrs'),
        'pictures': 'https://picsum.photos/id/84/200/200'
    },
    {
        'name': 'Ariana Hancco',
        'user': 'larianahq',
        'timestamp': datetime.now().strftime('%b, %dth, %Y - %H, %M hrs'),
        'pictures': 'https://picsum.photos/id/784/200/200'
    }
]


def list_posts(request):
    content = []
    for post in posts:
        content.append("""
            <p><strong>{name}</strong></p>
            <p><small>{user} - <i>{timestamp}</i></small></p>
            <figure><img src='{pictures}'/></figure>
        """.format(**post))
    return HttpResponse('<br>'.join(content))