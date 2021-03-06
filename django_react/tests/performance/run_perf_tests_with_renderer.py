if __name__ == '__main__':
    import os
    import sys
    import django

    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'django_react.tests.performance.settings.renderer_settings'

    django.setup()

    from django_react.tests.performance.perf_tests import run_perf_test

    print('Running perf test with a renderer which boots node on every render request...')

    run_perf_test()