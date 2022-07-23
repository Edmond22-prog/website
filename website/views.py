from django.shortcuts import render
from django.views.generic import DetailView
from django.core.mail import send_mail
from website.models import Community, Education, Experience, ItemPortfolio, Profile


def index(request):
    profile = Profile.objects.first()
    experiences = Experience.objects.all().order_by('-id')
    educations = Education.objects.all().order_by('-start_year')
    communities = Community.objects.all().order_by('-id')
    items_portfolio = ItemPortfolio.objects.all()
    return render(request, 'website/index.html', {
        'profile': profile,
        'experiences': experiences,
        'educations': educations,
        'communities': communities,
        'items_portfolio': items_portfolio,
    })


def sending(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        # Envoi du mail
        send_mail(
            subject,
            message,
            email,
            ['edghimakoll@gmail.com'],
        )
        return render(request, 'website/sending_mail.html', {'name': name})
    else:
        return render(request, 'website/sending_mail.html', {})


class PortfolioDetailView(DetailView):
    model = ItemPortfolio
    template_name = 'website/portfolio_details.html'
