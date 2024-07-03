# Generated by Django 5.0.3 on 2024-07-01 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bizconnect', '0006_scheduledmeeting'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentFunds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('industry', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('equity', 'Equity'), ('debt', 'Debt'), ('convertible_note', 'Conertible Note')], max_length=100)),
                ('investment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contact_method', models.CharField(choices=[('email', 'Email'), ('phone', 'Phone')], max_length=100)),
                ('notes', models.TextField()),
                ('supporting_documents', models.FileField(blank=True, null=True, upload_to='supporting_documents/')),
            ],
        ),
    ]
