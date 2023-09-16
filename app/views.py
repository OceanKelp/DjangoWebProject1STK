"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from .Pfolder.tablecontrol import tabletitle
from django.http import JsonResponse
# from Stk import stkviews.Stkcontact

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            # 'title':'About',
            'title': gett(),
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

# my code
# table of information
def table(request):
    """Renders the table page."""
    assert isinstance(request, HttpRequest)
    #tablecontrol()
    return render(
        request,
        'app/table.html',
        {
            'title':tabletitle(),
            'message':'Your table page.',
            'year':datetime.now().year,
        }
    )

def gett():
    abc = "I returened title"
    return(abc)



# from django.http import JsonResponse

def upload_file(request):
    if request.method == 'POST' and 'file' in request.FILES:
        uploaded_file = request.FILES['file']
        print('loadded file')
        # Process the uploaded file here (e.g., save it to disk or perform further actions)
        response_data = {'message': 'File uploaded successfully'}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'message': 'Invalid request'}, status=400)