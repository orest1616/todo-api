import logging
from datetime import datetime

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = datetime.now()
        response = self.get_response(request)
        duration = (datetime.now() - start_time).total_seconds()

        user = request.user if request.user.is_authenticated else "Incognito"
        log_msg = f"[{request.method}] {request.path} | {response.status_code} | user: {user} | {duration:.3f}s"
        logger.info(log_msg)

        return response
