# Generated by Django 3.2.7 on 2022-04-23 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('have order', '已接单'), ('have clean', '已清洗'), ('repaired', '已维修'), ('finish', '已完成')], default='have order', max_length=20, verbose_name='订单状态'),
        ),
    ]
