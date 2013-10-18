APP = test42cc
SETTINGS = settings

PWD = $(pwd)
MANAGESCRIPT = django-admin.py
M = manage.py
MANAGE = PYTHONPATH=$(PWD) DJANGO_SETTINGS_MODULE=$(APP).$(SETTINGS) $(MANAGESCRIPT)

test:
	$(MANAGE) test contact

run:
	$(MANAGE) runserver

syncdb:
	$(MANAGE) syncdb --noinput
	python manage.py migrate