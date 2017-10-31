from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=16)
    age =  models.IntegerField(default=1)
    def __unicode__(self):
        return self.name
class Article(models.Model):
    title = models.CharField('标题',max_length=70)
    body = models.TextField('正文')
    build_t = models.DateTimeField('创建时间',auto_now=True)  #自动添加
    last_modified_t = models.DateTimeField('修改时间',auto_now=True)
    views = models.PositiveIntegerField('浏览量',default=0)
    likes = models.PositiveIntegerField('点赞数',default=0)

    topped = models.BooleanField('置顶',default=False)
    category = models.ForeignKey('Category',verbose_name='分类',null=True,
                                 on_delete=models.SET_NULL)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-last_modified_t']
class Category(models.Model):
    name = models.CharField('类名',max_length=20)
    created_t = models.DateTimeField('创建时间',auto_now= True)
    last_modified_time = models.DateTimeField('修改时间',auto_now=True)

    def __str__(self):
        return self.name
class User(models.Model):
    name = models.CharField('昵称',max_length=20)
    def __str__(self):
        return  self.name