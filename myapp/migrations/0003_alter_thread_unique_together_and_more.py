# Generated by Django 5.0.2 on 2024-03-22 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_cargaragedata_thread_chatmessage'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='thread',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='chatmessage',
            name='thread',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to='myapp.thread'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='first_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thread_first_person', to='myapp.profile'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='second_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='thread_second_person', to='myapp.profile'),
        ),
        migrations.AddConstraint(
            model_name='thread',
            constraint=models.UniqueConstraint(fields=('first_person', 'second_person'), name='unique_thread'),
        ),
    ]
