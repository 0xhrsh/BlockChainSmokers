from django.contrib import admin
from .models import Candidate, Constituency, Party, Profile


# Register your models here.
class ConstituencyAdmin(admin.ModelAdmin):
    list_display = ['name',]


    class Meta:
        model = Constituency
        fields = '__all__'


admin.site.register(Profile)
admin.site.register(Constituency, ConstituencyAdmin)
admin.site.register(Candidate)
admin.site.register(Party)
