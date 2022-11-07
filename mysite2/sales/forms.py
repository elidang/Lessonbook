from django import forms
from sales.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product  # 사용할 모델
        fields = ['pcode', 'pname', 'unitprice', 'discountrate', 'imgfile'] #

        labels = {
            'pcode': '제품 코드 ',
            'pname': '제  품  명 ',
            'unitprice': '단   가 ',
            'discountrate': '할 인 율 ',
            'imgfile': '이 미 지',
        }  #
