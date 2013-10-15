# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Contact'
        db.create_table(u'contact_contact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('f_name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('l_name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('bday', self.gf('django.db.models.fields.DateField')()),
            ('bio', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('jabber', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('skype', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('other', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'contact', ['Contact'])


    def backwards(self, orm):
        # Deleting model 'Contact'
        db.delete_table(u'contact_contact')


    models = {
        u'contact.contact': {
            'Meta': {'object_name': 'Contact'},
            'bday': ('django.db.models.fields.DateField', [], {}),
            'bio': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'f_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jabber': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'l_name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'other': ('django.db.models.fields.TextField', [], {}),
            'skype': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['contact']