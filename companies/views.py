
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from companies.forms import CompanyForm
from companies.models import Company


# Create your views here.
class CompaniesListView(ListView):
    model = Company
    context_object_name = 'companies'
    template_name = 'companies/companies_list.html'

    def get_queryset(self):
        return Company.objects.all()


class CreateCompanyView(CreateView):
    model = Company
    template_name = 'companies/create_company.html'
    form_class = CompanyForm
    success_url = reverse_lazy('companies_list')