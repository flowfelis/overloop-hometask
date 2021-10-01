import django
import os
import sys


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "techtest.settings")
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", ".."))
django.setup()

from techtest.articles.models import Article
from techtest.authors.models import Author
from techtest.regions.models import Region
from django.core import management

# Migrate
management.call_command("migrate", no_input=True)
# Seed
Article.objects.create(title="Fake Article", content="Fake Content").regions.set(
    [
        Region.objects.create(code="AL", name="Albania"),
        Region.objects.create(code="UK", name="United Kingdom"),
    ]
)
author = Author.objects.create(first_name='Alican', last_name='Donmez')
Article.objects.create(title="Fake Article", content="Fake Content", author=author)
Article.objects.create(title="Fake Article", content="Fake Content")
Article.objects.create(title="Fake Article", content="Fake Content")
Article.objects.create(title="Fake Article", content="Fake Content").regions.set(
    [
        Region.objects.create(code="AU", name="Austria"),
        Region.objects.create(code="US", name="United States of America"),
    ]
)
