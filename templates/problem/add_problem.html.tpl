{% extends "base.html.tpl" %}

{% block content %}
    <form action="/problem/add/" method="post">{% csrf_token %}
    {{form.as_p}}
    <input type="submit" value="Submit" />
{% endblock %}
