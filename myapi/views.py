from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .serializers import TestSerializer
from .models import Test
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    return HttpResponse("hi")

# @csrf_exempt
# def test_api(request):
#     if request.method == "GET":
#         test = Test.objects.all()
#         serializer = TestSerializer(test, many=True)
#         return JsonResponse(serializer.data, safe = False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = TestSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)



@api_view(['GET','POST'])
def test_api(request):

    if request.method == "GET":
        test = Test.objects.all()
        serializer = TestSerializer(test, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET','PUT','DELETE'])
def test_api_list(request, pk):

    try:
        test = Test.objects.get(pk=pk)
    except Test.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = TestSerializer(test)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TestSerializer(test, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        test.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
