# Generated by Django 4.2.6 on 2023-11-25 16:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_info',
            old_name='username',
            new_name='name',
        ),
    ]