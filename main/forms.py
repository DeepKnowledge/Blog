from django import forms
from django.forms import ModelForm
from django.forms import Form
from django.contrib.auth.models import User
from django.utils.translation import ugettext, ugettext_lazy as _

class LoginForm(Form):
    name = forms.CharField(label="Name", max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class ExampleForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'first arg is the legend of the fieldset',
                'like_website',
                'favorite_number',
                'favorite_color',
                'favorite_food',
                'notes'
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button white')
            )
        )
        super(ExampleForm, self).__init__(*args, **kwargs)
