from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Member, Saving

@login_required
def index(request):
    member = Member.objects.get(user=request.user)
    savings = Saving.objects.filter(member=member)
    return render(request, 'savings/index.html', {'savings': savings})

@login_required
def update_income(request):
    if request.method == 'POST':
        member = Member.objects.get(user=request.user)
        member.monthly_income = request.POST['income']
        member.save()
    return render(request, 'savings/update_income.html')

@login_required
def pay_saving(request, saving_id):
    saving = Saving.objects.get(pk=saving_id)
    saving.is_paid = True
    saving.save()
    return render(request, 'savings/pay_saving.html')
@login_required
def total_savings(request):
    member = Member.objects.get(user=request.user)
    total = member.total_savings()
    return render(request, 'savings/total_savings.html', {'total': total})
