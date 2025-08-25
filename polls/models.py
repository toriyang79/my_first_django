from re import T
from turtle import title
from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField('이게 이렇게 나와요', max_length=200)
    content = models.TextField('내용')
    created_at = models.DateTimeField('작성일', auto_now_add=True)
    updated_at = models.DateTimeField('수정일', auto_now=True)

    def __str__(self):
        return "__str__통해서   요롷게 나옵니다."+ self.title

    class Meta:
        verbose_name = '아티클'
        verbose_name_plural = '아티클들'


class Memo(models.Model):
    # 제목, 내용, 중요여부, 생성일
    title = models.CharField(max_length=200)  # 제목
    content = models.TextField('내용')  # 내용(빈칸 허용)
    is_important = models.BooleanField('중요', default=False) # 중요 여부 (체크박스)
    created_at = models.DateTimeField('생성일', auto_now_add=True) # 생성일(자동)


    def __str__(self):
         return self.title

    class Meta:
        verbose_name = '메모'
        verbose_name_plural = '메모 목록'
        ordering = ['-created_at']  # 최신순 정렬