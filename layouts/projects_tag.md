# Projects

List of projects

{% for project in projects|sort(false,true,'id') %}
  * [{{ project.name }}](projects/{{ project.id }}.html)
    <p> {{ project.teaser }} </p>
{% endfor %}