
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escola_app_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aluno',
            name='atualizado_em',
        ),
    ]
