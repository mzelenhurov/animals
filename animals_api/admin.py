from django.contrib import admin
from animals_api.models import Cat, Dog


class MyModelAdmin(admin.ModelAdmin):
    readonly_fields = ('owner',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(owner=request.user)

    def has_change_permission(self, request, obj=None):
        if obj:
            if obj.owner == request.user:
                return True
            return False

    def has_delete_permission(self, request, obj=None):
        if obj:
            if obj.owner == request.user:
                return True
            return False

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'owner', None) is None:
            obj.owner = request.user
        obj.save()


admin.site.register(Cat, MyModelAdmin)
admin.site.register(Dog, MyModelAdmin)
