<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <link href="/static/css/bootstrap.css" rel="stylesheet">
    <link href="/static/css/style.css" rel="stylesheet">
    <link href="/static/css/flat-ui.css" rel="stylesheet">
    <link href="http://fonts.googleapis.com/css?family=Oswald:700|Droid+Serif:400,700italic" rel="stylesheet" type="text/css" />
    {% block head %} {% endblock %}
</head>
<body>

<div class="container">
<br>
<h1>CodeGolf</h1>
<a href="/accounts/logout/"> Logout </a>
<a href="/accounts/login/"> Login </a>

</div>
{% block content %} {% endblock %}


</body>
</html>
