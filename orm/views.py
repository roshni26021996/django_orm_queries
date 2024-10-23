from django.shortcuts import render
from .models import Country, State, City
from django.db.models import Count

def all_orm_queries(request):  
    all_country_asc = Country.objects.all().order_by('sortname')[:5]
    all_country_desc = Country.objects.all().order_by('-phonecode')[:5]
    all_country_limit = Country.objects.all()[:5]
    all_country_distinct = Country.objects.distinct()[:5]
    all_country_between = Country.objects.filter(id__range=(1,50))[:5]
    all_country_select = Country.objects.values('name')[:5]
    all_country_count = State.objects.values('country_id').annotate(country_count=Count('country_id', distinct=True))
    
    context = {
        'all_country_asc': all_country_asc,
        'all_country_desc': all_country_desc,
        'all_country_limit': all_country_limit,
        'all_country_distinct': all_country_distinct,
        'all_country_between': all_country_between,
        'all_country_select': all_country_select,
        'all_country_count': all_country_count,
    }
    
    print(all_country_count.query)
    
    return render(request, 'orm_queries.html', context)

def insert_create_queries(request):
    
    # record_one = Country.objects.create(id="2222", name="Test 2", sortname="TU", phonecode="333") 
    record_one = Country.objects.create(name="Test 4", sortname="XT", phonecode="333") 
    print(record_one.query)
    return render(request)
    
    # return render(request,  'insert_create_queries.html')

def update_queries(request):
    
    record_one = Country.objects.create(name="Test 1", sortname="T", phonecode="303") 
    
    return render(request,  'insert_create_queries.html')

def delete_queries(request):
    
    record_one = Country.objects.create(name="Test 1", sortname="T", phonecode="303") 
    
    return render(request,  'insert_create_queries.html')


# Create your views here.
