from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def predict(request):
    return render(request, 'predict.html')

def no_hate_speech(request):
    return render(request, 'no_hate_speech.html')