from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.utils import timezone
import INUBLOG_APP.models

appModel = INUBLOG_APP.models

def mainPage(request):
    contents_list = appModel.BlogContents.objects.all().order_by('-id')
    pagination = Paginator(contents_list, 3)
    page = request.GET.get('page')
    posts = pagination.get_page(page)

    return render(request, 'main.html', {'blogList': posts})

def newContentsPage(request):
    return render(request, 'new_contents.html')

def modifyContentsPage(request):
    return render(request, 'modify_contents.html')

def signUpPage(request):
    return render(request, 'sign_up.html')

def loginPage(request):
    return render(request, 'login_page.html')

def detailPage(request):
    contents_list = appModel.BlogContents.objects.all()
    selectedItemTitle = request.GET.get('title')

    selectedItem = ''
    for item in contents_list:
        if (item.title == selectedItemTitle):
            selectedItem = item

    return render(request, 'detail.html', {'selectedItem': selectedItem})

def newContents(request):
    contents = appModel.BlogContents()
    contents.title = request.GET['new_title']
    contents.body = request.GET['new_body']
    contents.enroll_date = timezone.datetime.now()
    contents.modify_date = timezone.datetime.now()
    contents.save()
    return redirect('/main/detail/?title=' + contents.title)