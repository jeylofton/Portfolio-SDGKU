from django.db import migrations


BIO_PRIMARY = (
    "I'm Jey Lofton, a Vertical Software Designer and developer with a passion "
    "for building practical, user-focused software solutions for small "
    "businesses and entrepreneurs.\n\n"
    "My professional background spans military service, education, filmmaking, "
    "and technology. As a U.S. Army veteran and former instructor, I developed "
    "a strong foundation in leadership, problem-solving, strategic planning, "
    "and breaking down complex information into manageable solutions.\n\n"
    "In 2022, I began teaching myself to code, driven by a desire to understand "
    "how software works and how technology can solve everyday business "
    "challenges. What started as independent learning developed into a passion "
    "for designing and building websites, web applications, and business "
    "management platforms."
)

BIO_SECONDARY = (
    "Today, I combine my experience in leadership, instructional design, and "
    "creative storytelling with software development to build digital solutions "
    "that prioritize functionality, accessibility, and user experience.\n\n"
    "My approach is simple: understand the problem, design a practical "
    "solution, and build technology that serves a purpose."
)


def set_bio(apps, schema_editor):
    Profile = apps.get_model('portfolio', 'Profile')
    profile = Profile.objects.first()
    if profile is None:
        Profile.objects.create(
            name='Jey Lofton',
            role='Vertical Software Designer',
            bio_primary=BIO_PRIMARY,
            bio_secondary=BIO_SECONDARY,
            email='jeylofton@gmail.com',
        )
        return
    profile.bio_primary = BIO_PRIMARY
    profile.bio_secondary = BIO_SECONDARY
    profile.save()


def unset_bio(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ('portfolio', '0004_set_profile_identity'),
    ]
    operations = [migrations.RunPython(set_bio, unset_bio)]
