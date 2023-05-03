from django.shortcuts import render
from . models import jadwal 
from . serializers import jadwalSerializer
#rest framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def readjadwal(request):
    jadwalImsyak = jadwal.objects.all()
    serializer = jadwalSerializer(jadwalImsyak, many=True)
    return Response(serializer.data)
@api_view(['GET'])
def detailjadwal(request, id):
    jadwalImsyak = jadwal.objects.get(pk=id)
    serializer = jadwalSerializer(jadwalImsyak, many=false)
    return Response(serializer.data)
@api_view(['POST'])
def createjadwal(request):
    jadwalImsyak = jadwal.objects.all()
    serializer = jadwalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['PUT'])
def updatejadwal(request, id):
    jadwalImsyak = jadwal.objects.get(pk=id)
    serializer = jadwalSerializer(instance=jadwalImsyak, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['DELETE'])
def deletejadwal(request, id):
    jadwalImsyak = jadwal.objects.get(pk=id)
    jadwalImsyak.delete()
    return Response('data di hapus', status=204)
    
# Create your views here.
 