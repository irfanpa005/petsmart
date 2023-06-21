from django.contrib import admin
from . models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}

    # def get_categories(self, obj):
    #     product = Product.objects.get(pk=)
    #     print("\n".join([p.category_name for p in obj.category.all()]))
    #     return "\n".join([p.category_name for p in obj.category.all()])


admin.site.register(Product,ProductAdmin)
