# Generated by Django 4.0.2 on 2022-03-08 17:01

import articles.blocks
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_articlepagetag_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('media', articles.blocks.GEMediaBlock(icon='media'))], blank=True, null=True),
        ),
    ]
