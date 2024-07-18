# Generated by Django 5.0.7 on 2024-07-18 11:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpertRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=255)),
                ('firstname', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=6)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=20)),
                ('district', models.CharField(choices=[('bundibugyo', 'Bundibugyo'), ('gulu', 'Gulu'), ('jinja', 'Jinja'), ('kabarole', 'Kabarole'), ('kampala', 'Kampala'), ('lira', 'Lira'), ('masaka', 'Masaka'), ('mpigi', 'Mpigi'), ('mukono', 'Mukono'), ('soroti', 'Soroti'), ('wakiso', 'Wakiso')], max_length=20)),
                ('country', models.CharField(choices=[('uganda', 'Uganda'), ('tanzania', 'Tanzania'), ('kenya', 'Kenya')], max_length=20)),
                ('knowledge', models.JSONField()),
                ('experience', models.JSONField()),
                ('achievements', models.TextField()),
                ('references', models.TextField()),
                ('user_type', models.CharField(default='expert', max_length=20)),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='InvestmentDeal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=255)),
                ('funding_goal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('valuation', models.DecimalField(decimal_places=2, max_digits=10)),
                ('terms', models.TextField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Funded', 'Funded')], default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Investor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('individual', 'Individual'), ('organization', 'Organization')], max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=50)),
                ('capital', models.CharField(max_length=100)),
                ('information', models.TextField()),
                ('password', models.CharField(max_length=128)),
                ('surname', models.CharField(blank=True, max_length=100, null=True)),
                ('firstname', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=10, null=True)),
                ('company', models.CharField(blank=True, max_length=100, null=True)),
                ('tourism', models.BooleanField(default=False)),
                ('media', models.BooleanField(default=False)),
                ('commercial', models.BooleanField(default=False)),
                ('estate', models.BooleanField(default=False)),
                ('manufacturing', models.BooleanField(default=False)),
                ('education', models.BooleanField(default=False)),
                ('health', models.BooleanField(default=False)),
                ('wholesale', models.BooleanField(default=False)),
                ('user_type', models.CharField(default='investor', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
                ('district', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=255)),
                ('user_type', models.CharField(default='entrepreneur', max_length=20)),
                ('role_in_company', models.CharField(choices=[('founder', 'Founder'), ('owner', 'Owner'), ('director', 'Director')], max_length=100)),
                ('password', models.CharField(max_length=128)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ConsultationPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('package_type', models.CharField(choices=[('Hourly Rate', 'Hourly Rate'), ('Retainer-based', 'Retainer-based'), ('Project-Based', 'Project-Based'), ('Specialised Challenge', 'Specialised Challenge'), ('Growth Strategy', 'Growth Strategy')], max_length=50)),
                ('package_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bizconnect.expertregistration')),
            ],
        ),
        migrations.CreateModel(
            name='InvestmentFunds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('industry', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Equity', 'Equity'), ('Debt', 'Debt'), ('Convertible Note', 'Convertible Note')], max_length=100)),
                ('investment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contact_method', models.CharField(choices=[('Email', 'Email'), ('Phone', 'Phone')], max_length=100)),
                ('notes', models.TextField()),
                ('supporting_documents', models.FileField(blank=True, null=True, upload_to='supporting_documents/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('investment_deal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investment_fund', to='Bizconnect.investmentdeal')),
                ('investor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investment_fund', to='Bizconnect.investor')),
            ],
        ),
        migrations.AddField(
            model_name='investmentdeal',
            name='entrepreneur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='investment_deals', to='Bizconnect.registration'),
        ),
        migrations.CreateModel(
            name='BusinessIdeas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('industry', models.CharField(max_length=100)),
                ('target_market', models.TextField()),
                ('business_model', models.TextField()),
                ('projections', models.TextField()),
                ('goals', models.TextField(blank=True, null=True)),
                ('pitch_deck', models.FileField(blank=True, null=True, upload_to='attachments/pitch_deck/')),
                ('plan', models.FileField(blank=True, null=True, upload_to='attachments/plan/')),
                ('video', models.FileField(blank=True, null=True, upload_to='attachments/video/')),
                ('support', models.FileField(blank=True, null=True, upload_to='attachments/support/')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('entrepreneur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='business_ideas', to='Bizconnect.registration')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('type', models.CharField(choices=[('Article', 'Article'), ('Template', 'Template'), ('Practice', 'Best Practice')], max_length=100)),
                ('supporting_documents', models.FileField(blank=True, null=True, upload_to='supporting_documents/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('expert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource', to='Bizconnect.expertregistration')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduledMeeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('expert_name', models.CharField(max_length=255)),
                ('consultation_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('link', models.URLField()),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Denied', 'Denied')], default='Pending', max_length=10)),
                ('denial_reason', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('consultation_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bizconnect.consultationpackage')),
                ('entrepreneur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_meeting', to='Bizconnect.registration')),
            ],
        ),
        migrations.CreateModel(
            name='ReplyRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('text_area', models.TextField()),
                ('status', models.CharField(choices=[('SENT', 'Sent'), ('NOT_SENT', 'Not Sent')], default='NOT_SENT', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('meeting', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bizconnect.scheduledmeeting')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_idea', models.CharField(max_length=255)),
                ('industry', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('target_market', models.TextField()),
                ('consultation_time', models.TimeField()),
                ('consultation_date', models.DateField()),
                ('urgency_level', models.CharField(max_length=10)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='attachments/')),
                ('comments', models.TextField(blank=True, null=True)),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Scheduled', 'Scheduled'), ('Concluded', 'Concluded')], default='Pending', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('assigned_expert', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_requests', to='Bizconnect.expertregistration')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Bizconnect.registration')),
            ],
        ),
        migrations.AddField(
            model_name='scheduledmeeting',
            name='service_request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedule_meeting', to='Bizconnect.servicerequest'),
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_type', models.CharField(choices=[('entrepreneur', 'Entrepreneur'), ('expert', 'Expert'), ('investor', 'Investor')], max_length=20)),
                ('email', models.EmailField(blank=True, default='', error_messages={'unique': 'A user with that email already exists.'}, max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='registration',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='investor',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='expertregistration',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
