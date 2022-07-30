from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# 회원
class Member(models.Model):
    # 장고가 지원하는 User모델을 일대일매핑(OneToOneField)을 통해 참조한다.
    # 그냥 User모델을 사용할 수도 있는데 따로 Member모델을 만든 이유는,
    # 아이디,비밀번호 말고도 유저이름, 주소, 이메일, 연락처를 따로 받아야 되기 때문.

    # 참고로, models.CASCADE는 pk-fk관계에서 pk가 지워질경우 그에 따른 fk를 모두 자동으로 지운다는 뜻. 
    user = models.OneToOneField(User,on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    pnumber = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return str(self.user)


# 카테고리
class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name

# 상품
class Product(models.Model):
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.SET_NULL)
    img = models.ImageField(null=True, blank= True)
    
    brand = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date publicshed', default = timezone.now)
    is_crolled = models.BooleanField(default=True) #크롤링한 상품과 우리가 등록한 상품을 구별하기 위해 넣어놨음.
    
    def __str__(self): 
        return self.name


#장바구니
class Cart(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    cart_count = models.IntegerField()

    def __str__(self):
        return str(self.member.id)


#주문
class Order(models.Model):
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.IntegerField() #주문번호
    order_status = models.BooleanField(default=False, null=True, blank=True)
    order_date = models.DateTimeField(auto_now_add=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


#주문상품
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, blank=True, null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    orderPrice = models.IntegerField()

    def __str__(self):
        return self.product.name


#배송
class Delivery(models.Model):
    member = models.ForeignKey(Member, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    address = models.CharField(max_length=200)
    delivery_status = models.BooleanField(default=False, null=True, blank=True)
    delivery_date = models.DateTimeField(auto_now_add=True)
    delivery_comment = models.CharField(max_length=200)
    
    def __str__(self):
        return self.address



#FAQ게시판
class Board(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100)
    b_content = models.CharField(max_length=300)
    b_img = models.ImageField(null=True, blank=True)
    b_date = models.DateTimeField(auto_now_add=True)


#댓글
class Comment(models.Model):
    board = models.ForeignKey(Board,on_delete=models.CASCADE, blank=True, null=True)
    is_admin = models.BooleanField(default=False) #관리자만 달 수 있으므로 관리자인지 체크
    c_content = models.CharField(max_length=100)
    c_date = models.DateTimeField(auto_now_add=True)












