
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola_app_api', '0002_remove_aluno_atualizado_em'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='codigo_aluno',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
