from django.db import models


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('database', 'Database'),
        ('tools', 'Tools'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    icon = models.ImageField(upload_to='skills/', blank=True, null=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    skills = models.ManyToManyField(Skill, related_name='projects', blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Experience(models.Model):
    KIND_CHOICES = [
        ('experience', 'Experience'),
        ('education', 'Education'),
    ]

    organization = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    description = models.TextField()
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default='experience')
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, related_name='experiences', blank=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f'{self.role} @ {self.organization}'

    @property
    def date_range(self):
        start = self.start_date.strftime('%B %Y')
        end = self.end_date.strftime('%B %Y') if self.end_date else 'Present'
        return f'{start} - {end}'


class Profile(models.Model):
    name = models.CharField(max_length=120, default='My Name')
    role = models.CharField(max_length=120, default='My role as dev')
    bio_primary = models.TextField(blank=True)
    bio_secondary = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField(blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'

    def __str__(self):
        return self.name
