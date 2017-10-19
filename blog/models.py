from django.db import models
import mongoengine
from myblog.settings import DBNAME
# Create your models here.
mongoengine.connect(DBNAME)
class Student(mongoengine.Document):
    name = mongoengine.StringField(max_length=16)
    age = mongoengine.IntField(default=1)
    def __unicode__(self):
        return self.name
