from optparse import make_option
from django.core.management.base import CommandError
from mezzanine.blog.management.base import BaseImporterCommand

class Command(BaseImporterCommand):

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser)
        #parser.add_argument("-s", "--some-arg-name", dest="some_arg_var", help="Description of some-arg-name")

    def handle_import(self, options):
        pages = [
            {
                'title': 'About',
                'content': '<h2>About Us</h2><p>lorem ipsum...</p>',
                'old_id': 'about',
            },
            {
                'title': 'Our History',
                'content': 'Back in the day....',
                'old_parent_id': 'about',
                #'url': 'about/our-history',
            },
        ]
        for page in pages:
            added_page = self.add_page(**page)

            #defaults = dict(tags=[], old_url=None, old_id=None, old_parent_id=None)
            #defaults.update(page)
            #self.pages.append(defaults)

        # blog posts could be added here too
        posts = []
        for post in posts:
            added_post = self.add_post(**post)
