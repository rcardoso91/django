from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('codigo_aluno', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=80)),
                ('data_nascimento', models.DateField()),
                ('criado_em', models.DateField(auto_now=True)),
                ('atualizado_em', models.DateField(null=True)),
                ('endereco_rua', models.CharField(max_length=80)),
                ('endereco_numero', models.IntegerField()),
            ],
        ),
    ]
