# Generated by Django 4.1 on 2022-08-27 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_post_options_alter_post_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Publish')], default='draft', max_length=10),
        ),
    ]
