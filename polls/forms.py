from django import forms
from .models import Memo


class MemoForm(forms.ModelForm):
    """Model과 자동 연결되는 Form"""
    class Meta:
        model = Memo  # 연결할 모델
        fields = ['title', 'content', 'is_important']  # 사용할 필드

        # 위젯 커스터마이징 (선택사항)
        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 40}),
        }

        # 에러 메시지 커스터마이징 (선택사항)
        error_messages = {
            'title': {
                'required': '제목은 반드시 입력해야 합니다.',
                'max_length': '제목이 너무 깁니다.',
            },
        }
    