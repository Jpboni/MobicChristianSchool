# Generated by Django 3.2.4 on 2022-12-30 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_alter_page_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='postfilecontent',
            name='course_code',
        ),
    ]
