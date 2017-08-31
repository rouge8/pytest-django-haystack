import pytest


__version__ = '0.1.1'


def pytest_configure(config):
    # Register the marks
    config.addinivalue_line(
        'markers',
        'haystack: Mark the test as using the django-haystack search engine, '
        'rebuilding the index for each test.')


@pytest.fixture(autouse=True)
def _haystack_marker(request):
    """
    Implement the 'haystack' marker.

    This rebuilds the index at the start of each test and clears it at the end.

    Takes an optional connection parameter; if set, clears and rebuilds
    only the specified haystack connections.
    """
    marker = request.keywords.get('haystack', None)

    if marker:
        from pytest_django.lazy_django import skip_if_no_django
        from django.core.management import call_command
        request.getfuncargvalue('db')

        # optional haystack connection parameter
        # if specified, pass to clear_index and rebuild_index
        connection = marker.kwargs.get('connection', None)
        index_args = {}
        if connection:
            index_args['using'] = connection

        def clear_index():

            call_command('clear_index', interactive=False, **index_args)

        # Skip if Django is not configured
        skip_if_no_django()

        request.addfinalizer(clear_index)

        call_command('rebuild_index', interactive=False, **index_args)
