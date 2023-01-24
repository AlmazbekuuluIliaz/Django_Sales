from django.db import models
from simple_history.models import HistoricalRecords
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_int(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s Не может быть отрицательной'),
            params={'value': value})

def validate_price(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s Цена не может быть отрицательной'),
            params={'value': value})



class Storages(models.Model):
    phone = models.CharField(verbose_name='Телефон', max_length=25)
    address = models.CharField(verbose_name='Адрес', max_length=255)
    boss = models.CharField(verbose_name='Управляющий', max_length=255)
    number_storage = models.IntegerField(validators=[validate_int])
    
    history = HistoricalRecords()

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Место хранения'
        verbose_name_plural = 'Места хранения'
        

class Sales(models.Model):
    name = models.CharField(verbose_name='Название акции', max_length=25)
    company = models.CharField(verbose_name='Название компании', max_length=25)
    price = models.IntegerField(verbose_name='Прайс', validators=[validate_price])
    number_storage = models.ForeignKey(Storages, related_name='sales', on_delete=models.PROTECT, null=True)
    number = models.IntegerField(validators=[validate_int])
    photo = models.CharField(verbose_name='Фото акции',max_length=300)
    description = models.TextField(verbose_name='Описание акции')
    code_sale = models.IntegerField(validators=[validate_int])

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'


class Companies(models.Model):
    name = models.CharField(verbose_name='Название компании', max_length=255)
    address = models.CharField(verbose_name='Адрес компании', max_length=255)
    phone = models.CharField(verbose_name='Телефон компании', max_length=25)
    code_company = models.IntegerField(validators=[validate_int])

    history = HistoricalRecords()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['id']


class Contacts(models.Model):
    code_assistant = models.CharField(max_length=255)
    first_name = models.CharField(verbose_name='Имя представителя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия представителя', max_length=255)
    birthday = models.DateField(verbose_name='День рождения')
    address = models.CharField(verbose_name='Адрес представителя', max_length=255)
    phone = models.CharField(verbose_name='Телефон представителя', max_length=25)
    position = models.CharField(verbose_name='Должность', max_length=255)
    code_company = models.ForeignKey(Companies, related_name='сontacts', on_delete=models.PROTECT, null=True)

    history = HistoricalRecords()

    def __str__(self):
        return self.first_name 

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class User(models.Model):
    email = models.EmailField(max_length=255, verbose_name='Email адрес', unique=True)
    first_name = models.CharField(verbose_name='Имя', max_length=255)
    last_name = models.CharField(verbose_name='Фамилия', max_length=255)
    telephone = models.CharField(verbose_name='Номер телефона', max_length=255)
    is_active = models.BooleanField(verbose_name='Активирован', default=True)
    is_staff = models.BooleanField(verbose_name='Персонал', default=False)
    is_superuser = models.BooleanField(verbose_name='Администратор', default=False)
    favourite = models.ManyToManyField(Sales, verbose_name='Любимые акции')
    
    history = HistoricalRecords()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']


class Main(models.Model):
    sale = models.CharField(max_length=255)
    number = models.CharField(max_length=255)
    code_company = models.ForeignKey(Companies, verbose_name='Компания', related_name='main', on_delete=models.PROTECT, null=True)
    code_sale = models.ForeignKey(Sales, verbose_name='Акция', related_name='main', on_delete=models.PROTECT, null=True)
    sale_date = models.DateField()
    artist = models.IntegerField(validators=[validate_int])

    history = HistoricalRecords()

    def __str__(self):
        return self.sale

    class Meta:
        verbose_name = 'Главная'
        verbose_name_plural = 'Главная'
        ordering = ['id']

