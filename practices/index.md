---
layout: index
title: Exploring power and the powerful
description: 
home: true
---

# Practices

List of practices

{% assign practices = site.data.practices | group_by:"Friendly Term" %}
{% for practice in practices  %}
  * {{ practice.name }} 
  {% for subpractice in practice.items %}
    * [{{ subpractice["Sub-Practice"]}}]({{ subpractice["Sub-Practice"] | slugify}}.html)
      <p> {{ subpractice.Description }} </p>

  {% endfor %}
{% endfor %}