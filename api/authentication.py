from tastypie.authentication import ApiKeyAuthentication

class CustomAuthentication(ApiKeyAuthentication):
    def is_auth(self, request, **kwargs):
        print(kwargs)
        if request.method == 'GET':
            print ('True')
            return True
        
        return super().is_auth(request, **kwargs)
    


