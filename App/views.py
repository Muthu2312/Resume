from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .forms import ContactForm

# # Create your views here.
# class Login(View):
#     def get(self,request):
#         return render(request,"Login.html")

from django.views.generic.edit import FormView


class ContactView(FormView):
    template_name = 'Login.html'
    form_class = ContactForm
    success_url = '/'  # URL to redirect to on successful form submission

    def form_valid(self, form):
        form.save()
        # Handle form submission (e.g., send an email, save to database)
        return super().form_valid(form)