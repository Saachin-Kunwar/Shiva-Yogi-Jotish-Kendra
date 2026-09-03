from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    SERVICE_CHOICES = [
        ('जन्म कुण्डली', 'जन्म कुण्डली विश्लेषण'),
        ('विवाह मिलान', 'विवाह मिलान'),
        ('ग्रह दशा/गोचर', 'ग्रह दशा / गोचर विश्लेषण'),
        ('करियर/शिक्षा', 'करियर तथा शिक्षा परामर्श'),
        ('वास्तु', 'वास्तु परामर्श'),
        ('शुभ मुहूर्त', 'शुभ मुहूर्त निर्धारण'),
    ]

    service = forms.ChoiceField(
        choices=SERVICE_CHOICES,
        widget=forms.Select(attrs={
            'class': 'w-full px-4 py-3 border rounded-xl border-amber-200 focus:outline-none focus:ring-2 focus:ring-amber-500 text-sm bg-white'
        })
    )

    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone', 'service', 'consultation_date', 'message']
        widgets = {
            'consultation_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 py-3 border rounded-xl border-amber-200 focus:outline-none focus:ring-2 focus:ring-amber-500 text-sm bg-white'
            }),
            'message': forms.Textarea(attrs={
                'rows': 3,
                'class': 'w-full px-4 py-3 border rounded-xl border-amber-200 focus:outline-none focus:ring-2 focus:ring-amber-500 text-sm bg-white',
                'placeholder': 'Any specific questions or details (Optional)...'
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Baki text fields ko lagi tailwind styling apply garne
        for field_name, field in self.fields.items():
            if field_name not in ['service', 'consultation_date', 'message']:
                field.widget.attrs.update({
                    'class': 'w-full px-4 py-3 border rounded-xl border-amber-200 focus:outline-none focus:ring-2 focus:ring-amber-500 text-sm bg-white',
                    'placeholder': f'Enter your {field.label.lower()}...'
                })