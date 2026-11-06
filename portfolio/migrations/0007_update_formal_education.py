from datetime import date

from django.db import migrations


NEW_DESCRIPTION = (
    "Currently pursuing a 22-month Associate of Science in Software Development, "
    "building on my previous experience with independently learning frontend "
    "technologies.\n\n"
    "My education focuses on the software development lifecycle, including "
    "designing, developing, testing, debugging, and maintaining software "
    "applications.\n\n"
    "Through coursework and hands-on projects, I'm developing skills in:\n"
    "- Frontend Development: HTML, CSS, JavaScript, and responsive website development.\n"
    "- Backend Development: Python, Django, and server-side application development.\n"
    "- Database Management: Working with databases and data-driven applications.\n"
    "- UI/UX Design: User-centered design, usability, accessibility, and interface planning.\n"
    "- Development Methodologies: Agile, Scrum, software project management, and risk assessment.\n"
    "- Version Control: Git, GitHub, and collaborative development practices.\n\n"
    "My studies emphasize applying programming concepts to practical projects while "
    "developing a stronger understanding of how complete software applications are "
    "designed, built, and maintained."
)


def apply(apps, schema_editor):
    Experience = apps.get_model('portfolio', 'Experience')

    entry = Experience.objects.filter(
        kind='education',
        organization='Associate Degree Studies',
    ).first()

    if entry is None:
        entry = Experience.objects.filter(
            role__icontains='Software Engineering Education',
            kind='education',
        ).first()

    if entry is None:
        entry = Experience(
            kind='education',
            start_date=date(2026, 7, 1),
        )

    entry.organization = 'San Diego Global Knowledge University'
    entry.role = 'Associate of Science in Software Development (ASSD) — Software Development Education'
    entry.description = NEW_DESCRIPTION
    entry.start_date = date(2026, 7, 1)
    entry.end_date = None
    entry.save()


def revert(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('portfolio', '0006_set_real_experiences'),
    ]
    operations = [migrations.RunPython(apply, revert)]
