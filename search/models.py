from django.db import models


class HumanManageer(models.Manager):
    def create_human(self, xh, name, phoneNumber, college, gender):
        human = self.create(xh=xh, name=name,
                            phoneNumber=phoneNumber,
                            college=college, gender=gender)
        return human


class Human(models.Model):
    _database = 'hlju'
    GENDER_CHOICE = (
        ('male', '男'),
        ('female', '女')
    )
    xh = models.IntegerField(verbose_name="学号", unique_for_date=True)
    name = models.CharField(verbose_name="姓名", max_length=70)
    phoneNumber = models.CharField(verbose_name="电话", max_length=200)
    college = models.CharField(verbose_name="学院",
                               max_length=200,
                               blank=True)
    gender = models.CharField(choices=GENDER_CHOICE,
                              max_length=20,
                              verbose_name='性别',
                              blank=True)
    object = models.Manager()
    create = HumanManageer()


    class Meta:
        verbose_name = "联系人"

    def __str__(self):
        return self.name