# Generated by Django 3.0.7 on 2020-07-05 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0023_auto_20200705_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookmark', to='mainApp.Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='mainApp.Post'),
        ),
        migrations.AlterField(
            model_name='like',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='like', to='mainApp.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='loc',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
