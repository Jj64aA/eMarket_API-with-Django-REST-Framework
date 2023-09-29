import django_filters

from .models import Product 


class ProductsFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    keyword = django_filters.filters.CharFilter(field_name="name",lookup_expr="icontains")
    minPrice = django_filters.filters.NumberFilter(field_name="price" or 0,lookup_expr="gte")
    maxPrice = django_filters.filters.NumberFilter(field_name="price" or 100000,lookup_expr="lte")

    class Meta:
        model = Product
        fields = ('category', 'brand','keyword',"minPrice","maxPrice")

class myfilter(django_filters.FilterSet):
    keyword = django_filters.filters.CharFilter(field_name="name",lookup_expr="icontains")
    class Meta:
        model = Product 
        fields = ['keyword']     

        