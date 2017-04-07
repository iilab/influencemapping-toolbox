---
title: Projects
layout: default
# TODO
# http://archive.stefaner.eu/projects/elastic-lists/
# http://mbaez.github.io/elastic-lists/
---

<h1 class="page-heading">Influence Mapping Projects</h1>

<div class="row">
  <form class="form form-filters">
    <div class="form-group col-md-6">
      <label for="search">Search</label>
      <input type="text" class="form-control" id="search"
        placeholder="Search for projects..." autocomplete="off">
    </div>
    <div class="form-group col-md-3">
      <label for="thematic-focus">Thematic Focus</label>
      <select class="form-control facet" id="thematic-focus">
        <option value="">Any</option>
      </select>
    </div>
    <div class="form-group col-md-3">
      <label for="intended-impact">Intended Impact</label>
      <select class="form-control facet" id="intended-impact">
        <option value="">Any</option>
      </select>
    </div>
  </form>
</div>

<table class="table table-condensed">
  {% for project in site.projects %}
    <tr id="item-{{project.slug}}" class="item"
        data-thematic-focus="{{project.thematic_focus}}"
        data-intended-impact="{{project.intended_impact}}">
      <td>
        <strong>
          <a href="{{project.url}}" class="item-title">{{project.title}}</a>
        </strong>
      </td>
      <td class="item-description">{{project.description}}</td>
      <td>
        {% if project.home_url %}
          <a href="{{project.home_url}}"><i class="fa fa-external-link-square" aria-hidden="true"></i></a>
        {% endif %}
      </td>
    </tr>
  {% endfor %}
</table>
