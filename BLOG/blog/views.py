from django.shortcuts import render


## add the rest framework for api
from rest_framework.response import Response
from rest_framework.views import APIView
## these two are for giving out data an api based structure and
## api based CURD method
from .serializers import ArticleSerializer
## include the database
from .models import Article


## we create a custom class but inherited from the APIview
## so we can use its feture

class ArticleView(APIView):

    #first 
    # def get(self,request):
    #     articles = Article.objects.all() ## fetch all the data
    #     return Response({"articles":articles})
    # [second]
    def get(self,request):
        articles = Article.objects.all() ## fetch all the data
        ## send them to the serializer
        serializer = ArticleSerializer(articles,many=True)
        return Response({"articles":serializer.data})

