from django.shortcuts import render
from .forms import SearchForm
from .models import SearchResult
from exa_py import Exa

#For searching the query
def search_results(request):
    query = []
    context = 10

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_term = form.cleaned_data['search_term']
            query = exa_search(search_term)

    else:
        form = SearchForm()

    return render(request, 'search/search_results.html', {'form': form, 'results': query, 'context': context})


#Output of the results
def exa_search(search_term):
    exa = Exa(api_key="<YOUR_API_KEY>")   #PUT YOUR EXA API KEY HERE
    
    # Assuming the correct parameter to pass the search term is 'query' (this depends on the Exa API)
    search_response = exa.search(use_autoprompt=True, num_results=10, query=search_term)

    results = [result.__dict__ for result in search_response.results] if search_response.results else []

    return results
