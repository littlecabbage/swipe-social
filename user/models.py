import datetime

from django.db import models


class User(models.Model):
    """文档： 用户数据模型"""

    SEX = (
        ('男', '男'),
        ('女', '女'),
    )

    nickname = models.CharField(max_length=32, unique=True)
    phonenum = models.CharField(max_length=32, unique=True)

    sex = models.CharField(max_length=8, choices=SEX)

    avatar = models.CharField(max_length=256)
    location = models.CharField(max_length=32)
    birth_year = models.IntegerField()
    birth_month = models.IntegerField()
    birth_day = models.IntegerField()

    @property
    def age(self):
        today = datetime.date.today()
        birth_date = datetime.date(self.birth_year, self.birth_month, self.birth_day)
        times = today - birth_date
        return times // 365


class Profile(models.Model):
    """用户配置项"""
    SEX = (
        ('男', '男'),
        ('女', '女'),
    )

    location = models.CharField(max_length=128, verbose_name="目标城市")

    min_distance = models.IntegerField(verbose_name="最小查找范围")
    max_distance = models.IntegerField(verbose_name="最大查找范围")

    min_dating_age = models.IntegerField(verbose_name="最小交友年龄")
    max_dating_age = models.IntegerField(verbose_name="最大交友年龄")

    dating_sex = models.CharField(max_length=8, verbose_name="匹配的性别", choices=SEX)
    vibration = models.BooleanField(verbose_name="开启震动")
    only_match = models.BooleanField(verbose_name="不让为匹配的人看我的相册")
    auto_play = models.BooleanField(verbose_name="自动播放视频")



