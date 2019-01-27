from django.shortcuts import render, redirect
from django.db.models import Avg, Count, Min, Sum
from expenses.models import Expense
from expenses.forms import ExpenseSplitForm, ReportForm
# Create your views here.
def reports(request):
	object_list=[]
	exp_sum=0
	form = ReportForm()
	if request.method=="POST":
		form=ReportForm(request.POST)
		form.is_valid()
		search_data=form.cleaned_data
		month = search_data.get("month")
		member=search_data.get("member")
		if month:
			object_list=Expense.objects.filter(datetime__month=request.POST.get("month"))
		if member:
			object_list = object_list.filter(user=member)
		exp_sum = object_list.aggregate(Sum('amount')).get("amount__sum")
	return render(request,"expenses/reports.html",
		{"object_list":object_list,"exp_sum":exp_sum,"search_form":form}
		)
def expense_split_view(request, expense_id):
	msg=""
	expense = Expense.objects.get(id=expense_id)
	if request.method=="POST":
		form = ExpenseSplitForm(request.POST)
		form.is_valid()
		data = form.cleaned_data.get("members_split")
		number_members = len(data)
		if number_members>0:
			amount = expense.amount/number_members
			for i in data:
				exp = Expense(comment=expense.comment,
					datetime=expense.datetime,
					amount=amount,
					user=i)
				exp.save()
			expense.delete()
			return redirect("/expenses")
		else:
			msg="expense not splitted!!"
	return render(request, "expenses/expense_split.html",
		{"expense":expense,"split_form":ExpenseSplitForm,"msg":msg})
