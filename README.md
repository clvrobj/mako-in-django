mako-in-django
==============

Let's include mako template in django template

##Install
1. Copy /templatetags folder to any app in your django project, make sure that app is in  INSTALLED_APPS of settings.py
2. Add below into settings.py:

    ```python
    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.request',
        )
    ```
    
    
    
    This pass request instance to mako template.

3. In django template:

    ```html
    {% load mako_ext %}
    {% include_mako_template 'path/to/mako_template.html' %}
    ```
    or if you want to pass some keyword arguments:
    ```html
    {% load mako_ext %}
    {% include_mako_template 'path/to/mako_template.html' arg1=value1 arg2=value2 %}
    ```
