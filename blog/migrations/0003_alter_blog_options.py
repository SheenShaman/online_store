# Generated by Django 4.2.4 on 2023-09-21 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_published_blog_is_published_alter_blog_slug_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'verbose_name': 'Блог', 'verbose_name_plural': 'Блог'},
        ),
    ]