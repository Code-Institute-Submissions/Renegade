from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import MemberForm


# ABOUT PAGE
def about(request):
    """ A view to show members of the band """

    member = Member.objects.all()

    context = {
        'member': member,
    }

    return render(request, 'about/about.html', context)


# MEMBER INFO
def member_info(request, member_id):
    """ A view to show band member information """

    member = get_object_or_404(Member, pk=member_id)

    context = {
        'member': member,
    }

    return render(request, 'about/member_info.html', context)


# ADD BAND MEMBER
@login_required
def add_member(request):
    """ Add a band member to the About section """
    if not request.user.is_superuser:
        messages.error(request, 'No access! Only page admin can do that.')
        return redirect(reverse('about'))

    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES)
        if form.is_valid():
            member = form.save()
            messages.success(request, 'Successfully added band member!')
            return redirect(reverse('about'))
        else:
            messages.error(request, 'Failed to add member. Please ensure the form is valid.')
    else:
        form = MemberForm()

    template = 'about/add_member.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


# EDIT BAND MEMBER
@login_required
def edit_member(request, member_id):
    """ Edit a member of the band page """
    if not request.user.is_superuser:
        messages.error(request, 'No access! Only page admin can do that.')
        return redirect(reverse('about'))

    member = get_object_or_404(Member, pk=member_id)
    if request.method == 'POST':
        form = MemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully edited the band member!')
            return redirect(reverse('member_info', args=[member.id]))
        else:
            messages.error(request, 'Failed to update band member. Please ensure the form is valid.')
    else:
        form = MemberForm(instance=member)
        messages.info(request, f'You are editing {member.name}')

    template = 'about/edit_member.html'
    context = {
        'form': form,
        'member': member,
    }

    return render(request, template, context)


# DELETE BAND MEMBER
@login_required
def delete_member(request, member_id):
    """ Delete a member from the band page """
    if not request.user.is_superuser:
        messages.error(request, 'No access! Only page admin can do that.')
        return redirect(reverse('about'))

    member = get_object_or_404(Member, pk=member_id)
    member.delete()
    messages.success(request, 'Member deleted!')
    return redirect(reverse('about'))
