from django.contrib import admin

from website.models import Communautaire, Diplome, Experience, Item_portfolio, Profil, Skill

class SkillAdmin(admin.ModelAdmin):
    list_display = ('nom', 'capacite', 'categorie')
    list_filter = ('categorie',)
    search_fields = ('nom',)


class DiplomeAdmin(admin.ModelAdmin):
    list_display = ('intitule', 'debut_annee', 'fin_annee')
    list_filter = ('ville',)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'periode_commencement', 'periode_fin')
    list_filter = ('ville',)


admin.site.register(Skill, SkillAdmin)
admin.site.register(Diplome, DiplomeAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Profil)
admin.site.register(Communautaire)
admin.site.register(Item_portfolio)