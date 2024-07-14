from django.contrib import admin
from .models import Patient, Session, BodyComposition, ClientSession
from .forms import PatientForm, SessionForm
from django.urls import reverse
from django.utils.html import format_html



class PatientAdmin(admin.ModelAdmin):
    form = PatientForm
    list_display = (
        'name', 'phone_number', 'email', 'age', 'sex', 'weight', 'height', 'blood_group', 'purpose'
    )
    search_fields = ('name__icontains', 'phone_number__icontains', 'email__icontains', 'purpose__icontains')

    fieldsets = [
        ('Personal Information', {
            'fields': ['name', 'phone_number', 'email', 'occupation', 'address', 'age', 'sex', 'marital_status']
        }),
        ('Physical Information', {
            'fields': ['weight', 'height', 'blood_group']
        }),
        ('Medical Information', {
            'fields': (('purpose', 'medical_issue'), ('medicine', 'supplement')),
            'classes': ('wide', 'extrapretty'),
        }),
        ('Daily Routine', {
            'fields': (('wake_up_time', 'sleep_time', 'noon_nap'),),
            'classes': ('wide', 'extrapretty'),
        }),
        ('Family History', {
            'fields': ['family_history']
        }),
        ('Food Preferences', {
            'fields': (('veg', 'non_veg', 'jain', 'egg', 'chicken', 'sea_food'),
                       ('sweet', 'spicy', 'sour', 'salty', 'blend', 'pungeant'),
                       ('food_allergy', 'beverage', 'dessert', 'fruits'),
                       ('water_intake', 'outside_food'),
                       ('alcohol', 'smoke')),
            'classes': ('wide', 'extrapretty'),
        }),
        ('Exercise', {
            'fields': (('excercise',),
                       ('time_excercise', 'what_excercise', 'day_excercise'),),
            'classes': ('wide', 'extrapretty'),
        }),
        ('Hair and Skin', {
            'fields': (('hair_problem', 'hair_qaulity'),
                       ('skin_quality',)),
            'classes': ('wide', 'extrapretty'),
        }),
        ('Health Issues', {
            'fields': (('diabetes', 'thyroid', 'pcos', 'hypertension', 'heart_disease', 'cholesterol'),
                       ('constipation', 'diarrhea', 'acidity', 'head_ache', 'body_pain')),
            'classes': ('wide', 'extrapretty'),
        }),
        ('Periods', {
            'fields': (('irregular_period',),
                       ('how_irrugular',)),
            'classes': ('wide', 'extrapretty'),
        }),
        ('Children Information', {
            'fields': (('kids', 'how_dilevery'),),
            'classes': ('wide', 'extrapretty'),
        }),
        ('Other Information', {
            'fields': (('consume_oil', 'consume_ghee'),
                       ('consume_salt', 'consume_sugar'),
                       ('consume_milk', 'consume_rice'),
                       ('consume_flour',)),
            'classes': ('wide', 'extrapretty'),
        })
    ]

admin.site.register(Patient, PatientAdmin)


class SessionInline(admin.TabularInline):
    model = Session
    form = SessionForm
    extra = 0
    readonly_fields = ('generate_pdf',)

    def generate_pdf(self, obj):
        if obj.id:
            return format_html(
                '<a class="button" href="{}">PDF</a>',
                reverse('generate_pdf', args=[obj.id])
            )
        return ''
    generate_pdf.short_description = 'GENERATE PDF'
    generate_pdf.allow_tags = True









class ClientSessionAdmin(admin.ModelAdmin):
    inlines = [SessionInline]
    list_display = ('patient',)
    search_fields = ('patient__name__icontains',)  # Enable dynamic searching

    
admin.site.register(ClientSession, ClientSessionAdmin)

admin.site.register(Session)
admin.site.register(BodyComposition)


    








admin.site.site_header = "Healvibe Admin"
admin.site.site_title = "Healvibe Admin Portal"
admin.site.index_title = "Welcome to Healvibe Admin Portal"
