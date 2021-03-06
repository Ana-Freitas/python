# Generated by Django 2.0.7 on 2018-08-02 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0001_initial'),
        ('products', '0003_auto_20180731_1653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Produto'},
        ),
        migrations.AddField(
            model_name='product',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=False, to='provider.Provider'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, verbose_name='Descrição'),
        ),
    ]
