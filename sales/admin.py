from django.contrib import admin

# Register your models here.
from .models import Pages,Team, Testimonials,Blog,ContactUs,Messages, ImageGrid,Services, Shop,SocialMedia,Company

admin.site.register(Pages)
admin.site.register(Team)
admin.site.register(Testimonials)
admin.site.register(Blog)
admin.site.register(ContactUs)
admin.site.register(Messages)
admin.site.register(ImageGrid)
admin.site.register(Services)
admin.site.register(Shop)
admin.site.register(SocialMedia)
admin.site.register(Company)
