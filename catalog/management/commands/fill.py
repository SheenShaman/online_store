import json

from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()
        with open('data.json', 'r', encoding='utf-8') as file:
            data = file.read()
            data_json = json.loads(data)
            category = []
            product = []
            for item in data_json:
                if item['model'] == "catalog.category":
                    category.append(Category(pk=item['pk'], **item['fields']))
            Category.objects.bulk_create(category)

            for item in data_json:
                if item['model'] == "catalog.product":
                    name = item['fields']['name']
                    description = item['fields']['description']
                    image = item['fields']['image']
                    category = item['fields']['category']
                    num_category = Category.objects.get(pk=category)
                    price = item['fields']['price']
                    date_of_creation = item['fields']['date_of_creation']
                    date_of_change = item['fields']['date_of_change']
                    product.append(Product(pk=item['pk'],
                                           name=name,
                                           description=description,
                                           image=image,
                                           category=num_category,
                                           price=price,
                                           date_of_creation=date_of_creation,
                                           date_of_change=date_of_change
                                           ))
            Product.objects.bulk_create(product)

