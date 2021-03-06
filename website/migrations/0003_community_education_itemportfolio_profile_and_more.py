# Generated by Django 4.0.5 on 2022-07-23 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20211216_1300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('community_role', models.CharField(blank=True, max_length=255, null=True)),
                ('community_start', models.CharField(blank=True, max_length=255, null=True)),
                ('community_end', models.CharField(blank=True, max_length=255, null=True)),
                ('structure', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diploma', models.CharField(blank=True, max_length=255, null=True)),
                ('start_year', models.IntegerField(blank=True)),
                ('end_year', models.IntegerField(blank=True)),
                ('school', models.CharField(blank=True, max_length=255, null=True)),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemPortfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Application', 'Application'), ('Web', 'Web')], default='Application', max_length=255)),
                ('client', models.CharField(blank=True, max_length=255, null=True)),
                ('project_link', models.CharField(blank=True, max_length=255, null=True)),
                ('project_pic_1', models.ImageField(blank=True, upload_to='images/portfolio/')),
                ('project_pic_2', models.ImageField(blank=True, null=True, upload_to='images/portfolio/')),
                ('project_pic_3', models.ImageField(blank=True, null=True, upload_to='images/portfolio/')),
                ('detail', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('surname', models.CharField(blank=True, max_length=255, null=True)),
                ('localisation', models.CharField(blank=True, max_length=255, null=True)),
                ('bio', models.TextField()),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='images/profile/')),
                ('background_pic', models.ImageField(blank=True, null=True, upload_to='images/background/')),
                ('twitter_link', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_link', models.CharField(blank=True, max_length=255, null=True)),
                ('github_link', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=255, null=True)),
                ('grade', models.CharField(blank=True, max_length=255, null=True)),
                ('birthday', models.DateField(blank=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Communautaire',
        ),
        migrations.DeleteModel(
            name='Diplome',
        ),
        migrations.DeleteModel(
            name='Item_portfolio',
        ),
        migrations.DeleteModel(
            name='Profil',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='nom_compagnie',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='pays',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='periode_commencement',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='periode_fin',
            new_name='experience_end',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='titre',
            new_name='experience_start',
        ),
        migrations.RenameField(
            model_name='experience',
            old_name='ville',
            new_name='role',
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='nom',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='capacite',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='categorie',
        ),
        migrations.AddField(
            model_name='skill',
            name='skill_svg',
            field=models.ImageField(blank=True, null=True, upload_to='images/skills/'),
        ),
    ]
