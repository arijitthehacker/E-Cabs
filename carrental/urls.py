from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import logout

from frontend.views import CarDetailsView
from frontend.views import NewBookingView
from frontend.views import HomeView

from django.conf.urls import include
from django.views.generic import TemplateView
from frontend.views import UserRegistrationView
from django.contrib.auth.views import login




urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^car/(?P<pk>\d+)/$', CarDetailsView.as_view(), name='car-details'),

    url(r'^booking/(?P<car_pk>\d+)/$', NewBookingView.as_view(), name='new-booking'),
    url(r'^signup/$', UserRegistrationView.as_view(), name='user_registration'),
	url(r'^login/$', login, {'template_name': 'login.html'},name='login'),
	url(r'^logout/$', logout, {'next_page': '/login/'}, name='logout'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
