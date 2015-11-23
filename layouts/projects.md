{{ content }}
{% for project in projects.data %}
  * [{{ project.Name }}]({{ project.Name | slugify}}.html)
    <p> {{ project.Teaser }} </p>
{% endfor %}