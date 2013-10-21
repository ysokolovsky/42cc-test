from django.core.management.base import BaseCommand
from django.db.models import get_app, get_models
from optparse import make_option


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--error',
            action='store_true',
            dest='error',
            default=False,
            help='Error output'),
    )

    def handle(self, *args, **options):
        app = get_app('contact')
        for model in get_models(app):
            info = "%s%s%s%d\n" % ("Model: ", model,
                                   " Objects count: ",
                                   model.objects.count())
            self.stdout.write(info)
            if options['error']:
                self.stderr.write('%s %s\n' % ("error: ", info))