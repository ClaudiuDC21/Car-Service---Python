from Tests.testDomain import test_domain
from Tests.testRepository import test_repository
from Tests.testService import test_service


def test_all():
    test_repository()
    test_domain()
    test_service()
