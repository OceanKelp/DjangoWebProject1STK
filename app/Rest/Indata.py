from django.http import JsonResponse

def upload_handler(request):
    if request.method == 'POST':
        # Process the uploaded data here
        # You can access form data using request.POST or request.FILES
        # Perform your processing, and then create a response
        response_data = {'message': 'File uploaded successfully'}
        return JsonResponse(response_data)
    else:
        # Handle other HTTP methods (e.g., GET) if needed
        return JsonResponse({'message': 'Unsupported method'}, status=405)

