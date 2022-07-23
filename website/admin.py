from django.contrib import admin
from website.models import Community, Education, Experience, ItemPortfolio, Profile


class EducationAdmin(admin.ModelAdmin):
    list_display = ('diploma', 'start_year', 'end_year')
    list_filter = ('city',)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('role', 'experience_start', 'experience_end')
    list_filter = ('city',)


class CommunityAdmin(admin.ModelAdmin):
    list_display = ('community_role', 'community_start', 'community_end')
    list_filter = ('city',)


admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Profile)
admin.site.register(Community, CommunityAdmin)
admin.site.register(ItemPortfolio)
