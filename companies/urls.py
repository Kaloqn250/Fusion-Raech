from django.urls import path

from companies.views import CompaniesListView, CreateCompanyView

urlpatterns = [
    path('list/', CompaniesListView.as_view(), name='companies_list'),
    path('create/', CreateCompanyView.as_view(), name='create_company')
]