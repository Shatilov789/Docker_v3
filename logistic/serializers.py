from rest_framework import serializers
from rest_framework.utils import model_meta

from logistic.models import StockProduct, Product, Stock


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['title', 'description']


class ProductPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = StockProduct
        fields = ['product', 'quantity', 'price']


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = Stock
        fields = ['address', 'positions']

    def create(self, validated_data):
        positions = validated_data.pop('positions')
        stock = super().create(validated_data)
        for p in positions:
            StockProduct.objects.create(stock=stock, **p)

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop('positions')
        stock = super().update(instance, validated_data)
        positions_instance = instance.positions.all()

        for r in positions_instance:
            for w in positions:
                if r.product == w['product']:

                    if 'price' in w:
                        r.price = w['price']
                    if 'quantity' in w:
                        r.quantity = w['quantity']
        if r.product.id != w['product'].id:
           StockProduct.objects.create(product=w['product'], price=w['price'],quantity=w['quantity'],stock_id=r.stock_id)

        r.save()
        return stock
