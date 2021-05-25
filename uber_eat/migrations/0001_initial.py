# Generated by Django 3.2.2 on 2021-05-25 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('Cid', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Cname', models.CharField(max_length=20, null=True)),
                ('Cpassword', models.CharField(default=None, max_length=20)),
                ('Cemail', models.EmailField(default=None, max_length=254)),
                ('Cphone', models.CharField(max_length=20, null=True)),
                ('Caddress', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deliver',
            fields=[
                ('Did', models.IntegerField(primary_key=True, serialize=False)),
                ('Dname', models.CharField(max_length=20, null=True)),
                ('Dphone', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('Oid', models.IntegerField(primary_key=True, serialize=False)),
                ('Ocount', models.IntegerField(default=0, verbose_name='商品數量')),
                ('Oprice', models.IntegerField(default=0, verbose_name='商品總價')),
                ('Ostatus', models.SmallIntegerField(choices=[(1, '正在建立訂單'), (2, '店家出貨'), (3, '外送員領貨'), (4, '外送員抵達'), (5, '消費者領取貨(結束訂單)')], default=1, verbose_name='訂單狀態')),
                ('Ocreated', models.DateTimeField(auto_now_add=True)),
                ('C', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uber_eat.consumer')),
                ('D', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='uber_eat.deliver')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('Sid', models.IntegerField(primary_key=True, serialize=False)),
                ('Sname', models.CharField(max_length=20, null=True)),
                ('Saddress', models.CharField(max_length=20, null=True)),
                ('Sphone', models.CharField(max_length=20, null=True)),
                ('Stransit_price', models.DecimalField(decimal_places=2, default='30', max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Pid', models.IntegerField(primary_key=True, serialize=False)),
                ('Pname', models.CharField(max_length=20, null=True)),
                ('Ptime', models.DateField(null=True)),
                ('Pprice', models.IntegerField(null=True)),
                ('S', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uber_eat.store')),
            ],
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('OGid', models.IntegerField(primary_key=True, serialize=False)),
                ('OGcount', models.IntegerField(default=1, verbose_name='商品數量')),
                ('O', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uber_eat.order')),
                ('P', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uber_eat.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='S',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uber_eat.store'),
        ),
    ]