from django.db import models

class ConsumerBehavior(models.Model):
    gender = models.CharField(max_length=10)
    age = models.CharField(max_length=20)
    ethnic = models.CharField(max_length=20)
    occupation = models.CharField(max_length=20)
    income = models.CharField(max_length=30)
    use_social_media = models.CharField(max_length=5)
    experience_purchasing = models.CharField(max_length=5)
    reviews_affect = models.CharField(max_length=5)
    internet_hours = models.CharField(max_length=20)
    attention_ads = models.CharField(max_length=5)
    PB1 = models.IntegerField()
    PB2 = models.IntegerField()
    PB3 = models.IntegerField()
    PB4 = models.IntegerField()
    ATTD1 = models.IntegerField()
    ATTD2 = models.IntegerField()
    ATTD3 = models.IntegerField()
    ATTD4 = models.IntegerField()
    SN1 = models.IntegerField()
    SN2 = models.IntegerField()
    SN3 = models.IntegerField()
    SN4 = models.IntegerField()
    PBC1 = models.IntegerField()
    PBC2 = models.IntegerField()
    PBC3 = models.IntegerField()
    PBC4 = models.IntegerField()
    
    class Meta:
         db_table = 'dashboard_consumerbehavior'
         verbose_name_plural = 'Consumer Behavior'

    def __str__(self):
        return f'{self.gender}, {self.age}, {self.ethnic}'
    
    
    # def __str__(self):
    #     return f'{self.text}'

