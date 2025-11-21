from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms

# Создание заказа
def createOrderView(request, book_id=None):
    if request.method == 'POST':
        form = forms.OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        if book_id:
            form = forms.OrderForm(initial={'book': book_id})
        else:
            form = forms.OrderForm()
    return render(request, 'order/order_create.html', {'form': form})


# Список заказов
def orderListView(request):
    orders = models.OrderModels.objects.all().order_by('-id')
    return render(request, 'order/order_list.html', {'orders': orders})


# Обновление заказа
def updateOrderView(request, id):
    order = get_object_or_404(models.OrderModels, id=id)
    if request.method == 'POST':
        form = forms.OrderForm(request.POST, request.FILES, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = forms.OrderForm(instance=order)
    return render(request, 'order/order_update.html', {'form': form, 'order': order})


# Удаление заказа
def deleteOrderView(request, id):
    order = get_object_or_404(models.OrderModels, id=id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')
    return render(request, 'order/order_confirm_delete.html', {'order': order})
