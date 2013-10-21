from django.db import models
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


class Contact(models.Model):
    f_name = models.CharField(max_length=60)
    l_name = models.CharField(max_length=60)
    bday = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=60)
    other = models.TextField()
    photo = models.ImageField(upload_to='photo', blank=True, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.f_name, self.l_name)


class Request(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    host = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s - %s" % (self.host, self.path)


class Signals(models.Model):
    object_id = models.IntegerField(verbose_name="object id")
    date = models.DateTimeField(verbose_name="date", auto_now_add=True)
    model = models.CharField(verbose_name="model", max_length=50)
    signal = models.CharField(verbose_name="signal", max_length=50)


@receiver(post_save)
def save_handler(instance, **options):
    model = instance._meta.object_name
    signal = 'create' if options['created'] else 'edit'
    if model == 'Signals':
        return
    try:
        Signals.objects.create(
            model=model,
            signal=signal,
            object_id=instance.id
        )
    except:
        return


@receiver(post_delete)
def delete_handler(instance, **options):
    model = instance._meta.object_name
    if model == 'Signals':
        return
    try:
        Signals.objects.create(
            model=model,
            signal='delete',
            object_id=instance.id
        )
    except:
        return
