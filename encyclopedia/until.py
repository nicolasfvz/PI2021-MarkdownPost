from .models import Posts

def exact_post(title):
    if (Posts.objects.filter(title=title).first() != None):
        return True
    else:
        return False