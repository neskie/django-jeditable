from django.contrib.flatpages.models import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required
from django.db.models import get_model
from django.http import HttpResponseRedirect

@login_required
def edit(request,model_app,model_name, object_id):
    '''Edits a field from a model. If it is a get request it should return a
    plain text version of a template, and if it is a POST request it should
    return an html representation of the text.'''
    user = request.user
    model_class = get_model(model_app, model_name)
    try:
        model_object = model_class._default_manager.get(id=object_id)
    except:
        model_object = model_class._default_manager.none()
    if request.method == 'GET':
        field = request.GET.get('id', 'field')
        try:
            value = model_object.__getattribute__(field)
        except:
            value = model_object
        templates = ['jeditable/model_field.html',
                    'jeditable/%s_field.html' % model_app,
                    'jeditable/%s_%s.html' % (model_app, field) ]
        return render_to_response(templates,
                        {'field': value },
                        context_instance=RequestContext(request))

    elif request.method == 'POST':
        if user.has_perm('can_change_%s' % model_name):
            field = request.POST.get('id', '')
            value = request.POST.get('value', '')
            model_object.__setattr__(field, value)
            model_object.save()
            model_object = model_class._default_manager.get(id=object_id)

            return render_to_response([ 'jeditable/%s_%s.html' % (model_app, field ),
                'jeditable/%s_field.html' % (model_app ),
                'jeditable/post_model_%s.html' % field, 'jeditable/model_field.html'],
                        {'field': value},
                        context_instance=RequestContext(request))
        else:
            return HttpResponseRedirect(model_object.get_absolute_url())
