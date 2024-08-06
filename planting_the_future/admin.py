from django.contrib import admin
from .models import Account, Profile, Tree, PlantedTree

admin.site.register(Profile)

class AccountAdmin(admin.ModelAdmin):
    # Admin configuration for the Account model
    list_display = ('name', 'created', 'active')
    search_fields = ('name',)
    list_filter = ('active',)

    def get_users(self, obj):
        # Returns a comma-separated list of usernames associated with the account
        return ", ".join([user.username for user in obj.users.all()])
    get_users.short_description = 'Users'

admin.site.register(Account, AccountAdmin)

class TreeAdmin(admin.ModelAdmin):
    # Admin configuration for the Tree model
    list_display = ('name', 'scientific_name')

admin.site.register(Tree, TreeAdmin)

class PlantedTreeAdmin(admin.ModelAdmin):
    # Admin configuration for the PlantedTree model
    list_display = ('tree', 'user', 'age', 'planted_at', 'account', 'location_lat', 'location_lon')
    list_filter = ('tree', 'user', 'account')
    search_fields = ('tree__name', 'user__username')

    def get_queryset(self, request):
        # Optimizes the queryset to use select_related for related fields
        qs = super().get_queryset(request)
        return qs.select_related('tree', 'user', 'account')

    def user_name(self, obj):
        # Returns the username of the user who planted the tree
        return obj.user.username
    user_name.short_description = 'User'

admin.site.register(PlantedTree, PlantedTreeAdmin)
