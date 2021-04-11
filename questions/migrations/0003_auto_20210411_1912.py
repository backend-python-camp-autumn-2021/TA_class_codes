# Generated by Django 3.1 on 2021-04-11 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0002_answer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answered_at',
        ),
        migrations.AddField(
            model_name='questions',
            name='correct_choice',
            field=models.IntegerField(choices=[(1, 'Choice 1'), (2, 'Choice 2'), (3, 'Choice 3'), (4, 'Choice 4')], default=1),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('result', models.FloatField(null=True)),
                ('answered_at', models.DateTimeField(auto_now_add=True)),
                ('answers', models.ManyToManyField(to='questions.Answer')),
                ('questions', models.ManyToManyField(to='questions.Questions')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
