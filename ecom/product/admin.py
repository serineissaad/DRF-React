from django.contrib import admin
from . import models

@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'status', 'slug', 'author')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(models.Tenant)
admin.site.register(models.Owner)
admin.site.register(models.Amenity)
admin.site.register(models.Property)
admin.site.register(models.Images)
admin.site.register(models.Booking)
admin.site.register(models.Review)
admin.site.register(models.Payment)
admin.site.register(models.City)
