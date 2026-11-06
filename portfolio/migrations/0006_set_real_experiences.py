from datetime import date

from django.db import migrations


def apply(apps, schema_editor):
    Skill = apps.get_model('portfolio', 'Skill')
    Experience = apps.get_model('portfolio', 'Experience')

    Experience.objects.all().delete()

    def skill(name):
        obj, _ = Skill.objects.get_or_create(name=name)
        return obj

    independent = Experience.objects.create(
        organization='Self-Directed Learning',
        role='Independent Coding & Web Development',
        kind='education',
        start_date=date(2022, 1, 1),
        end_date=None,
        description=(
            "My interest in software development began in 2022 when I started exploring "
            "programming independently as a personal hobby. I focused on learning HTML, "
            "CSS, React, and Next.js, selecting technologies based on my interests and "
            "curiosity.\n\n"
            "Using Visual Studio Code, I experimented with writing code, creating basic "
            "website layouts, and understanding how frontend technologies work together. "
            "During this period, I also gained introductory knowledge of JavaScript and "
            "UI/UX design principles.\n\n"
            "My focus wasn't on launching complete applications or commercial websites. "
            "Instead, I wanted to understand how websites were structured, how code "
            "worked, and how different technologies could be used to create digital "
            "experiences.\n\n"
            "This independent exploration established the foundation for my later formal "
            "education in software engineering."
        ),
    )
    independent.skills.set([skill('HTML'), skill('CSS'), skill('JavaScript'),
                            skill('React'), skill('Next.js')])

    formal = Experience.objects.create(
        organization='Associate Degree Studies',
        role='Software Engineering Education',
        kind='education',
        start_date=date(2026, 1, 1),
        end_date=None,
        description=(
            "Building on my independent interest in coding, I began formal software "
            "engineering studies in 2026 to develop a more comprehensive understanding "
            "of application development.\n\n"
            "Through structured coursework and practical assignments, I've expanded "
            "beyond frontend experimentation into software development methodologies, "
            "backend programming, database management, and application architecture.\n\n"
            "Academic experience includes:\n"
            "- Frontend Development: HTML, CSS, JavaScript, and responsive web development.\n"
            "- Backend Development: Python, Django, and server-side application functionality.\n"
            "- Database Technologies: Working with databases and learning data management concepts.\n"
            "- UI/UX Design: User-centered design, interface planning, and accessibility principles.\n"
            "- Software Development Practices: Agile methodologies, Scrum, project planning, and risk management.\n"
            "- Version Control: Using Git and GitHub to manage code, branches, and collaborative development workflows."
        ),
    )
    formal.skills.set([skill('HTML'), skill('CSS'), skill('JavaScript'),
                       skill('Python'), skill('Django'), skill('SQL'),
                       skill('Github'), skill('Web Development')])

    army = Experience.objects.create(
        organization='U.S. Army',
        role='Staff Sergeant (E-6) — Military Leadership & Technical Instruction',
        kind='experience',
        start_date=date(2008, 1, 1),
        end_date=date(2023, 1, 1),
        description=(
            "Served more than 15 years in the United States Army, gaining extensive "
            "experience in leadership, operational planning, technical instruction, and "
            "problem-solving.\n\n"
            "Following military service, continued working as a civilian instructor, "
            "building on experience teaching complex technical subjects and developing "
            "structured learning environments."
        ),
    )
    army.skills.set([skill('Troubleshooting'), skill('Customer Support')])

    invidious = Experience.objects.create(
        organization='Invidious Entertainment LLC',
        role='Producer & Screenwriter',
        kind='experience',
        start_date=date(2023, 1, 1),
        end_date=None,
        description=(
            "Through Invidious Entertainment LLC, I pursue filmmaking, screenwriting, "
            "and creative development, combining storytelling with project management "
            "and visual communication.\n\n"
            "My background in film production has strengthened my understanding of "
            "visual design, audience engagement, collaboration, and creative "
            "problem-solving — skills that also influence my approach to software and "
            "interface design."
        ),
    )


def revert(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('portfolio', '0005_set_profile_bio'),
    ]
    operations = [migrations.RunPython(apply, revert)]
