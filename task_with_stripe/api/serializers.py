from rest_framework import serializers

from payments.models import Item


class ItemSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Item
        fields = ('name', 'description', 'price',)
        lookup_field = 'pk'

    def get_price(self, obj):
        price_cent = obj.price
        price = price_cent / 100
        return price
