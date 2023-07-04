import os

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .services import generate_questions, print_all_questions


def home(request):
    if request.method == 'POST':
        text = request.POST['text']
        questions = generate_questions(text)
        context = {'questions': questions}
        return render(request, 'base.html', context)
    return render(request, 'base.html')

def history(request):
    return render(request, 'donwload.html')

data = print_all_questions()

class TestListView(TemplateView):
    template_name = 'download.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = data
        return context

def download(request, test_id):
    test = next((t for t in data if t[0] == test_id), None)
    if test:
        header = test[1]
        questions = test[2]
        filename = f'test_{test_id}.txt'
        with open(filename, 'w') as f:
            f.write(questions)
        file_path = os.path.join(os.getcwd(), filename)
        response = HttpResponse(open(file_path, 'rb'), content_type='text/plain')
        response['Content-Disposition'] = f'attachment; filename="{header}.txt"'
        return response
    else:
        return HttpResponse("Test not found.")
