---
title: Exploring power and the powerful
layout: default.html
---

# Practices

There are a number of essential practices which most influence mapping project apply along the way. 

<nav><ul class="pager">
{% for grouper, list in practices | groupby('practice') %}
<li>[{{grouper}}](#{{grouper|lower}})</li>
{% endfor %}
</ul></nav>
We've organised these practices in a way that allow you to find more by looking at existing project documentation and relevant tools that can be used in the context of this practice.

</div></div><!-- dirty trick. close parent container and row--> 
<div class="container" id="main">
<div class="row">
{% for grouper, list in practices | groupby('practice') %}
## {{ grouper }}
_{{ list[0].practiceintro }}_
{% for subpractice in list %}  * [{{ subpractice.name }}](practices/{{ grouper|lower}}/{{ subpractice.id }}.html): _{{ subpractice.description }}_ 
{% endfor %}
<br>
<h3>Relevant projects <small>Consult project documentation about {{ list[0].alias }}</small></h3>
</div>
</div>
<div class="container-fluid" id="main">
<div class="row">
<div class="carousel">
{% for project in projects %}
{% if project.practice1 == grouper or project.practice2 == grouper or project.practice3 == grouper%}
<div>
<div class="panel panel-primary">
<div class="panel-heading">
<h4 class="panel-title">{{ project.name}}</h4>
</div>
<div class="panel-body">
<p><small>{{ project.description | truncate(150) }}</small></p>
<a href="projects/{{ project.id }}.html#documented-practices">Read More</a>
</div>
</div>
</div>
{% endif %}
{% endfor %}
</div>
<br>
</div>
</div>
{% set title = false %}
{% for tool in tools %}
{% if tool.practice == grouper or tool.practice_2 == grouper or tool.practice_3 == grouper %}
{% set title = true %}
{% endif %}
{% endfor %}
{% if title %}
<div class="container" id="main"><!-- dirty trick. reopen parent container -->
<div class="row">
<span class="pull-left"><h3>Relevant tools <small>Tools that can be used for {{ list[0].alias }}</small></h3></span><!--
<span class="pull-right project-filter">
<div class="btn-group" data-toggle="buttons">
<label class="btn btn-primary glyphicon glyphicon-user active" data-toggle="tooltip" data-placement="top" title="User"><input type="checkbox" autocomplete="off" checked></label><label class="btn btn-primary glyphicon glyphicon-education active" data-toggle="tooltip" data-placement="top" title="Data User"><input type="checkbox" autocomplete="off" checked></label><label class="btn btn-primary glyphicon glyphicon-wrench active" data-toggle="tooltip" data-placement="top" title="Developer"><input type="checkbox" autocomplete="off" checked></label>--></div>
</span>
</div>
</div>
{% endif %}
<div class="container-fluid" id="main">
<div class="row">
<br>
<div class="carousel">
{% for tool in tools %}
{% if tool.practice == grouper or tool.practice_2 == grouper or tool.practice_3 == grouper %}
<div>
<div class="panel panel-primary" data-toolbox-user="{{ tool.target_audience }}">
<div class="panel-heading">
<h4 class="panel-title">{{ tool.name }}</h4>
</div>
<div class="panel-body">
<p><small>{{ tool.description | truncate(150)  }}</small></p>
<a href="tools/{{ tool.id }}.html">Read More</a>
</div>
</div>
</div>
{% endif %}
{% endfor %}
</div>
</div>
</div>
<div class="container" id="main"><!-- dirty trick. reopen parent container -->
<div class="row">
{% endfor %}
</div><!--- group row -->
</div><!--- group container -->
<div class="container" id="main"><div class="row"><!-- dirty trick. reopen parent container and row -->