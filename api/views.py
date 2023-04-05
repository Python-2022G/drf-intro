from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


class HiView(APIView):
    def get(sefl, request: Request) -> Response:
        '''hi view'''
        query_params = request.query_params
        name = query_params.get('name', '')

        return Response({'hi': name}, status=status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
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
    

@api_view(['GET', 'POST'])
def division(request: Request) -> Response:
    '''divide two number'''
    if request.method == "GET":
        query_params = request.query_params
        x = query_params.get('x', 0)
        y = query_params.get('y')
    elif request.method == 'POST':
        data = request.data
        x = data.get('a', 0)
        y = data.get('b')
    
    if y is None:
        return Response({'warning': 'y is required'}, status=status.HTTP_400_BAD_REQUEST)
    elif y == '0':
        return Response({'error': 'cant divide by 0'}, status=status.HTTP_406_NOT_ACCEPTABLE)

    return Response({'result': int(x) / int(y)}, status=status.HTTP_200_OK)
