from django.db import models
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.

class Customer(models.Model):
    name = models.CharField(verbose_name="客户姓名", max_length=200, null=True)
    telephone = models.CharField(verbose_name="电话", max_length=200, null=True)
    address = models.CharField(verbose_name="收货地址", max_length=200, null=True)

    def __str__(self):
        return f'{self.name}--{self.telephone}'


class Order(models.Model):
    NEW_TWOHAND = (('NEW','首次维修'), ('TH','二修'))

    date = models.DateTimeField(verbose_name="收卡时间", auto_now=True)
    brand = models.CharField(verbose_name="品牌", max_length=100, null=True)
    name = models.CharField(verbose_name="型号", max_length=100, null=True)
    sn_num = models.CharField(verbose_name="SN码", max_length=200, null=True)
    new = models.CharField(verbose_name="首修or二修", max_length=20, choices=NEW_TWOHAND, default='NEW')
    before_pic = ProcessedImageField(verbose_name="维修前图片", blank=True, null=True,
                                    upload_to='order/',
                                    format='JPEG',
                                    options={'quality': 20}
                                    )
    repaired_pic = ProcessedImageField(verbose_name="维修后图片", blank=True, null=True,
                                    upload_to='order/',
                                    format='JPEG',
                                    options={'quality': 20}
                                    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date}--{self.name}'