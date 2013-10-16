from django.db import models


class Contact(models.Model):
    f_name = models.CharField(max_length=60)
    l_name = models.CharField(max_length=60)
    bday = models.DateField()
    bio = models.TextField()
    email = models.EmailField()
    jabber = models.EmailField()
    skype = models.CharField(max_length=60)
    other = models.TextField()

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Request(models.Model):
    time = models.DateTimeField(auto_now_add = True)
    host = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    method = models.CharField(max_length=255)

    def __unicode__(self):
        return "%s - %s" % (self.host, self.path)