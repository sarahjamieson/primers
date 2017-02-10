from django.shortcuts import render, get_object_or_404, redirect
from primerdb.forms import PrimerForm
from django.http import HttpResponse
from django.contrib import messages
from primerdb.models import Primer


def index(request):
    return render(request, "primerdb/home.html")


def add_primer_to_db(request):
    """

    :param request:
    :return:
    """
    add_successful = False
    if request.method == 'POST':
        form = PrimerForm(request.POST)
        if form.is_valid():
            form.save()
            add_successful = True
        else:
            messages.error(request, "Error")
    return render(request, "primerdb/add_form.html", {'form': PrimerForm(), 'success': add_successful})


def search_by_gene(request):
    primers = None
    genes = Primer.objects.values_list('gene', flat=True).order_by('gene').distinct()
    if 'gene' in request.GET:
        gene = request.GET['gene']
        primers = Primer.objects.filter(gene__icontains=gene)

    return render(request, 'primerdb/search.html', {'primers': primers, 'genes': genes})


def primer_update(request, pk):
    primer = get_object_or_404(Primer, pk=pk)
    form = PrimerForm(request.POST or None, instance=primer)
    if form.is_valid():
        form.save()
        return redirect('search')
    return render(request, "primerdb/update_form.html", {'form': form})

