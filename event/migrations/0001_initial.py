# Generated by Django 3.2.7 on 2021-10-05 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_year', models.CharField(max_length=4)),
                ('end_year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_picture')),
                ('club_id', models.CharField(max_length=10, unique=True)),
                ('club_name', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('reg_no', models.CharField(max_length=10, unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('mobile_no', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('address', models.TextField(null=True)),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='event.batch')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='event.department')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=35)),
                ('faculty_id', models.CharField(max_length=10, unique=True)),
                ('designation', models.CharField(max_length=35)),
                ('hod', models.BooleanField(default=False)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.department')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_picture')),
                ('event_name', models.CharField(max_length=35)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(null=True)),
                ('organized_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='event.club')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.faculty')),
            ],
        ),
        migrations.AddField(
            model_name='club',
            name='incharge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.faculty'),
        ),
        migrations.CreateModel(
            name='Circular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='profile_picture')),
                ('title', models.CharField(max_length=35)),
                ('description', models.TextField(null=True)),
                ('date', models.DateField()),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.batch')),
                ('circular_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.faculty')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.department')),
            ],
        ),
    ]
