# Generated by Django 4.0.4 on 2022-06-30 18:07

from django.db import migrations, models
import produto.models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0009_produto_desconto'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem_principal',
            field=models.ImageField(blank=True, null=True, upload_to=produto.models.upload_image_book),
        ),
    ]
