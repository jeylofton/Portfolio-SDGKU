from datetime import date

from django.db import migrations


TITLE = 'Beignet Gallery'
START_DATE = date(2026, 5, 1)


def set_date(apps, schema_editor):
    Project = apps.get_model('portfolio', 'Project')
    Project.objects.filter(title=TITLE).update(created_at=START_DATE)


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('portfolio', '0009_fix_beignet_gallery_stack'),
    ]
    operations = [migrations.RunPython(set_date, noop)]
