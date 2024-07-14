from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import Patient, ClientSession
from .utils import create_google_sheet, delete_google_sheet



@receiver(post_save, sender=Patient)
def create_client_session(sender, instance, created, **kwargs):
    """
    Signal to create ClientSession and diet sheet when a Patient is created
    """
    if created:
        client_session, created = ClientSession.objects.get_or_create(patient=instance)
        
        # Only create the sheet if the ClientSession is newly created
        if created:
            patient_sheet_url = create_google_sheet(instance.name)
            client_session.patient_url = patient_sheet_url
            client_session.save()

@receiver(post_delete, sender=Patient)
def delete_google_sheet_patient(sender, instance, **kwargs):
    """
    Signal to delete the Google Sheet associated with a Patient when the Patient is deleted.
    """
    patient_name = instance.name
    delete_google_sheet(patient_name)
