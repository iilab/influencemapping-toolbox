{{ content }}
{% for grouper, list in practices.data | groupby('Friendly Term')  %}
  * {{ grouper['Friendly Term'] }} 
  {% for subpractice in list %}
    * [{{ subpractice["Sub-Practice"]}}]({{ subpractice["Sub-Practice"] | slugify}}.html)
      <p> {{ subpractice.Description }} </p>

  {% endfor %}
{% endfor %}