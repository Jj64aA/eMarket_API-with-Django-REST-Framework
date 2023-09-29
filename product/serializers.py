
from rest_framework import serializers

from .models import Product,Review


class ReviewtSerializer(serializers.ModelSerializer):
   class Meta : 
      model = Review
      fields = "__all__"   
      
class ProductSerializer(serializers.ModelSerializer):

   # reviews = serializers.SerializerMethodField(method_name='get_reviews', read_only=True)
   
   reviews = ReviewtSerializer(many=True, read_only=True)

   class Meta : 
      model = Product
      fields = "__all__"
   
   # def get_reviwes(self, obj):
   #    reviwes =  obj.reviwes.all()
   #    serializer = ReviewtSerializer(reviwes,many=True)
   #    return serializer.data

   