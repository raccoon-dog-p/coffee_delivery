from django.db import models

# Create your models here.

class CoffeeBean(models.Model):
    origin = models.CharField(max_length=15, null=False, help_text='원두 원산지')
    bean_name = models.CharField(max_length=50, null=False, unique=True, help_text='원두 이름')
    region = models.CharField(max_length=50, null=True, help_text='지역 이름')
    grade = models.CharField(max_length=10, null=False, help_text='원두 등급')
    processiong_method = models.CharField(max_length=10, null=True, help_text='원두 가공 방법')
    stock = models.PositiveBigIntegerField(null=False, help_text='원두 재고')
    date_receipt = models.DateTimeField(null=False, help_text='입고 날짜')
    price = models.PositiveIntegerField(null=False, help_text='원두 가격')
    aroma = models.PositiveSmallIntegerField(null=False, help_text='향미')
    flavor = models.PositiveSmallIntegerField(null=False, help_text='맛')
    acidity = models.PositiveSmallIntegerField(null=False, help_text='산미')
    texture = models.PositiveSmallIntegerField(null=False, help_text='질감')
    aftertastes = models.PositiveSmallIntegerField(null=False, help_text='후미')
    uniformity = models.PositiveSmallIntegerField(null=False, help_text='일관성')
    balance = models.PositiveSmallIntegerField(null=False, help_text='균형감')
    cleancup = models.PositiveSmallIntegerField(null=False, help_text='깔끔함')
    sweetness = models.PositiveSmallIntegerField(null=False, help_text='단맛')
    total_score = models.PositiveSmallIntegerField(null=False, help_text='종합 점수')


    def __str__(self):
        return self.bean_name

    class Meta: 
        db_table = 'coffee_bean'

class Coffee(models.Model):
    origin = models.ForeignKey(CoffeeBean, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=False, unique=True)
    is_hot = models.BooleanField(null=False)
    price = models.PositiveIntegerField(null=False, help_text='커피 가격')
    size = models.CharField(max_length=2, default='M')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'coffee'