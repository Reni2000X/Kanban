# Generated by Django 5.1.6 on 2025-03-17 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='group',
        ),
        migrations.AddField(
            model_name='task',
            name='board',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='board', to='dashboard.board'),
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('open', 'Open'), ('renaming', 'Renaming'), ('session_prep', 'Session Prep'), ('to_be_recorded', 'To Be Recorded'), ('recorded', 'Recorded'), ('for_post', 'For Post'), ('from_post', 'From Post'), ('leveling', 'Leveling'), ('for_qa', 'For Qa'), ('bugfixing', 'Bugfixing'), ('in_regression', 'In Regression'), ('qa_done', 'Qa Done'), ('ready_for_delivery', 'Ready For Delivery'), ('delivered', 'Delivered'), ('completed_recordings', 'Completed Recordings')], default='open', max_length=25),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
