# Generated by Django 3.1.7 on 2021-02-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TamilQuestions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=100)),
                ('Option1', models.CharField(max_length=50)),
                ('Option2', models.CharField(max_length=50)),
                ('Option3', models.CharField(max_length=50)),
                ('Option4', models.CharField(max_length=50)),
                ('Answer', models.CharField(max_length=50)),
            ],
        ),
    ]
