{% for grouper, list in practices | groupby('practice')  %}
  * {{ grouper }} 
  {% for subpractice in list %}
    * [{{ subpractice.name }}]({{ subpractice.id }}.html)
      <p> {{ subpractice.description }} </p>

  {% endfor %}
{% endfor %}