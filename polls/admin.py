from django.contrib import admin
from .models import Article, Memo

# Register your models here.
# @admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content_short','created_at')

    def content_short(self, article):
        return article.content[:10]
    content_short.short_description = '간략한 내용'

admin.site.register(Article, ArticleAdmin)

# admin.py에서 우리가 만든 모델을 등록하는 것을 해보겠습니다!
# 샘플도 확인하시고 다른 툴(제미나이, gpt)을 이용해서 구조를 만들어서 적용도 해보겠습니다
# 1시 50분까지 해보겠습니다!

# 만약 모델 만드는 과정에서 문제가 생기면
# sqlite 파일 삭제해서 진행하시면 됩니다
# 하지만 이게 자주 반복되면 곤란합니다.

# DB초기화 
# sqlite파일 삭제, migrations 내부 파일 삭제(__init__.py는 있어야합니다!!)

@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_important', 'created_at']
    list_filter = ['is_important', 'created_at']
    search_fields = ['title', 'content']
    list_editable = ['is_important']  # 목록에서 바로 수정 가능!