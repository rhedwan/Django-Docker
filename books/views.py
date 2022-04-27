from http import server
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from .serializers import BookSerializer
from .models import Book

@api_view(["GET", "POST", "PUT", "DELETE"])
def book_view(request):
    if request.method == "GET":
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    if request.method == "POST":
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

@api_view(["GET", "PUT", "DELETE"])
def book_detail(request, pk):
    if request.method == "GET":
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({
                "book" : "Book Not Found"
            }, status=status.HTTP_404_NOT_FOUND) 
        serializer = BookSerializer(book)
        return Response(serializer.data)

    if request.method == "PUT":
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    if request.method == "DELETE":
        book = Book.objects.get(pk=pk)
        book.delete()
        return Response({
            "book" : "Book Deleted succesfully"
        })
