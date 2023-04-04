from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def hi(request: Request) -> Response:
    '''hi view'''
    if request.method == 'GET':
        params = request.query_params
        name = params.get('name', '')
    
    elif request.method == 'POST':
        params = request.data
        name = params.get('name', '')

    return Response({'name': name})


@api_view(['GET'])
def addition(request: Request) -> Response:
    '''add two number'''
    if request.method == 'GET':
        params = request.query_params
        a = params.get('a', 0)
        b = params.get('b', 0)
        return Response({'result': int(a) + int(b)})
    

@api_view(['GET'])
def subtraction(request: Request) -> Response:
    '''subtract two number'''
    if request.method == 'GET':
        params = request.query_params
        a = params.get('a', 0)
        b = params.get('b', 0)
        return Response({'result': int(a) - int(b)})
    

@api_view(['GET'])
def multiplication(request: Request) -> Response:
    '''multiply two number'''
    if request.method == 'GET':
        params = request.query_params
        a = params.get('a', 0)
        b = params.get('b', 0)
        return Response({'result': int(a) * int(b)})
    

@api_view(['GET'])
def division(request: Request) -> Response:
    '''divide two number'''
    if request.method == 'GET':
        params = request.query_params
        a = int(params.get('a', 0))
        b = params.get('b', None)

        if b is None:
            return Response({'error': 'b is required'})
        else:
            b = int(b)
        
        if b == 0:
            return Response({'error': 'division by zero'})
        
        return Response({'result': a / b})