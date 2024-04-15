from rest_framework import serializers
from .models import Books

class BooksSerializers(serializers.ModelSerializer):    #ModelSerializer bu admin dan qo'shgan malumotlarni json
                                                        #ko'rinishida saqlab beradi

    class Meta:                                          #rest_framework ishlatishdan maqsad barcha malumotlarni
                                                         # json ko'rinishda saqlash
        model=Books
        fields=('title','subtitle','author', 'isbn', 'price')