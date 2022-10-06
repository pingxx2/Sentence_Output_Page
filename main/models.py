from django.db import models
from django.contrib.auth.models import User

class Sentence(models.Model):
    # 문구 내용
    content = models.TextField("문구")
    # 제목
    title = models.CharField("제목", max_length=300)
    # 작성자
    writer = models.CharField("작성자", max_length=100)
    # 북마크
    bookmark = models.ManyToManyField(User, related_name='bookmark_sentence')

    def __str__(self):
        return f'({self.id}) {self.title}'
