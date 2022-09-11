from django.views.generic import ListView
from .models import Item

# Create your views here.
class HomePageView(ListView):
    model = Item
    template_name = 'base/index.html'
    queryset = Item.objects.all().filter(label='on-sale')[:5]
    context_object_name = 'item_list'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['featured_products'] = Item.objects.all().order_by('-count_sold')[:6]
        return context
