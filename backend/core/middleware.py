class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # trước view
        response = self.get_response(request)
        # sau view
        return response
