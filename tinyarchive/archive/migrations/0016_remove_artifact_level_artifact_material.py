# Generated by Django 4.0.5 on 2023-08-08 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('archive', '0015_remove_artifact_material_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artifact',
            name='Level',
        ),
        migrations.AddField(
            model_name='artifact',
            name='material',
            field=models.CharField(choices=[('other', 'Other'), ('plastic', 'Plastic'), ('ceramic', 'Ceramic'), ('glass', 'Glass'), ('metal', 'Metal')], default='glass', max_length=50),
        ),
    ]
