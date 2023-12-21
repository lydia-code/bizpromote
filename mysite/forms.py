from django.forms import ModelForm
from mysite.models import Brand

class brandForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'