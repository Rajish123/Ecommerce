from django.shortcuts import redirect

# if you specify path i.e, store.middlewares.auth.auth_middleware in middleware/settings. It will
# always run before any view
def auth_middleware(get_response):

    def middleware(request):
        if not request.session.get('customer'):
            return redirect('account:login')
        response = get_response (request)
        return response
    return middleware