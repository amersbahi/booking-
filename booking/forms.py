from django import forms
from django.core.validators import RegexValidator, MinValueValidator
from .models import patient
from django.utils import timezone


class AppointmentsForm(forms.Form):
    full_name = forms.CharField(label='الأسم الكامل', max_length=100, required= True)
    phone_number = phone_number = forms.CharField(
        label='رقم الهاتف', 
        max_length=15, 
        validators=[RegexValidator(regex=r'^\d{9,15}$', message='الرجاء إدخال رقم صالح')], required=True
    )
    message = forms.CharField(label='نوع الالم', widget=forms.Textarea, required=False)
    datetime_field = forms.DateTimeField( label='التاريخ و الوقت',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        input_formats=['%Y-%m-%dT%H:%M'],  # Corrected format string
        validators=[MinValueValidator(limit_value=timezone.now(), message="الرجاء التأكد من التاريخ والوقت")])
    