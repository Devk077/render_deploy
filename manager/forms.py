from django import forms
from .models import Patient,Session

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name'}),
            'phone': forms.TextInput(attrs={'type': 'tel', 'placeholder': "Enter Phone Number"}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter email'}),
            'occupation': forms.TextInput(attrs={'placeholder': 'Enter Occupation'}),
            'address': forms.Textarea(attrs={'rows': 5, 'cols': 100, 'placeholder': 'Enter Address'}),
            'age': forms.TextInput(attrs={'type': 'number', 'placeholder': '18'}),
            'sex': forms.Select(choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'))),
            'marital_status': forms.Select(choices=(
                ('Single', 'Single'), ('Married', 'Married'), ('Divorced', 'Divorced'), ('Widowed', 'Widowed'))
            ),

            'height': forms.TextInput(attrs={'type': 'number', 'placeholder': 'Enter height in cm'}),
            'weight': forms.TextInput(attrs={'type': 'number', 'placeholder': 'Enter weight in kg'}),
            'blood_group': forms.Select(choices=(
                ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'),
                ('O-', 'O-'))
            ),
            'purpose': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter Purpose'}),
            'medical_issue': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter Medical Issue(if any?)'}),
            'medicine': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter Medicine(if any?)'}),
            'supplement': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Enter Supplement(if any?)'}),

            'wake_up_time': forms.TextInput(attrs={'placeholder': 'Enter wake up time'}),
            'sleep_time': forms.TextInput(attrs={'placeholder': 'Enter sleep time'}),
            'noon_nap': forms.TextInput(attrs={'placeholder': 'Enter noon nap'}),

            'family_history': forms.Textarea(
                attrs={'rows': 5, 'cols': 100, 'placeholder': 'Enter Family History(if any?)'}),

            'food_allergy': forms.Textarea(attrs={'placeholder': 'Enter Food Allergy(if any?)', 'rows': 5}),
            'beverage': forms.Textarea(attrs={'placeholder': 'Do you consume tea, coffee, milk? other?', 'rows': 5}),
            'dessert': forms.Textarea(attrs={'placeholder': 'Do you eat dessert or sweet daily? And what?', 'rows': 5}),
            'fruits': forms.Textarea(attrs={'placeholder': 'Do you consume fruits daily? And what?', 'rows': 5}),

            'water_intake': forms.Textarea(attrs={'placeholder': 'Enter Water Intake', 'rows': 5}),
            'outside_food': forms.Textarea(attrs={'placeholder': 'Do you eat outside food?', 'rows': 5}),
            'alcohol': forms.Textarea(attrs={'placeholder': 'Do you consume alcohol?', 'rows': 5}),
            'smoke': forms.Textarea(attrs={'placeholder': 'Do you smoke?', 'rows': 5}),

            'excercise': forms.Textarea(attrs={'placeholder': 'Do you do any exercise? If yes, what?', 'rows': 5}),
            'time_excercise': forms.Textarea(attrs={'placeholder': 'Enter time of exercise', 'rows': 5}),
            'what_excercise': forms.Textarea(attrs={'placeholder': 'Enter type of exercise', 'rows': 5}),
            'day_excercise': forms.Textarea(attrs={'placeholder': 'Number of days of exercised', 'rows': 5}),

            'hair_problem': forms.Textarea(attrs={'placeholder': 'Enter Hair Problem', 'rows': 5}),
            'hair_qaulity': forms.Textarea(attrs={'placeholder': 'Enter Hair Quality', 'rows': 5}),
            'skin_quality': forms.Textarea(attrs={'placeholder': 'Enter Skin Quality', 'rows': 5}),

            'how_irrugular': forms.Textarea(attrs={'placeholder': 'How irregular?', 'rows': 5}),

            'how_dilevery': forms.Textarea(attrs={'placeholder': 'How was the delivery?', 'rows': 5}),

            'consume_oil': forms.Textarea(attrs={'placeholder': 'Do you consume oil? If yes, which one?', 'rows': 5}),
            'consume_ghee': forms.Textarea(attrs={'placeholder': 'Do you consume ghee? If yes, which one?', 'rows': 5}),
            'consume_salt': forms.Textarea(attrs={'placeholder': 'Do you consume salt? If yes, which one?', 'rows': 5}),
            'consume_sugar': forms.Textarea(attrs={'placeholder': 'Do you consume sugar? If yes, which one?', 'rows': 5}),
            'consume_milk': forms.Textarea(attrs={'placeholder': 'Do you consume milk? If yes, which one?', 'rows': 5}),
            'consume_rice': forms.Textarea(attrs={'placeholder': 'Do you consume rice? If yes, which one?', 'rows': 5}),
            'consume_flour': forms.Textarea(attrs={'placeholder': 'Do you consume flour? If yes, which one?', 'rows': 5}),

        }

class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = '__all__'
        widgets = {
            # 'session_date': forms.DateTimeInput(attrs={'type': 'date'}),
            'session_notes': forms.Textarea(attrs={'rows' : 5, 'cols': 50, 'placeholder': 'Enter notes'}),
        }