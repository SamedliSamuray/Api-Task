from rest_framework.generics import ListAPIView,ListCreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework import filters
from ..models import Blog
from .serializers import BlogSerializer

class BlogListAPIView(ListAPIView):
    queryset=Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['create_date']
    
class BlogCreateAPIView(ListCreateAPIView):
    queryset=Blog.objects.all()
    serializer_class = BlogSerializer
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
    
class BlogUpdateAPIView(UpdateAPIView):
    queryset=Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field='pk'
    
class BlogDestroyAPIView(DestroyAPIView):
    queryset=Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field='pk'
    
class BlogRetrieveAPIView(RetrieveAPIView):
    queryset=Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field='pk'
