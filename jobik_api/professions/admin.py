import django.contrib

import professions.models

__all__ = []


@django.contrib.admin.register(professions.models.CategoriesModel)
class CategoriesAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        professions.models.CategoriesModel.name.field.name,
        professions.models.CategoriesModel.is_published.field.name,
    )
    list_editable = (
        professions.models.CategoriesModel.is_published.field.name,
    )


@django.contrib.admin.register(professions.models.ProfessionsModel)
class ProfessionAdmin(django.contrib.admin.ModelAdmin):
    list_display = (
        professions.models.ProfessionsModel.name.field.name,
        professions.models.ProfessionsModel.is_published.field.name,
        professions.models.ProfessionsModel.category.field.name,
    )
    list_editable = (
        professions.models.ProfessionsModel.is_published.field.name,
    )
    list_display_links = (
        professions.models.ProfessionsModel.category.field.name,
    )
