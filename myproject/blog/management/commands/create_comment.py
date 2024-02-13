from django.core.management.base import BaseCommand
from blog.models import Post, Author, Comment
from django.utils import lorem_ipsum
from random import choice, randint


class Command(BaseCommand):
    help = "Create comment"

    def handle(self, *args, **kwargs):

        authors = Author.objects.all()
        posts = Post.objects.all()

        for i in range(10):
            comment = Comment(
                author = choice(authors),
                post = choice(posts),
                content = "\n".join(lorem_ipsum.paragraphs(3, common=False)),
                create_date = f'2000-01-{randint(10,30)}',
                edit_date = f'2000-02-{randint(10,30)}',
                )


            comment.save()
           