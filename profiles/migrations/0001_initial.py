# Generated by Django 3.1.13 on 2021-11-24 16:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0066_collection_management_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GEUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Transgender', 'Transgender'), ('Non-conforming/Non-binary', 'Non Conforming Non Binary'), ('Other', 'Other'), ('Not comfortable sharing', 'Not Given')], max_length=50, null=True)),
                ('location', models.CharField(blank=True, max_length=128, null=True)),
                ('date_of_birth', models.DateField(null=True)),
                ('terms_and_conditions', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SecurityQuestion',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SecurityQuestionIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SecurityQuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=250)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.securityquestion')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profiles.geuser')),
            ],
        ),
        migrations.CreateModel(
            name='GEUserSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prevent_phone_number_in_username', models.BooleanField(default=False, verbose_name='Prevent phone number in username / display name')),
                ('prevent_email_in_username', models.BooleanField(default=False, verbose_name='Prevent email in username / display name')),
                ('num_security_questions', models.PositiveSmallIntegerField(default=1, verbose_name='Number of security questions asked for password recovery')),
                ('password_recovery_retries', models.PositiveSmallIntegerField(default=5, verbose_name='Max number of password recovery retries before lockout')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.site')),
                ('terms_and_conditions', models.ForeignKey(blank=True, help_text='Choose a footer page', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='geuser',
            name='user_questions',
            field=models.ManyToManyField(through='profiles.SecurityQuestionAnswer', to='profiles.SecurityQuestion'),
        ),
    ]
