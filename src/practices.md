---
title: Exploring power and the powerful
layout: default.html
---

# Practices

List of practices

{% for grouper, list in practices | groupby('practice') %}
### {{ grouper }}
_{{ list[0].practiceintro }}_
{% for subpractice in list %}  * [{{ subpractice.name }}](practices/subpractices/{{ subpractice.id }}.html): _{{ subpractice.description }}_ 
{% endfor %}
<br>
<div class="content panel panel-primary">
{% for project in projects %}
{% if project.practice1 == grouper %}
<div>
<div class="panel-heading">
<h3 class="panel-title">{{ project.title}}</h3>
</div>
<div class="panel-body">
[Read {{ project.name }}'s project documentation](projects/{{ project.id }}.html#documented-practices)
</div>
</div>
{% endif %}
{% endfor %}
</div>
<div class="row">
<div class="carousel">
{% for project in projects %}
{% if project.practice1 == grouper %}
<div class="col-md-4">
<div class="panel panel-primary">
<div class="panel-heading">
<h4 class="panel-title">{{ project.name}}</h4>
</div>
<div class="panel-body">
<p>{{ project.description }}</p>
<a href="#">Read More</a>
</div>
</div>
</div>
{% endif %}
{% endfor %}
</div>
</div>
<br>
{% endfor %}