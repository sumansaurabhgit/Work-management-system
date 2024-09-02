from django import forms
from .models import Work, Worker

from django.forms.widgets import Select


class WorkForm(forms.ModelForm):
    class Meta:
        model = Work
        fields = ['name', 'numberOfWorker',
                  'startDate', 'duration', 'priority', 'role', 'status']
        widgets = {
            'startDate': forms.DateInput(attrs={'type': 'date'}),
            'numberOfWorker': forms.NumberInput(attrs={'min': 1, 'value': 1}),
            'priority': forms.NumberInput(attrs={'min': 1, 'class': 'ui dropdown'}),
            'duration': forms.NumberInput(attrs={'min': 1}),
            'status': Select(choices=Work.STATUS_CHOICES, attrs={'value': 'pending'}),
        }
        labels = {
            'name': 'Work Title',
            'numberOfWorker': 'Number of Workers',
            'startDate': 'Start Date',
            'duration': 'Duration(in days)',
            'priority': 'Priority Level',
            'role': 'Role',
            'status': 'Status',
        }


class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'role', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'ui input'}),
            'role': forms.TextInput(attrs={'class': 'ui input'}),
            'rating': forms.NumberInput(attrs={'class': 'ui input', 'min': 1, 'max': 5, 'step': 0.1}),
            # 'available': forms.RadioSelect(choices=Worker.AVAILABILITY_CHOICES),
        }
        labels = {
            'name': 'Worker Name',
            'role': 'Role',
            'rating': 'Rating',
            # 'available': 'Availability',
        }



from django import forms
from .models import Worker

class AssignWorkForm(forms.Form):
    work = forms.ModelChoiceField(queryset=Work.objects.filter(status='pending'), empty_label=None, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['workers'] = forms.ModelMultipleChoiceField(queryset=Worker.objects.filter(user=user, available=True))

class CompleteWorkForm(forms.Form):
    work = forms.ModelChoiceField(queryset=Work.objects.all(), empty_label=None, widget=forms.HiddenInput())

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
# forms.py






