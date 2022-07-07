from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import generics,mixins
import urllib.request

from .models import Mini
from .serializers import MiniSerializer


@api_view(['POST','GET'])
def alter_view(request, pk=None):
    method=request.method
    if method=='POST':
        list=Mini.objects.all()
        data=MiniSerializer(list,many=True).data
        return Response(data)
    
    
@api_view(['POST','GET'])   
def detail_view(request, id=None):
    method=request.method
    if method =='GET':
        if id is not None:
            detail=get_object_or_404(Mini,id=id)
            data=MiniSerializer(detail,many=False).data
    return Response(data)


@api_view(['POST','GET'])   
def create_view(request, id=None):
    method=request.method
    if method =='POST':
       serializer = MiniSerializer(data=request.data)
       if serializer.is_valid(raise_exception=True):
             name = serializer.validated_data.get('name')
             title = serializer.validated_data.get('title') or None
             if name is None:
                name=title
             serializer.save(name=name)
             return Response(serializer.data) 
    return Response({'validation':'not the site'})
        
    
class List_VIew(generics.ListAPIView):
    queryset = Mini.objects.all()
    serializer_class = MiniSerializer
    lookup_field = 'pk'
    
    
    
class Detail_View(generics.RetrieveAPIView):
    queryset = Mini.objects.all()
    serializer_class = MiniSerializer
    lookup_field = 'pk'
    

class MixinsView(mixins.RetrieveModelMixin,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 generics.GenericAPIView):
    
    queryset =  Mini.objects.all()
    serializer_class =  MiniSerializer
    lookup_field = 'pk'
    
    
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request,*args,**kwargs) 
        return self.list(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)
    
    
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.update(request,*args,**kwargs) 
        
    def post(self,request,*args,**kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.destroy(request,*args,**kwargs) 
    
    
    
     
    
    
    
        
         
