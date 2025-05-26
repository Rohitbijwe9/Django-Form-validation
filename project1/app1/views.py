from django.shortcuts import render

def UserFormView(request):
    template_name = 'app1/UserForm.html'
    message = ''
    data = {}

    if request.method == 'GET':
        first = request.GET.get('first_name', '')
        last = request.GET.get('last_name', '')
        mobile = request.GET.get('mobile', '')
        email = request.GET.get('email', '')

        if not first:
            message = 'First name required'
        elif not last:
            message = 'Last name required'
        elif len(mobile) < 10 or len(mobile) > 13 or not mobile.isdigit():
            message = 'Mobile number invalid'
        elif '@' not in email or '.' not in email:
            message = 'Email invalid'
        else:
            data = {'first': first, 'last': last, 'mobile': mobile, 'email': email}

    return render(request,template_name,{'message': message, 'data': data})
