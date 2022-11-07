# Create your views here.
from .forms import ProductForm
from .models import Product
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

def index(request):
    page = request.GET.get('page', '1')  # 페이지
    kw = request.GET.get('kw', '')  # 검색어
    product_list = Product.objects.order_by('pcode')
    if kw:
        product_list = product_list.filter(
            Q(pcode__icontains=kw) |  # 코드 검색
            Q(pname__icontains=kw) |  # 교재명 검색
            Q(unitprice__icontains=kw) |  # 단가 내용 검색
            Q(author_id__icontains=kw) |  #  작성자 검색
            Q(discountrate__icontains=kw)  # 할인율 검색
        ).distinct()
    paginator = Paginator(product_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'product_list': page_obj,'page': page, 'kw': kw}
    return render(request, 'sales/product_list.html', context)

def detail(request,product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {'product': product}
    return render(request, 'sales/product_detail.html', context)

@login_required(login_url='common:login')
def product_create(request):
    """
    제품등록
    """
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES) #
        if form.is_valid():
            product = form.save()

            product.pcode
            product.pname
            product.unitprice
            product.discountrate
            product.author = request.user
            product.save()

            return redirect('sales:index')
    else:
        form = ProductForm()
        context = {'form': form}
    return render(request, 'sales/product_form.html', context)

@login_required(login_url='common:login')
def product_modify(request, product_id):

    """
    질문수정
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.user != product.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('sales:detail', product_id=product.id)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.author = request.user
            product.modify_date = timezone.now()  # 수정일시 저장
            product.save()
            return redirect('sales:detail', product_id=product.id)
    else:
        form = ProductForm(instance=product)
    context = {'form': form}
    return render(request, 'sales/product_form.html', context)


@login_required(login_url='common:login')
def product_delete(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.user != product.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('sales:detail', product_id=product.id)
    product.delete()
    return redirect('sales:index')


def board_list(request):
    product_list = Product.objects.all().order_by('pcode')

    page = int(request.GET.get('p', 1))
    paginator = Paginator(product_list, 6)
    boards = paginator.get_page(page)
    return render(request, 'product_list.html', {'boards':boards})


