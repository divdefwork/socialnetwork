from django.contrib import admin

from .models import Post, Comment, UserProfile


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created_on']
    list_display_links = ('author',)
    search_fields = ('author',)
    list_filter = ('author', 'created_on')
    readonly_fields = ('created_on',)

    fieldsets = (
        (None, {
            'fields': (
                ('author', 'created_on'), 'body'
            )
        }),
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'created_on']
    list_display_links = ('author',)
    search_fields = ('author',)
    list_filter = ('author', 'created_on')
    readonly_fields = ('created_on',)

    fieldsets = (
        (None, {
            'fields': (
                ('author', 'created_on'),
            )
        }),
        (None, {
            'fields': (
                ('post', 'comment'),
            )
        }),
    )


admin.site.register(UserProfile)
