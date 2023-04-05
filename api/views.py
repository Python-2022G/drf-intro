from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def hi(request: Request) -> Response:
    '''hi view'''
    if request.method == 'GET':
        query_params = request.query_params
        name = query_params.get('name', '')

    elif request.method == 'POST':
        name = request.data.get('name', '')

    return Response({'hi': name}, status=status.HTTP_200_OK)


@api_view(['GET'])
def addition(request: Request) -> Response:
    '''add two number'''
    pass
    

@api_view(['GET'])
def subtraction(request: Request) -> Response:
    '''subtract two number'''
    pass
    

@api_view(['GET'])
def multiplication(request: Request) -> Response:
    '''multiply two number'''
    pass
    

@api_view(['GET'])
def division(request: Request) -> Response:
    '''divide two number'''
    pass