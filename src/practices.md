---
title: Exploring power and the powerful
description: 
home: true
---

# Practices

List of practices

{% for grouper, list in practices | groupby('practice') %}
### __{{ grouper }}__

__{{ list[0].practiceintro }}__

  {% for subpractice in list %}* [{{ subpractice.name }}](practices/subpractices/{{ subpractice.id }}.html): _{{ subpractice.tagline }}_ 

  {% endfor %}

{% endfor %}