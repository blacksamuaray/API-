from rest_framework.decorators import api_view
from django.shortcuts import render
from .models import Books
from rest_framework import generics
from .serializers import BooksSerializers
from rest_framework.response import Response

class BookListApiView(generics.ListAPIView):
    queryset=Books.objects.all()
    serializer_class =BooksSerializers


class BookDetailApiview(generics.RetrieveAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers

class BookDeleteApiView(generics.DestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers


class BooksUpdateApiview(generics.UpdateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers


class BookCreateApiView(generics.CreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializers


@api_view(['GET'])
def book_list_view(request,*args,**kwargs):
    books=Books.objects.all()
    serializer=BooksSerializers(books, many=True)
    return Response(serializer.data)