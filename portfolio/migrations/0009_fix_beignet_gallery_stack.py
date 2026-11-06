from django.db import migrations


TITLE = 'Beignet Gallery'
SKILL_NAMES = ['Next.js', 'TypeScript', 'Bootstrap', 'PostgreSQL', 'Supabase']


def fix_stack(apps, schema_editor):
    Project = apps.get_model('portfolio', 'Project')
    Skill = apps.get_model('portfolio', 'Skill')

    project = Project.objects.filter(title=TITLE).first()
    if project is None:
        return
    skills = [Skill.objects.get_or_create(name=name)[0] for name in SKILL_NAMES]
    project.skills.set(skills)


def revert_stack(apps, schema_editor):
    Project = apps.get_model('portfolio', 'Project')
    Skill = apps.get_model('portfolio', 'Skill')

    project = Project.objects.filter(title=TITLE).first()
    if project is None:
        return
    previous = ['Django', 'Python', 'PostgreSQL', 'HTML/CSS', 'JavaScript']
    skills = [Skill.objects.get_or_create(name=name)[0] for name in previous]
    project.skills.set(skills)


class Migration(migrations.Migration):
    dependencies = [
        ('portfolio', '0008_add_beignet_gallery_project'),
    ]
    operations = [migrations.RunPython(fix_stack, revert_stack)]
