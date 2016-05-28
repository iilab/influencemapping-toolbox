---
title: Projects
layout: default
# TODO
# http://archive.stefaner.eu/projects/elastic-lists/
# http://mbaez.github.io/elastic-lists/
---

<h1>Influence Mapping Projects</h1>

<table class="table table-condensed">
  {% for project in site.projects %}
    <tr>
      <td><a href="{{project.url}}">{{project.title}}</a></td>
      <td>{{project.description}}</td>
      <!-- td>{{project.tags | array_to_sentence_string}}</td -->
      <td>
        {% if project.home_url %}
          <a href="{{project.home_url}}"><i class="fa fa-external-link-square" aria-hidden="true"></i></a>
        {% endif %}
      </td>
    </tr>
  {% endfor %}
</table>
