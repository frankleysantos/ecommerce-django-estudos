# Generated by Django 4.0.4 on 2022-06-27 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(blank=True, upload_to='fotos/produtos/%Y/%m')),
                ('produto_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='produto.produto')),
            ],
        ),
    ]
