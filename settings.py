INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles', # Required for GraphiQL
    'graphene_django'
]

GRAPHENE = {
    'SCHEMA': 'django_root.schema.schema'
}