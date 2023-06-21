from django.forms import ModelForm
from .models import book,Author


class Bookcreate(ModelForm):
    class Meta:
        model = book
        fields = '__all__'


class Authoradd(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
    


