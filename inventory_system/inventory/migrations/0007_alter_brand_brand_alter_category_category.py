# Generated by Django 5.1.2 on 2024-10-17 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0006_alter_product_time_stamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand',
            field=models.CharField(choices=[('LENOVO', 'Lenovo'), ('HP', 'HP'), ('DELL', 'Dell'), ('APPLE', 'Apple'), ('ASUS', 'Asus'), ('ACER', 'Acer'), ('SAMSUNG', 'Samsung'), ('MICROSOFT', 'Microsoft'), ('TOSHIBA', 'Toshiba'), ('SONY', 'Sony'), ('LG', 'LG'), ('PANASONIC', 'Panasonic'), ('CANON', 'Canon'), ('STEELCASE', 'Steelcase'), ('HERMAN_MILLER', 'Herman Miller'), ('HAWORTH', 'Haworth'), ('HON', 'HON'), ('ALLSTEEL', 'Allsteel'), ('KNOLL', 'Knoll'), ('AERON', 'Aeron'), ('XCHAIR', 'XChair'), ('FLEXISPOT', 'FlexiSpot'), ('ERGOTECH', 'Ergotech'), ('STABILO', 'Stabilo'), ('PAPER_MATE', 'Paper Mate'), ('BIC', 'BIC'), ('3M', '3M'), ('PENTEL', 'Pentel'), ('FABER_CASTELL', 'Faber-Castell'), ('DYMO', 'Dymo'), ('POST_IT', 'Post-it'), ('QUILL', 'Quill'), ('EXPO', 'Expo'), ('PARKER', 'Parker'), ('HUSKY', 'Husky'), ('HON_STORAGE', 'HON Storage'), ('SAFCO', 'Safco'), ('GLADIATOR', 'Gladiator')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('ELECTRONIC', 'Electronic'), ('COMPUTER', 'Computer'), ('PRINTER', 'Printer'), ('SCANNER', 'Scanner'), ('MONITOR', 'Monitor'), ('MOUSE', 'Mouse'), ('KEYBOARD', 'Keyboard'), ('HEADPHONES', 'Headphones'), ('PAPER', 'Paper'), ('STATIONERY', 'Stationery'), ('PEN', 'Pen'), ('FOLDER', 'Folder'), ('NOTEBOOK', 'Notebook'), ('MARKER', 'Marker'), ('TABLE', 'Table'), ('CHAIR', 'Chair'), ('CABINET', 'Cabinet'), ('SHELF', 'Shelf'), ('DESK', 'Desk'), ('SOFA', 'Sofa'), ('OFFICE', 'Office'), ('OTHER', 'Other')], max_length=255, null=True),
        ),
    ]
