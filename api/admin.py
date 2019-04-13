from django.contrib import admin

# Register your models here.

from api.models import Profile, Room

admin.site.site_header = 'Администрирование Online Cinema'
admin.site.site_title = 'Административный сайт Online Cinema'


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'standart_user_id',
        'login',
        'email',
        'current_room_id'
    )
    search_fields = (
        'login',
        'email',
    )
    readonly_fields = (
        'standart_user_id',
        'login',
        'email',
    )
    exclude = (
        'password',
    )


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'type',
        'creator',
        'created_at'
    )
    search_fields = (
        'id',
        'name',
        'creator'
    )
    readonly_fields = (
        'id',
        'name',
        'type',
        'creator',
        'created_at'
    )