{{ content }}
{% for grouper, list in practices | groupby('friendly_term')  %}
  * {{ grouper }} 
  {% for subpractice in list %}
    * [{{ subpractice.name }}]({{ subpractice.id }}.html)
      <p> {{ subpractice.description }} </p>

  {% endfor %}
{% endfor %}