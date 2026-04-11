from django.contrib import admin
from .models import About,SocialLink

# Register your models here.


class AboutAdmin(admin.ModelAdmin):
  def has_add_permission(self, request):
    count=About.objects.all().count()
    if count==0:
      return True
    return False

admin.site.register(About,AboutAdmin)


#to remove add button from the django admin
#we have overwrite the function modeladmin
#only one about us we can add

admin.site.register(SocialLink)
