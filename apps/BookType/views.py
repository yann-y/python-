from django.views.generic import View
from django.shortcuts import render
from apps.BookType.models import BookType
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect


class FrontAddView(View):
    def get(self,request):
        return render(request, 'BookType/bookType_add.html')
    def post(self,request):
        print("添加图书类型************************")
        id = request.POST.get("bookType_Id")
        name = request.POST.get("bookType_Name")
        day = request.POST.get("bookType_Day")
        print(id, name, day)
        BookType.objects.create(bookTypeId=id,bookTypeName=name,days=day)
        print(id,name,day)
        return redirect("BookType:frontList")


class ListAllView(View):
    def get(self,request):
        bookTypes = BookType.objects.all()
        bookTypeList = []
        for bookType in bookTypes:
            bookTypeObj = {
                'bookTypeId': bookType.bookTypeId,
                'bookTypeName': bookType.bookTypeName,
            }
            bookTypeList.append(bookTypeObj)
        return JsonResponse(bookTypeList,safe=False)

class FrontEditView(View):
    def get(self,request):
        type_Id=request.GET.get("type_Id")
        type_Name = request.GET.get("type_Name")
        type_Day = request.GET.get("type_Day")
        return render(request, "BookType/bookType_edit.html", {"bookType_Id": type_Id, "bookType_Name": type_Name,"bookType_Day":type_Day})

    def post(self,request):
        id = request.POST.get("bookType_Id")
        name = request.POST.get("bookType_Name")
        day = request.POST.get("bookType_Day")
        print(id, name, day)
        result = BookType.objects.filter(bookTypeId=id).update(bookTypeId=id, bookTypeName=name, days=day)
        print(id, name, day)
        return redirect("BookType:frontList")

class FrontDeleteView(View):
    def get(self,request):
        type_Id = request.GET.get("type_Id")
        BookType.objects.filter(bookTypeId=type_Id).delete()
        return redirect("BookType:frontList")



class FrontListView(View):
    def get(self,request):
        pageSize = 5
        currentPage = request.GET.get("currentPage")
        bookTypes = BookType.objects.all()
        paginator = Paginator(bookTypes, pageSize)
        totalPage = paginator.num_pages
        recordNumber = paginator.count

        # 获取第page页的内容
        try:
            currentPage = int(currentPage)
        except Exception as e:
            currentPage = 1
        if currentPage > totalPage:
            currentPage = totalPage

        # 获取第page页的Page实例对象
        bookTypes_page = paginator.page(currentPage)

        startIndex = (currentPage - 1) * pageSize #计算起始序号


        startPage = currentPage - 5
        endPage = currentPage + 5
        if startPage < 1:
            startPage=1
        if endPage > totalPage:
            endPage = totalPage;

        pageList = list(range(startPage,endPage+1))

        context = {
            'bookTypes_page': bookTypes_page,
            'currentPage': currentPage,
            'totalPage': totalPage,
            'recordNumber': recordNumber,
            'startIndex': startIndex,
            'pageList': pageList,
        }

        print(pageList)

        # 使用模板
        return render(request, 'BookType/bookType_frontquery_result.html', context)


    def post(self,request):
        pass



