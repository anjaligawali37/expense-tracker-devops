from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ExpenseForm
from .models import Expense


@login_required
def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)

        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            return redirect("view_expenses")

    else:
        form = ExpenseForm()

    return render(request, "expenses/add_expense.html", {"form": form})


@login_required
def view_expenses(request):
    expenses = Expense.objects.filter(user=request.user)
    return render(
        request,
        "expenses/view_expenses.html",
        {"expenses": expenses}
    )