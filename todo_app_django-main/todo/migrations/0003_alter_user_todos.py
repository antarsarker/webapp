# Generated by Django 4.2.4 on 2023-08-27 06:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_created_at_todo_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='todos',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.todo'),
        ),
    ]
