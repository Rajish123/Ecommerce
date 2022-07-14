from django.shortcuts import redirect

# if you specify path i.e, store.middlewares.auth.auth_middleware in middleware/settings. It will
# always run before any view
def auth_middleware(get_response):

    def middleware(request):
        # from which url the request is coming
        # returns a url, which you havve visited.In this case you cannot visit order page without login,
        # if you visit order page by logging in and clear the cookies, and again tried to visit 
        # order page you are redirected to login page.
        # PATH_INFO shows from which url you are redirected. Here url is orders/order

        returnUrl = request.META['PATH_INFO']
        # print(request.META['PATH_INFO'])
        
        if not request.session.get('customer'):
            # now if you login you will be directly redircted to orders page
            return redirect(f'/accounts/log?return_url={returnUrl}')
        response = get_response (request)
        return response
    return middleware