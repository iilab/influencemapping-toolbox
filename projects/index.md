---
layout: index
title: Projects
description: 
home: true
---

# Projects

List of projects

{% for project in site.data.projects %}
  * [{{ project.Name }}]({{ project.Name | slugify}}.html)
    <p> {{ project.Teaser }} </p>
{% endfor %}
