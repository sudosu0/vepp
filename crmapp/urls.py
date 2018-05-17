from django.urls import re_path
import crmapp.views as crmapp

app_name = 'crmapp'

urlpatterns = [
    re_path(r'^$', crmapp.main_crm, name='main_crm'),
    re_path(r'^workers/list/$', crmapp.workers_list_view, name='workers_list'),
    re_path(r'^worker/detail/(?P<worker_pk>\d+)/$', crmapp.worker_detail_view, name='worker_detail'),
    re_path(r'^worker/update/(?P<worker_pk>\d+)/$', crmapp.worker_update_view, name='worker_update'),

    re_path(r'^partners/$', crmapp.partners_view, name='partners'),
    re_path(r'^partner/create/$', crmapp.partner_create_view, name='partner_create'),
    re_path(r'^partner/read/(?P<partner_pk>\d+)/$', crmapp.partner_read_view, name='partner_read'),
    re_path(r'^partner/update/(?P<partner_pk>\d+)/$', crmapp.partner_update_view, name='partner_update'),

    re_path(r'^firms/$', crmapp.firms_view, name='firms'),
    re_path(r'^firm/create/$', crmapp.firm_create_view, name='firm_create'),
    re_path(r'^firm/read/(?P<firm_pk>\d+)/$', crmapp.firm_read_view, name='firm_read'),
    re_path(r'^firm/update/(?P<firm_pk>\d+)/$', crmapp.firm_update_view, name='firm_update'),

    re_path(r'^services/$', crmapp.services_view, name='services'),
    re_path(r'^service/create/$', crmapp.service_create_view, name='service_create'),
    re_path(r'^service/update/(?P<service_pk>\d+)/$', crmapp.service_update_view, name='service_update'),
]
