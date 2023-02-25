"""
Views for the recipe APIs
"""
# from drf_spectacular.utils import (
#     extend_schema_view,
#     extend_schema,
#     OpenApiParameter,
#     OpenApiTypes,
# )

from rest_framework import (
    viewsets,
    # mixins,
    # status,
)
# from rest_framework.decorators import action
# from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import (
    Recipe,
    # Tag,
    # Ingredient,
)
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        # tags = self.request.query_params.get('tags')
        # ingredients = self.request.query_params.get('ingredients')
        # queryset = self.queryset
        # if tags:
        #     tag_ids = self._params_to_ints(tags)
        #     queryset = queryset.filter(tags__id__in=tag_ids)
        # if ingredients:
        #     ingredient_ids = self._params_to_ints(ingredients)
        #     queryset = queryset.filter(ingredients__id__in=ingredient_ids)

        return self.queryset.filter(user=self.request.user).order_by('-id')

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return serializers.RecipeSerializer

        return self.serializer_class

    def perform_create(self, serializer):
        """Create a new recipe."""
        serializer.save(user=self.request.user)