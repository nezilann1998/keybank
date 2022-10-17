from random import choices
from django import forms
GENDER_CHOICES=(
    ("1", "Male"),
    ("2","Female"),
    ("3","others")
)
districtchoices=(
    ("1","Trivandrum"),
    ("2","Kottayam"),
    ("3","Kollam"),
    ("4","ernakulam")
)
branchchoices=(
    ("1","SBT"),
    ("2","Central Bank"),
    ("3","Southindian Bank")
)
accountchoices=(
    ("1","Saving"),
    ("2","Current"),
    ("3","Business")
)
materialchoices=(
    ("1","credit card"),
    ("2","debit card"),
    ("3","visa"),
    ("4","mastercard")
)
class BankForm(forms.Form):
    firstname=forms.CharField(label="Enter First Name" ,max_length=50)
    lastname=forms.CharField(label="Enter last Name" ,max_length=50)
    DOB=forms.DateField()
    Age=forms.DecimalField()
    Gender=forms.ChoiceField(choices=GENDER_CHOICES,widget=forms.RadioSelect)
    email=forms.EmailField()
    district=forms.ChoiceField(choices=districtchoices)
    branch=forms.ChoiceField(choices=branchchoices)
    accounttype=forms.ChoiceField(choices=accountchoices)
    materials=forms.ChoiceField(choices=materialchoices,widget=forms.CheckboxSelectMultiple,)

    
    def __str__(self):
        return self.firstname