from django.db import models


class ServiceRequest(models.Model):
    """Модель заявки на услугу"""
    car_model_name = models.CharField(max_length=255, verbose_name='Марка и модель авто')
    car_production_year = models.PositiveSmallIntegerField(verbose_name='Год выпуска авто')
    engine_volume = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Объем двигателя')
    phone = models.CharField(max_length=11, verbose_name='Номер телефона')
    dt_created = models.DateTimeField(auto_now_add=True)
    dt_updated = models.DateTimeField(auto_now=True)
    is_processed = models.BooleanField(verbose_name='Обработана ли заявка', default=False)

    def __str__(self):
        return self.phone + ' - ' + self.car_model_name
