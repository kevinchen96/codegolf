{% extends "base.html.tpl" %}

{% block content %}
<div class="container">
<p>So if you enter your stuffs here you can do stuffs</p>

<form action="/accounts/login/" method="post">{% csrf_token %}
{{error}}
<input type="username" name="username" class="form-control" placeholder="Username" required="required"><br>
<input type="password" name="password" class="form-control" placeholder="Password" required="required"><br>
<input type="submit" value="Submit" />
</div>
{% endblock %}

