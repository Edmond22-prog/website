from django.shortcuts import render
from django.views.generic import DetailView
from website.models import Communautaire, Diplome, Experience, Item_portfolio, Profil, Skill



def index(request):
    profil = Profil.objects.first()
    liste_skill_langage = Skill.objects.filter(categorie="Langage")
    liste_skill_techno = Skill.objects.filter(categorie="Technologie")
    liste_experience = Experience.objects.all().order_by('-id')
    liste_diplome = Diplome.objects.all().order_by('-debut_annee')
    liste_communautaire = Communautaire.objects.all().order_by('-id')
    liste_item_portfolio = Item_portfolio.objects.all()
    return render(request, 'website/index.html', {
        'profil': profil,
        'liste_skill_langage': liste_skill_langage,
        'liste_skill_techno': liste_skill_techno,
        'liste_experience': liste_experience,
        'liste_diplome': liste_diplome,
        'liste_communautaire': liste_communautaire,
        'liste_item_portfolio': liste_item_portfolio,
    })


class PortfolioDetailView(DetailView):
    model = Item_portfolio
    template_name = 'website/portfolio_details.html'