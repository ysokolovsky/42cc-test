from django import forms
from django.utils.safestring import mark_safe
from django.conf import settings


class DatepickerWidget(forms.TextInput):
    class Media:
        js = (settings.STATIC_URL + 'js/jquery-ui-1.10.3.custom.min.js',
              settings.STATIC_URL + 'js/main.js')

        css = {'all':
               (settings.STATIC_URL + 'css/jquery-ui-1.10.3.custom.min.css',)}

    def __init__(self, params='', attrs={}):
        self.params = params
        super(DatepickerWidget, self).__init__()

    def render(self, name, value, attrs=None):
        rendered = super(DatepickerWidget, self).render(name, value, attrs=attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
                                    $('#id_%s').datepicker({%s});
                                    </script>'''%(name, self.params,))