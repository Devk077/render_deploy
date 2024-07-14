from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Session
from django.http import HttpResponse
from .utils import fetch_excel_data
import pdfkit
from django.conf import settings
from django.template.loader import get_template

def index(request):
    return render(request, "index.html")



def generate_pdf(request, session_id):
    session = get_object_or_404(Session, id=session_id)
    sheet_name = session.client_session.patient.name
    start = session.start_meal_line
    end = session.end_meal_line

    if not start or not end:
        messages.error(request, "Start and End meal lines must be SAVED to generate PDF")
        return redirect(request.META.get('HTTP_REFERER'))

    session_date = session.session_date
    if not session_date:
        messages.error(request, "Session date not found")
        return redirect(request.META.get('HTTP_REFERER'))

    body_composition = session.body_composition
    if not body_composition:
        messages.error(request, "Body composition data not found")
        return redirect(request.META.get('HTTP_REFERER'))

    # Fetch meal data from Excel or wherever you're storing it
    Food, Time, Quantity = [], [], []

    if start and end:
        Food, Time, Quantity = fetch_excel_data(sheet_name, start, end)

    meal_data = list(zip(Food, Time, Quantity))

    data = {
        'name': session.client_session.patient.name,
        'phone_number': session.client_session.patient.phone_number,
        'sleep_time': session.client_session.patient.sleep_time,
        'date': str(session_date),
        'height': str(body_composition.height),
        'weight': str(body_composition.weight),
        'body_fat': str(body_composition.body_fat),
        'age': str(body_composition.age),
        'BMI': str(body_composition.BMI),
        'RMR': str(body_composition.RMR),
        'visceral_fat': str(body_composition.visceral_fat),
        'meal_data': meal_data,
    }

    template = get_template("pdf.html")
    html = template.render(data)

    config = pdfkit.configuration(wkhtmltopdf=settings.WKHTMLTOPDF_PATH)

    try:
        # Generate PDF from HTML string
        pdf = pdfkit.from_string(html, False, configuration=config)

        # Set up HTTP response
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{sheet_name} diet plan.pdf"'
        return response

    except Exception as e:
        # Handle any exceptions here
        print(f"Error generating PDF: {e}")
        return HttpResponse("Error generating PDF", status=500)
