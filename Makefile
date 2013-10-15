APP = test42cc
SETTINGS = settings

PWD = $(pwd)
MANAGESCRIPT = django-admin.py
MANAGE = PYTHONPATH=$(PWD) DJANGO_SETTINGS_MODULE=$(APP).$(SETTINGS) $(MANAGESCRIPT)

test:
	$(MANAGE) test contact

run:
	$(MANAGE) runserver

syncdb:
	$(MANAGE) syncdb