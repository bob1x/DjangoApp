# Generated by Django 5.0.4 on 2024-05-06 17:00

import datetime
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('poste_type', models.IntegerField(choices=[(0, 'Offre'), (1, 'Demande')])),
                ('date_upload', models.DateTimeField(default=datetime.datetime.now)),
                ('intitule', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('lieu', models.CharField(max_length=255)),
                ('contact_Event', models.CharField(max_length=255)),
                ('date_enev', models.DateField()),
                ('heure_deb', models.TimeField()),
                ('heure_fin', models.TimeField()),
                ('place_dispo', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='user_photos')),
                ('telnum', models.CharField(default='00000000', max_length=8, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EvenClub',
            fields=[
                ('evenement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='isety.evenement')),
                ('club', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('isety.evenement',),
        ),
        migrations.CreateModel(
            name='EvenSocial',
            fields=[
                ('evenement_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='isety.evenement')),
                ('prix', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
            bases=('isety.evenement',),
        ),
        migrations.AddField(
            model_name='evenement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Logement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('poste_type', models.IntegerField(choices=[(0, 'Offre'), (1, 'Demande')])),
                ('date_upload', models.DateTimeField(default=datetime.datetime.now)),
                ('localisation', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('logment_contact', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recommandation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('poste_type', models.IntegerField(choices=[(0, 'Offre'), (1, 'Demande')])),
                ('date_upload', models.DateTimeField(default=datetime.datetime.now)),
                ('texte', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=999)),
                ('like', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('poste', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='isety.recommandation')),
            ],
        ),
        migrations.CreateModel(
            name='Stage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('poste_type', models.IntegerField(choices=[(0, 'Offre'), (1, 'Demande')])),
                ('date_upload', models.DateTimeField(default=datetime.datetime.now)),
                ('typeStg', models.IntegerField(choices=[(1, 'Ouvrier'), (2, 'Technicien'), (3, 'PFE')])),
                ('societe', models.CharField(max_length=255)),
                ('duree', models.IntegerField()),
                ('sujet', models.CharField(max_length=255)),
                ('contact_Stage', models.CharField(max_length=255)),
                ('specialite', models.CharField(choices=[('IT', 'IT - Technologie informatique'), ('SEG', 'SEG - Sc Eco et Gestion'), ('GC', 'GC - Génie Civil'), ('GP', 'GP - Génie des Procédés'), ('GM', 'GM - Génie Mécanique')], max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('poste_type', models.IntegerField(choices=[(0, 'Offre'), (1, 'Demande')])),
                ('date_upload', models.DateTimeField(default=datetime.datetime.now)),
                ('depart', models.CharField(max_length=255)),
                ('destination', models.CharField(max_length=255)),
                ('heure_dep', models.TimeField()),
                ('nbre_sieges', models.IntegerField()),
                ('contact_Trans', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
