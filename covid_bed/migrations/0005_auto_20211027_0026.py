# Generated by Django 3.0.1 on 2021-10-26 18:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('covid_bed', '0004_auto_20211027_0010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='occupied_isolation_beds',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='total_isolation_beds',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='vacant_isolation_beds',
        ),
        migrations.AddField(
            model_name='hospital',
            name='occupied_isolation',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='total_isolation',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='hospital',
            name='update_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='hospital',
            name='vacant_isolation',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='alternative_contact',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='category',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='city',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='contact',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='has_ICU_beds',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='has_ventilators',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='is_new_hospital',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='lat',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='location',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='long',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='occupied_HDU',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Occupied_HDU (High dependency unit) beds'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='occupied_ICU',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='occupied_NMC_reserved',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Occupied NMC (National Medical Commission) reserved'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='occupied_general',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='occupied_oxygen_general',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='total_HDU',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Total_HDU (High dependency unit) beds'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='total_ICU',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='total_NMC_reserved',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Total NMC (National Medical Commission) reserved'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='total_beds',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='total_general',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='total_oxygen_general',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='total_ventilators',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='vacant_HDU',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Vacant_HDU (High dependency unit) beds'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='vacant_ICU',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='vacant_NMC_reserved',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Vacant NMC (National Medical Commission) reserved'),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='vacant_general',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='hospital',
            name='vacant_oxygen_general',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
