from multiprocessing import context
from django.shortcuts import render,redirect
from .models import *
import json
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'home.html', context)

# 상품 상세페이지
def detail(request,product_id):
    product = Product.objects.get(id = product_id)
    context = {
        'product':product
    }
    return render(request, 'detail.html',context )



# 장바구니 페이지
def cart(request):
    # 로그인한 사용자에 한해서만 장바구니사용가능
    # 비회원은 사용불가 -> 로그인페이지로 이동
    if request.user.is_authenticated:
        member = request.user.member

        items = member.cart_set.all()
        total_price = member.get_cart_total()
    else:
        messages.warning(request,"장바구니는 로그인 후 이용 가능합니다.")
        return redirect("accounts:login")

    context = {
        'items': items, 
        'total_price': total_price}
        
    return render(request, 'cart.html', context)


# 장바구니 담기
def add_cart(request, product_id):
    # 로그인 한 경우
    if request.user.is_authenticated:
        member = request.user.member

        # 선택한 수량
        amount = int(request.POST.get('amount'))
        
        # 선택한 수량이 0개면 오류메시지 전달
        if(amount == 0):
            messages.warning(request,"수량을 확인해주세요.")
            return redirect("/shop/"+str(product_id)+"/detail")

        # 이미 장바구니에 있는 상품이면 원래갯수에 더해서 저장 
        # 처음 장바구니에 넣는 상품이면 선택한 수량만큼 저장
        try:
            cartItem = Cart.objects.get(product=product_id, member=member.id)
            if cartItem:
                cartItem.cart_count += amount
                cartItem.save()
        except Cart.DoesNotExist:
            product = Product.objects.get(id = product_id)
            cartItem = Cart()
            cartItem.member = member
            cartItem.product = product
            cartItem.cart_count = amount
            cartItem.save()

    # 로그인 안한 경우
    else:
        pass 


    return redirect("cart")    


# 장바구니 수량 감소(ajax)
def count_down(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        cart_id = data.get("cart_id")
        count = data.get("count")
        
        if(int(count) <= 1):
            pass
        else:
            cart = Cart.objects.get(id=cart_id)
            cart.cart_count = int(count)-1
            cart.save()
        
        context = {
            'cart_id' : cart_id,
            'count' : count,
        }
        
        return JsonResponse(context)

# 장바구니 수량 증가(ajax)
def count_up(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        
        cart_id = data.get("cart_id")
        count = data.get("count")

        cart = Cart.objects.get(id=cart_id)
        cart.cart_count = int(count)+1
        cart.save()

        context = {
            'cart_id' : cart_id,
            'count' : count,
        }

        return JsonResponse(context)