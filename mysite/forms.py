from django.forms import ModelForm
from mysite.models import Comany

class ComapnyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'