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