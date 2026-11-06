from django.contrib import admin

from .models import Experience, Profile, Project, Skill


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'featured', 'created_at')
    list_filter = ('featured', 'skills')
    search_fields = ('title', 'description')
    filter_horizontal = ('skills',)


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'organization', 'kind', 'start_date', 'end_date')
    list_filter = ('kind',)
    search_fields = ('role', 'organization', 'description')
    filter_horizontal = ('skills',)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'email')
