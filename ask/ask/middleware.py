import datetime
from qa.models import Session


class CheckSessionMiddleware(class):
    def process_request(request):
        pass
    '''
        try:
            sessid = request.COOCKIE.get('sessid')
            session = Session.objects.get(
                    key=sessid,
                    expires__gt=datetime.now(),
            )
            request.session = session
            request.user = session.user 
        except Session.DoesNotExist:
            request.session = None
            request.user = None
    '''
