---
layout: none
---

# {{ friendly_term }} 

{% for group, list in practices | groupby('friendly_term') -%}
  {% for practice in list %}{% if practice.friendly_term == friendly_term %}
  * [{{ practice.name }}]({{ practice.id }}.html)
    <p> {{ practice.category }} {{ practice.tagline }} </p>
    <p> {{ practice.description }} </p>
{% endif %}{%- endfor -%}{%- endfor -%}
