from django.contrib import admin
from . import models

admin.site.register(models.Sentence)
admin.site.register(models.Project)

# @admin.register(models.Project)
# class ProjectAdmin(admin.ModelAdmin):
#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'annotator':
#             annotator = models.Group.objects.filter(name="Annotator").first()
#             kwargs["queryset"] = models.User.objects.filter(groups__contains=annotator)
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)

