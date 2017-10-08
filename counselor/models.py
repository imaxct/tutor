from django.db import models


# Create your models here.


class Academy(models.Model):
    """
    学院
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class User(models.Model):
    """
    学生
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    stu_no = models.CharField(max_length=20)
    id_no = models.CharField(max_length=20)
    grade = models.CharField(max_length=10)
    academy = models.ForeignKey(Academy, verbose_name='user academy')

    def __str__(self):
        return '%s %s %s' % (self.stu_no, self.name, self.academy.name)


class Teacher(models.Model):
    """
    教师
    """
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    academy = models.ForeignKey(Academy, verbose_name='teacher academy')

    def __str__(self):
        return self.name


class Question(models.Model):
    """
    问题
    """
    id = models.IntegerField(primary_key=True)
    pub_date = models.DateField(auto_now=True, editable=True)
    question_text = models.TextField(max_length=300, null=True)

    def __str__(self):
        return self.question_text


class Option(models.Model):
    """
    选项
    """
    id = models.IntegerField(primary_key=True)
    option_num = models.CharField(max_length=1)
    option_text = models.CharField(max_length=200)
    score = models.FloatField(default=0.0)

    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='question id')

    def __str__(self):
        return self.option_text


class Record(models.Model):
    """
    记录
    """
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='record user')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='record question')
    option = models.ForeignKey(Option, on_delete=models.CASCADE, verbose_name='record option')

    class Meta:
        unique_together = ('user', 'question', 'option')

    def __str__(self):
        return '%s %s %s' % (self.user.name, self.question.question_text, self.option.option_num)
