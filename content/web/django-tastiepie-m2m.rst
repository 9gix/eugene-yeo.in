##################################
Django Tastypie ManyToMany Through
##################################

:date: 2012-12-04 02:00:00
:tags: django, python

.. code-block:: python

    # models.py
    from django.db import models

    class Ingredient(models.Model):
        name = models.CharField(max_length=100)
        description = models.TextField()

    class RecipeIngredients(models.Model):
        recipe = models.ForeignKey('Recipe')
        ingredient = models.ForeignKey('Ingredient')
        weight = models.IntegerField(null = True, blank = True)

    class Recipe(models.Model):
        title = models.CharField(max_length=100)
        ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredients', null = True, blank = True)


.. code-block:: python

    # api.py
    from tastypie.resources import Resource, ModelResource
    from tastypie import fields
    from junk.models import RecipeIngredients, Ingredient, Recipe

    class IngredientResource(ModelResource):
        class Meta:
            queryset = Ingredient.objects.all()
            resource_name = "ingredients"

    class RecipeIngredientResource(ModelResource):
        ingredient = fields.ToOneField(IngredientResource, 'ingredient',full=True)
        class Meta:
            queryset= RecipeIngredients.objects.all()

    class RecipeResource(ModelResource):
        ingredients = fields.ToManyField(RecipeIngredientResource,
                attribute=lambda bundle: bundle.obj.ingredients.through.objects.filter(
                    recipe=bundle.obj) or bundle.obj.ingredients, full=True)
        class Meta:
            queryset = Recipe.objects.all()
            resource_name = 'recipe'

With the following query ``GET /api/v1/recipe/2/?format=json`` It will return Ingredients Detail and Weight

.. code-block:: json

    {
      "id": "2", 
      "ingredients": [
        {
          "id": "1", 
          "ingredient": {"description": "", "id": "2", "name": "", "resource_uri": "/api/v1/ingredients/2/"}, 
          "recipe": "/api/v1/recipe/2/", 
          "resource_uri": "/api/v1/recipeingredient/1/", 
          "weight": null}, 
        {
          "id": "2", "ingredient": {"description": "", "id": "3", "name": "", "resource_uri": "/api/v1/ingredients/3/"}, 
          "recipe": "/api/v1/recipe/2/", 
          "resource_uri": "/api/v1/recipeingredient/2/", 
          "weight": null}], 
      "resource_uri": "/api/v1/recipe/2/", 
      "title": ""
    }

