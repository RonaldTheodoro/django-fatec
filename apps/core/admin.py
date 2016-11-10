from django.contrib import admin
from .models import Distributor
from .models import Category
from .models import Movie


admin.site.register(Distributor)
admin.site.register(Category)
admin.site.register(Movie)