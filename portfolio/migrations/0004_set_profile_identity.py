from django.db import migrations


def set_identity(apps, schema_editor):
    Profile = apps.get_model('portfolio', 'Profile')
    profile = Profile.objects.first()
    if profile is None:
        Profile.objects.create(
            name='Jey Lofton',
            role='Vertical Software Designer',
            bio_primary='',
            bio_secondary='',
            email='jeylofton@gmail.com',
        )
        return
    if profile.name in ('', 'My Name'):
        profile.name = 'Jey Lofton'
    if profile.role in ('', 'My rol as dev'):
        profile.role = 'Vertical Software Designer'
    profile.save()


def unset_identity(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('portfolio', '0003_seed_placeholder_data'),
    ]
    operations = [migrations.RunPython(set_identity, unset_identity)]
