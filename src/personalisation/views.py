from __future__ import absolute_import, unicode_literals

from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from personalisation.models import (
    ReferralRule, Segment, TimeRule, VisitCountRule)


def overview(request):
    """Display segments overview. Dummy function"""
    return render(request, 'wagtailadmin/segment.html')

def enable(request, segment_id):
    """Enable the selected segment"""
    segment = get_object_or_404(Segment, pk=segment_id)
    segment.status = 'enabled'
    segment.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def disable(request, segment_id):
    """Disable the selected segment"""
    segment = get_object_or_404(Segment, pk=segment_id)
    segment.status = 'disabled'
    segment.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

# TODO: Make these requestable from an exsisting page (the create page.)
# This code might become obselete.

class TimeRuleForm(ModelForm):
    """Create a form for the time rule model."""
    class Meta:
        model = TimeRule
        fields = ['start_time', 'end_time']

def time_rule_embed(request):
    """Show the content of the time rule modal."""
    return render(request, 'wagtailadmin/embeds/time_rule.html', {
        'form_fields': TimeRuleForm(),
    })

class ReferralRuleForm(ModelForm):
    """Create a form for the referral rule model."""
    class Meta:
        model = ReferralRule
        fields = ['regex_string']

def referral_rule_embed(request):
    """Show the content of the referral rule modal."""
    return render(request, 'wagtailadmin/embeds/referral_rule.html', {
        'form_fields': ReferralRuleForm,
    })

class VisitCountRuleForm(ModelForm):
    """Create a form for the visit count rule model."""
    class Meta:
        model = VisitCountRule
        fields = ['operator', 'count']

def visit_c_rule_embed(request):
    """Show the content of the visit count rule modal."""
    return render(request, 'wagtailadmin/embeds/visit_count_rule.html', {
        'form_fields': VisitCountRule,
    })
