import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm, ProjectForm
from .models import Experience, Profile, Project, Skill

logger = logging.getLogger(__name__)


def _profile():
    return Profile.objects.first()


def about(request):
    return render(request, 'portfolioTemplates/about.html', {
        'profile': _profile(),
        'active': 'about',
    })


def project_list(request):
    projects = Project.objects.prefetch_related('skills').all()
    return render(request, 'portfolioTemplates/project_list.html', {
        'projects': projects,
        'profile': _profile(),
        'active': 'projects',
    })


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolioTemplates/project_detail.html', {
        'project': project,
        'profile': _profile(),
        'active': 'projects',
    })


def experience_list(request):
    experiences = Experience.objects.prefetch_related('skills').all()
    return render(request, 'portfolioTemplates/experience_list.html', {
        'experiences': experiences,
        'profile': _profile(),
        'active': 'experience',
    })


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            visitor_email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message_body = form.cleaned_data['message']

            recipient = getattr(settings, 'CONTACT_RECIPIENT_EMAIL', None)
            from_email = getattr(settings, 'DEFAULT_FROM_EMAIL', None)

            body = (
                f"You received a new message from your portfolio contact form.\n\n"
                f"Name: {name}\n"
                f"Email: {visitor_email}\n"
                f"Subject: {subject}\n\n"
                f"Message:\n{message_body}\n"
            )

            email = EmailMessage(
                subject=f"[Portfolio Contact] {subject}",
                body=body,
                from_email=from_email,
                to=[recipient] if recipient else [],
                reply_to=[visitor_email],
            )
            try:
                email.send(fail_silently=False)
            except Exception:
                logger.exception('Contact form email failed to send')
                messages.error(request, 'Your message could not be sent. Please try again later.')
                return render(request, 'portfolioTemplates/contact.html', {
                    'form': form,
                    'profile': _profile(),
                    'active': 'contact',
                })

            messages.success(request, 'Thank you for reaching out! Your message has been sent successfully.')
            return redirect('portfolio:contact')
    else:
        form = ContactForm()

    return render(request, 'portfolioTemplates/contact.html', {
        'form': form,
        'profile': _profile(),
        'active': 'contact',
    })


def skill_list(request):
    skills = Skill.objects.prefetch_related('projects').all()
    return render(request, 'portfolioTemplates/skill_list.html', {
        'skills': skills,
        'profile': _profile(),
        'active': 'skills',
    })


def add_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save()
            return redirect('portfolio:project_detail', pk=project.pk)
    else:
        form = ProjectForm()
    return render(request, 'portfolioTemplates/project_form.html', {
        'form': form,
        'profile': _profile(),
        'active': 'projects',
    })
