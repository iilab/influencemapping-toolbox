---
title: Tools
layout: default
---

<h1 class="page-heading">Influence Mapping Tools</h1>

<div class="row">
  <form class="form form-filters">
    <div class="form-group col-md-6">
      <label for="search">Search</label>
      <input type="text" class="form-control" id="search"
        placeholder="Search for projects..." autocomplete="off">
    </div>
    <div class="form-group col-md-3">
      <label for="usage-audience">Usage Audience</label>
      <select class="form-control facet" id="usage-audience">
        <option value="">Any</option>
      </select>
    </div>
    <div class="form-group col-md-3">
      <label for="programming-language">Programming Language</label>
      <select class="form-control facet" id="programming-language">
        <option value="">Any</option>
      </select>
    </div>
  </form>
</div>

<table class="table table-condensed">
  {% for tool in site.tools %}
    <tr id="item-{{tool.slug}}" class="item"
        data-usage-audience="{{tool.usage_audience}}"
        data-programming-language="{{tool.programming_language}}">
      <td>
        <strong>
          <a href="{{tool.url}}" class="item-title">{{tool.title}}</a>
        </strong>
      </td>
      <td class="item-description">{{tool.description}}</td>
      <!-- td>{{tool.tags | array_to_sentence_string}}</td -->
      <td>
        {% if tool.home_url %}
          <a href="{{tool.home_url}}"><i class="fa fa-external-link-square" aria-hidden="true"></i></a>
        {% endif %}
      </td>
    </tr>
  {% endfor %}
</table>
