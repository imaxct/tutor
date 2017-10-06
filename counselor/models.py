from django.db import models


# Create your models here.


class User(models.Model):
    """
    用户
    """
    username = models.CharField(max_length=20)
    # TODO add fields
    pass


class Record(models.Model):
    """
    记录
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='record user')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='record question')
    option = models.ForeignKey(Option, on_delete=models.CASCADE, verbose_name='record option')

    class Meta:
        indexes = [
            models.Index(fields=[])
        ]

    def __str__(self):
        return '%s %s %s' % (self.user.username, self.question.question_text, self.option.option_num)


class Question(models.Model):
    """
    问题
    """
    pub_date = models.DateField
    question_text = models.TextField

    def __str__(self):
        return self.question_text


class Option(models.Model):
    """
    选项
    """
    score = models.FloatField
    option_text = models.CharField(max_length=200)
    option_num = models.CharField(max_length=1)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='question id')

    def __str__(self):
        return self.option_text
