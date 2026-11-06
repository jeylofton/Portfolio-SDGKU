from datetime import date

from django.db import migrations


def seed(apps, schema_editor):
    Profile = apps.get_model('portfolio', 'Profile')
    Skill = apps.get_model('portfolio', 'Skill')
    Project = apps.get_model('portfolio', 'Project')
    Experience = apps.get_model('portfolio', 'Experience')

    if not Profile.objects.exists():
        Profile.objects.create(
            name='Jey Lofton',
            role='Vertical Software Designer',
            bio_primary='',
            bio_secondary='',
            email='hello@example.com',
        )

    skill_names = ['HTML', 'CSS', 'JavaScript', 'Python', 'Django', 'Github', 'SQL',
                'Web Development', 'Troubleshooting', 'Customer Support', 'Hardware Setup']
    skills = {name: Skill.objects.get_or_create(name=name)[0] for name in skill_names}

    if not Project.objects.exists():
        p1 = Project.objects.create(title='Pet shop project',
                                    description='Description for pet shop project goes here')
        p1.skills.set([skills['HTML'], skills['CSS']])

        p2 = Project.objects.create(title='Coffee',
                                    description='Description for Coffee goes here')
        p2.skills.set([skills['HTML'], skills['Github'], skills['JavaScript'], skills['CSS']])

        p3 = Project.objects.create(title='E-commerce',
                                    description='Description for E-commerce goes here')
        p3.skills.set([skills['HTML'], skills['Python'], skills['Django'],
                    skills['Github'], skills['JavaScript'], skills['CSS']])

    if not Experience.objects.exists():
        e1 = Experience.objects.create(
            organization='University of Technology',
            role='Bachelor of Science in Computer Science',
            description='Focused on software engineering, web development, databases, and user-centered design. Completed projects in Python, JavaScript, and full-stack application development.',
            kind='education',
            start_date=date(2021, 9, 1),
            end_date=date(2025, 6, 1),
        )
        e1.skills.set([skills['Python'], skills['SQL'], skills['Web Development']])

        e2 = Experience.objects.create(
            organization='Brightcode Studio',
            role='Web Development Intern',
            description='Worked on responsive web interfaces, developed front-end components, and collaborated with designers to improve the user experience of client projects.',
            kind='experience',
            start_date=date(2024, 6, 1),
            end_date=date(2024, 8, 1),
        )
        e2.skills.set([skills['HTML'], skills['CSS'], skills['JavaScript']])

        e3 = Experience.objects.create(
            organization='Campus IT Support Center',
            role='IT Support Assistant',
            description='Provided technical assistance to students and staff, troubleshoot hardware and software issues, and maintained a smooth digital learning environment.',
            kind='experience',
            start_date=date(2022, 9, 1),
            end_date=date(2024, 5, 1),
        )
        e3.skills.set([skills['Troubleshooting'], skills['Customer Support'], skills['Hardware Setup']])


def unseed(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('portfolio', '0002_profile_experience'),
    ]
    operations = [migrations.RunPython(seed, unseed)]
