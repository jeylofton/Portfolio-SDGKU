from django.db import migrations


TITLE = 'Beignet Gallery'
DESCRIPTION = (
    'A full-stack catering platform for Beignet Gallery, a New Orleans-inspired '
    'catering company serving weddings, private parties, corporate events, and '
    'weekend pop-ups. The public site handles catering requests, online orders, '
    'event discovery, and a gallery; the staff dashboard covers orders, '
    'customers, catering packages, pop-ups, events, menus, inventory, payments, '
    'expenses, financials, loyalty, campaigns, staff, and SEO/search visibility '
    'settings — plus a Square integration for payouts straight to the business.'
)
IMAGE = 'projects/beignet-gallery.webp'
SKILL_NAMES = ['Python', 'Django', 'PostgreSQL', 'HTML/CSS', 'JavaScript']


def add_project(apps, schema_editor):
    Project = apps.get_model('portfolio', 'Project')
    Skill = apps.get_model('portfolio', 'Skill')

    project, _ = Project.objects.update_or_create(
        title=TITLE,
        defaults={
            'description': DESCRIPTION,
            'image': IMAGE,
            'featured': True,
        },
    )
    skills = [Skill.objects.get_or_create(name=name)[0] for name in SKILL_NAMES]
    project.skills.set(skills)


def remove_project(apps, schema_editor):
    Project = apps.get_model('portfolio', 'Project')
    Project.objects.filter(title=TITLE).delete()


class Migration(migrations.Migration):
    dependencies = [
        ('portfolio', '0007_update_formal_education'),
    ]
    operations = [migrations.RunPython(add_project, remove_project)]
