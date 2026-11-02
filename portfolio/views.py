from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProjectForm
from .models import Project, Skill


def project_list(request):
    projects = Project.objects.prefetch_related('skills').all()
    return render(request, 'portfolioTemplates/project_list.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolioTemplates/project_detail.html', {'project': project})


def skill_list(request):
    skills = Skill.objects.prefetch_related('projects').all()
    return render(request, 'portfolioTemplates/skill_list.html', {'skills': skills})


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            return redirect('portfolio:project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'portfolioTemplates/project_form.html', {'form': form})
