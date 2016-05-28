---
title: Tools
layout: default
---

<h1>Influence Mapping Tools</h1>

<table class="table table-condensed">
  {% for tool in site.tools %}
    <tr>
      <td><a href="{{tool.url}}">{{tool.title}}</a></td>
      <td>{{tool.description}}</td>
      <td>{{tool.tags | array_to_sentence_string}}</td>
      <td>
        {% if tool.home_url %}
          <a href="{{tool.home_url}}"><i class="fa fa-external-link-square" aria-hidden="true"></i></a>
        {% endif %}
      </td>
    </tr>
  {% endfor %}
</table>
