# Generated by Django 5.0.2 on 2024-02-16 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='full_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='edit_date',
            field=models.DateField(auto_now=True),
        ),
    ]
