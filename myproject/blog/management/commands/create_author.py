from django.core.management.base import BaseCommand
from blog.models import Author
from django.utils import lorem_ipsum


class Command(BaseCommand):
    help = "Create authors"

    def handle(self, *args, **kwargs):
        for i in range(10):
            author = Author(
                first_name = f'Name_{i}',
                second_name = f'Second_Name_{i}',
                email = f'Name_{i}@mail.ru',
                bio = ". ".join(lorem_ipsum.paragraphs(5, common=False)),
                birthdate = '2000-01-12')
            
            author.full_name = author.fullname()
            author.save()
            self.stdout.write(f'{author.full_name}')