from django.contrib import admin

from blog.models import *


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    # 列表页以列的形式展示对象,点击标题排序
    list_display = ('title', 'desc', 'click_count')
    # 表示哪些列有链接
    list_display_links = ('title', 'desc')
    # 表示哪些列能够被编辑
    list_editable = ('click_count',)
    # 表示哪些列能够被筛选
    list_filter = ('title', 'desc')
    # 搜索框
    search_fields = ('title', 'desc')
    # 分页
    list_per_page = 10

    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', 'user', 'category', 'tag',)
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend'),
        }),
    )

    class Media:
        js = (
            'blog/js/kindeditor-4.1.12/kindeditor-all-min.js',
            'blog/js/kindeditor-4.1.12/lang/zh-CN.js',
            'blog/js/kindeditor-4.1.12/config.js',
        )


admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Links)
admin.site.register(Ad)
