from django.shortcuts import render 

# =========== All these function based views customized for error that might be occurred in production =========== #

def error_404(request, expection):
    context = {"expection":expection}
    response =  render(request, 'error/404.html', context=context)
    response.status_code = 404
    return response

def error_400(request, expection):
    context = {"expection":expection}
    response =  render(request, 'error/400.html', context=context)
    response.status_code = 400
    return response

def error_403(request, expection):
    context = {"expection":expection}
    response =  render(request, 'error/403.html', context=context)
    response.status_code = 403
    return response

def error_500(request):
    response =  render(request, 'error/500.html')
    response.status_code = 500
    return response
