from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, FarmerProfile, CustomerProfile

class FarmerRegistrationForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=False)
    state = forms.CharField(max_length=100, required=False)
    district = forms.CharField(max_length=100, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'farmer'
        if commit:
            user.save()
            FarmerProfile.objects.create(
                user=user,
                phone=self.cleaned_data.get('phone'),
                state=self.cleaned_data.get('state'),
                district=self.cleaned_data.get('district')
            )
        return user


class CustomerRegistrationForm(UserCreationForm):
    phone = forms.CharField(max_length=15, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'customer'
        if commit:
            user.save()
            CustomerProfile.objects.create(
                user=user,
                phone=self.cleaned_data.get('phone')
            )
        return user


from .models import Product, Listing, Inventory, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['commodity', 'variety', 'grade', 'description', 'location', 'harvest_date']



class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['selling_price_per_kg']

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['total_quantity']

from .models import TAMSurvey
class TAMSurveyForm(forms.ModelForm):
    class Meta:
        model = TAMSurvey
        fields = ['perceived_usefulness', 'perceived_ease_of_use', 'comments']
        widgets = {
            'perceived_usefulness': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'perceived_ease_of_use': forms.NumberInput(attrs={'min': 1, 'max': 5}),
        }
