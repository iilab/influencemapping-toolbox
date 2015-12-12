---
title: Projects
description: 
home: true
---

# Projects

List of projects

{% for project in projects %}
  * [{{ project.name }}](projects/{{ project.id }}.html)
    <p> {{ project.teaser }} </p>
{% endfor %}