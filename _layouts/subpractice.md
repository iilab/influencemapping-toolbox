## {{ practice }} {% if alias %}({{ alias }}){% endif %}

# {{ name }} 

_{{ description }}_

__{{ intro }}__

{{ body }}

</div></div><!-- dirty trick. close parent container and row--> 
{% set title = false %}
{% for project in projects %}
{% if project.subpractice1 == name or project.subpractice2 == name or project.subpractice3 == name %}
{% set title = true %}
{% endif %}
{% endfor %}
{% if title %}
<div class="container">
<div class="row">
<br>
<h3>Relevant projects <small>Consult project documentation about this practice</small></h3>
</div>
</div>
{% endif %}
<div class="container-fluid">
<div class="row">
<div class="carousel">
{% for project in projects %}
{% if project.subpractice1 == name or project.subpractice2 == name or project.subpractice3 == name %}
<div>
<div class="panel panel-primary">
<div class="panel-heading">
<h4 class="panel-title">{{ project.name}}</h4>
</div>
<div class="panel-body">
<p><small>{{ project.description | truncate(150) }}</small></p>
<a href="../../projects/{{ project.id }}.html#documented-practices">Read More</a>
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
{% if tool.sub_practice == name or tool.sub_practice_2 == name or tool.sub_practice_3 == name %}
{% set title = true %}
{% endif %}
{% endfor %}
{% if title %}
<div class="container"><!-- dirty trick. reopen parent container -->
<div class="row">
<span class="pull-left"><h3>Relevant tools <small>Tools that can be of use to apply this practice</small></h3></span>
<span class="pull-right project-filter">
<div class="btn-group" data-toggle="buttons">
<label class="btn btn-primary glyphicon glyphicon-user active" data-toggle="tooltip" data-placement="top" title="User"><input type="checkbox" autocomplete="off" checked></label><label class="btn btn-primary glyphicon glyphicon-education active" data-toggle="tooltip" data-placement="top" title="Data User"><input type="checkbox" autocomplete="off" checked></label><label class="btn btn-primary glyphicon glyphicon-wrench active" data-toggle="tooltip" data-placement="top" title="Developer"><input type="checkbox" autocomplete="off" checked></label>
</div>
</span>
</div>
</div>
{% endif %}
<div class="container-fluid">
<div class="row">
<br>
<div class="carousel">
{% for tool in tools %}
{% if tool.sub_practice == name or tool.sub_practice_2 == name or tool.sub_practice_3 == name %}
<div>
<div class="panel panel-primary" data-toolbox-user="{{ tool.target_audience }}">
<div class="panel-heading">
<h4 class="panel-title">{{ tool.name }}</h4>
</div>
<div class="panel-body">
<p><small>{{ tool.description | truncate(150)  }}</small></p>
<a href="../../tools/{{ tool.id }}.html">Read More</a>
</div>
</div>
</div>
{% endif %}
{% endfor %}
</div>
</div>
</div>
<div class="container"><!-- dirty trick. reopen parent container -->
<div class="row">
</div><!--- group row -->
</div><!--- group container -->
<div class="container"><div class="row"><!-- dirty trick. reopen parent container and row -->