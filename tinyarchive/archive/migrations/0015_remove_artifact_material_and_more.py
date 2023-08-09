# Generated by Django 4.0.5 on 2023-08-08 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0014_artifact_origin_function'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artifact',
            name='material',
        ),
        migrations.RemoveField(
            model_name='artifact',
            name='origin_function',
        ),
        migrations.AddField(
            model_name='artifact',
            name='Level',
            field=models.CharField(choices=[('easy', 'Easy'), ('moderate', 'Moderate'), ('experienced', 'Experienced'), ('difficult', 'Difficult'), ('expert', 'Expert')], default='easy', max_length=50),
        ),
        migrations.AddField(
            model_name='artifact',
            name='country_of_origin',
            field=models.TextField(blank='True', max_length=10),
        ),
    ]
