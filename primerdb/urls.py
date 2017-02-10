from django.conf.urls import url
from django.contrib import admin
from primerdb.views import add_primer_to_db, index, primer_update, search_by_gene

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='home'),
    url(r'^add/$', add_primer_to_db, name='add'),
    url(r'^search/$', search_by_gene, name='search'),
    url(r'^edit/(?P<pk>\d+)/$', primer_update, name='edit'),
]
