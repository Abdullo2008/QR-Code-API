from rest_framework.decorators import api_view
from rest_framework.response import Response

from qrapp.tests import combine_photo


# from .models import QRModel
# from .serializers import QRSerializer


# def my_view(request):
#
#     full_url = request.build_absolute_uri()
#     Response(f"{full_url}/media/qr_kode/img.jpg")


# class QRAPIView(generics.ListAPIView):
#     queryset = QRModel
#     serializer_class = QRSerializer


# class QRAPIView(APIView):
#
#     serializer_class = QRSerializer
#
#     def post(self, request):
#
#         serializer = QRSerializer(data=request.data, context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'status': True,
#                 'message': 'Success',
#                 'Data': serializer.data},
#                 status=status.HTTP_201_CREATED)
#         else :
#             return Response({
#                 'status': False,
#                 'message': "Error"},
#                 status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def create_qr(request):
    data = request.data

    img = combine_photo(text=data['text'])
    host_name = request.get_host()
    return Response({"img": f"{host_name}/{img}",
                    'successful': True})
