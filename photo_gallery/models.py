# photo_gallery/models.py
from django.db import models                # Django ORM에서 모델 만들 때 필요한 기본 클래스
from django.contrib.auth.models import User # Django 기본 사용자 모델 (작성자/좋아요 등 연결)
from django.conf import settings            # settings.py의 설정 불러오기 (MEDIA_ROOT 등)
from PIL import Image                       # Pillow 라이브러리 (이미지 처리)
import os                                   # 파일 경로 및 삭제에 사용
from datetime import date                   # 사진 촬영일 기본값으로 사용

class DailyPhoto(models.Model):
    """하루 한 장 사진 모델"""

    # 카테고리 선택지
    CATEGORY_CHOICES = [
        ('daily', '일상'),
        ('food', '음식'),
        ('travel', '여행'),
        ('people', '사람'),
        ('nature', '자연'),
        ('other', '기타'),
    ]

    # 작성자: User 모델과 연결 (1:N 관계)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,      # 작성자가 삭제되면 사진도 같이 삭제
        related_name='photos'          # user.photos 로 해당 사용자의 사진 목록 접근 가능
    )

    # 사진 업로드 필드
    photo = models.ImageField(
        '사진',
        upload_to='photos/%Y/%m/%d/'   # 업로드 시 연월일 폴더에 저장됨
    )

    # 썸네일 이미지 (자동 생성됨, 사용자가 직접 수정 불가)
    thumbnail = models.ImageField(
        '썸네일',
        upload_to='thumbnails/%Y/%m/%d/',
        blank=True,
        editable=False                 # 폼에서 수정 불가
    )

    # 사진 정보
    title = models.CharField('제목', max_length=100)             # 사진 제목
    description = models.TextField('설명', max_length=500, blank=True) # 설명 (선택 사항)
    photo_date = models.DateField('촬영일', default=date.today)   # 촬영 날짜
    category = models.CharField(
        '카테고리',
        max_length=10,
        choices=CATEGORY_CHOICES,      # 위에서 정의한 카테고리 목록
        default='daily'                # 기본값은 '일상'
    )

    # 공개 여부 (True면 공개, False면 비공개)
    is_public = models.BooleanField('공개', default=True)

    # 좋아요 (여러 User가 같은 사진을 좋아요 가능, 다대다 관계)
    likes = models.ManyToManyField(
        User,
        related_name='liked_photos',   # user.liked_photos 로 접근 가능
        blank=True
    )

    # 자동 생성되는 날짜 정보
    created_at = models.DateTimeField('업로드일', auto_now_add=True) # 처음 저장될 때
    updated_at = models.DateTimeField('수정일', auto_now=True)      # 수정될 때마다 업데이트

    class Meta:
        verbose_name = '일일 사진'          # 관리자(admin)에서 표시될 단수 이름
        verbose_name_plural = '일일 사진들' # 관리자(admin)에서 표시될 복수 이름
        ordering = ['-photo_date', '-created_at'] # 최신 사진이 먼저 나오도록 정렬

    def __str__(self):
        # 객체를 문자열로 표현할 때: [작성자] 제목 (촬영일)
        return f'[{self.author.username}] {self.title} ({self.photo_date})'



    def save(self, *args, **kwargs):
        """저장할 때 썸네일이 없으면 자동으로 생성"""
        super().save(*args, **kwargs)
        if self.photo and not self.thumbnail:
            self.create_thumbnail()

    def create_thumbnail(self):
        """Pillow로 썸네일 생성"""
        img = Image.open(self.photo.path)   # 원본 이미지 열기

        # PNG 같은 투명 배경 이미지를 RGB로 변환
        if img.mode in ('RGBA', 'P'):
            img = img.convert('RGB')

        # 썸네일 크기 지정 (300x300)
        img.thumbnail((300, 300), Image.Resampling.LANCZOS)

        # 썸네일 파일명 만들기
        thumb_name = os.path.basename(self.photo.name)   # 원본 파일 이름
        thumb_name = f'thumb_{thumb_name}'               # 앞에 thumb_ 붙이기
        thumb_path = os.path.join('thumbnails',
                                  self.photo_date.strftime('%Y/%m/%d'),
                                  thumb_name)

        # MEDIA_ROOT 기준 전체 경로
        full_thumb_path = os.path.join(settings.MEDIA_ROOT, thumb_path)

        # 경로에 필요한 폴더 없으면 자동 생성
        os.makedirs(os.path.dirname(full_thumb_path), exist_ok=True)

        # JPEG로 썸네일 저장 (화질 85)
        img.save(full_thumb_path, 'JPEG', quality=85)

        # 모델 thumbnail 필드에 저장된 경로 업데이트
        self.thumbnail = thumb_path
        super().save(update_fields=['thumbnail'])

    def delete(self, *args, **kwargs):
        """객체 삭제 시 실제 파일도 같이 삭제"""
        # 삭제할 파일 경로 기억
        photo_path = self.photo.path if self.photo else None
        thumb_path = self.thumbnail.path if self.thumbnail else None

        # DB에서 레코드 삭제
        super().delete(*args, **kwargs)

        # 파일 삭제
        if photo_path and os.path.exists(photo_path):
            os.remove(photo_path)
        if thumb_path and os.path.exists(thumb_path):
            os.remove(thumb_path)
