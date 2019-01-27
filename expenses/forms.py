from django import forms
from expenses.models import Member
class ExpenseSplitForm(forms.Form):
	members_split=forms.ModelMultipleChoiceField(Member.objects.all())
class ReportForm(forms.Form):
	months=[i for i in zip(range(0,13),['',"JAN","FEB","MAR","APR","MAY","JUNE","JUL","AUG","SEP","OCT","NOV","DEC"])]
	month = forms.ChoiceField(choices=months, required=False)
	member = forms.ModelChoiceField(Member.objects.all(),required=False)