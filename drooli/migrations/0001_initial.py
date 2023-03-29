# Generated by Django 4.1.5 on 2023-02-06 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='parent_messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.CharField(max_length=250)),
                ('date_time', models.DateTimeField()),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_firstname', models.CharField(max_length=500)),
                ('parent_lastname', models.CharField(max_length=500)),
                ('parent_fullname', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=250)),
                ('phone_cell', models.CharField(max_length=100)),
                ('phone_work', models.CharField(max_length=100)),
                ('street_address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=250)),
                ('zipcode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_firstname', models.CharField(max_length=250)),
                ('student_lastname', models.CharField(max_length=250)),
                ('student_fullname', models.CharField(max_length=500)),
                ('tuition', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('age', models.DateField()),
                ('photo_url', models.URLField(max_length=250)),
                ('program', models.IntegerField()),
                ('street_address', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=250)),
                ('state', models.CharField(max_length=250)),
                ('zipcode', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='student_documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=250)),
                ('document_url', models.URLField()),
                ('date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drooli.students')),
            ],
        ),
        migrations.CreateModel(
            name='payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_purpose', models.CharField(max_length=250)),
                ('payment_amount', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drooli.students')),
            ],
        ),
        migrations.CreateModel(
            name='emergency_contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_fullname', models.CharField(max_length=250)),
                ('relationship', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drooli.students')),
            ],
        ),
        migrations.CreateModel(
            name='authorized_pickup_people',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=250)),
                ('relationship', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drooli.students')),
            ],
        ),
        migrations.CreateModel(
            name='attendance_records',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_time', models.TimeField()),
                ('checkout_time', models.TimeField()),
                ('date', models.DateField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drooli.students')),
            ],
        ),
    ]
