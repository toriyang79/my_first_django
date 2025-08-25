from django.contrib import admin
from .models import Article, Memo

# Register your models here.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']  # 목록에 표시할 필드
    search_fields = ['title', 'content']  # 검색 가능한 필드
    list_filter = ['created_at']  # 필터 옵션


# admin.site.register(Article, ArticleAdmin)

# polls/admin.py에 추가
@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_important', 'created_at']
    list_filter = ['is_important', 'created_at']
    search_fields = ['title', 'content']
    list_editable = ['is_important']  # 목록에서 바로 수정 가능!
