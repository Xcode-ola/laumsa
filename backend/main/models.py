from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class contact_details(models.Model):
    name = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    telephone2 = models.CharField(max_length=20)
    whatsapp = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    telegram = models.URLField(blank=True, null=True)
    discord = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)

    class Meta:
        verbose_name = 'Contact Details'
        verbose_name_plural = 'Contact Details'

    def __str__(self):
        return self.name

class CourseList(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.name

class Quiz(models.Model):
    course = models.ForeignKey(CourseList, related_name="quiz", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    def __str__(self):
        return self.name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, related_name="question", on_delete=models.CASCADE)
    question = models.TextField()

    class Meta:
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return self.quiz.title

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.CASCADE)
    choice = models.CharField(max_length=20)
    correct = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Answer'
        verbose_name_plural = 'Answers'

    def __str__(self):
        return self.choice

class ChapterList(models.Model):
    course = models.ForeignKey(CourseList, related_name="chapter", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Chapter'
        verbose_name_plural = 'Chapters'

    def __str__(self):
        return self.name

class CourseSummary(models.Model):
    course = models.ForeignKey(CourseList, related_name="summary", default=1, on_delete=models.CASCADE)
    chapter = models.ForeignKey(ChapterList, related_name="summary", on_delete=models.CASCADE)
    body = RichTextField()
    isverified = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Summary'
        verbose_name_plural = 'Summaries'

    def __str__(self):
        return self.chapter.name

class PracticeQuestion(models.Model):
    course = models.ForeignKey(CourseList, related_name="practice", default=1, on_delete=models.CASCADE)
    chapter = models.ForeignKey(ChapterList, related_name="practice", on_delete=models.CASCADE)
    question = models.TextField()
    answer = RichTextField()
    isverified = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Practice Question'
        verbose_name_plural = 'Practice Questions'

    def __str__(self):
        return self.chapter.name