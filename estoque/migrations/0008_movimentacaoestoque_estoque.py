# Generated by Django 4.2.2 on 2023-07-11 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0007_remove_movimentacaoestoque_estoque'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimentacaoestoque',
            name='estoque',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='estoque.estoque'),
        ),
    ]