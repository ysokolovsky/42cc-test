from django.conf import settings


def proj_settings(request):
    return {'settings': settings}