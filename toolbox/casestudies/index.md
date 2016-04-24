---
layout: default
title: Case Studies
studies:
    - title: Cargografias
      image: images/cargografias.png
      path: cargografias.html
    - title: Influence Map
      image: images/influence_map.png
      path: influence_map.html
    - title: La Fabrique de la Loi
      image: images/la_fabrique_de_la_loi.png
      path: la_fabrique_de_la_loi.html
    - title: LobbyRadar
      image: images/lobbyradar.png
      path: lobbyradar.html
    - title: Open Duka
      image: images/open_duka.png
      path: open_duka.html
    - title: Parltrack
      image: images/parltrack.png
      path: parltrack.html
    - title: Political Party Time
      image: images/political_party_time.png
      path: political_party_time.html
---

# Case Studies

<div class="row">
    <div class="col-md-3">
        We picked a handful of projects for deeper investigation, and interviewed project representatives to explore further the influence mapping space. These projects represent diverse practices, geographical and thematic focus, and technological approaches. 
    </div>
    <div class="col-md-9">        
        <div class="row" id="case-study-index">
            {% for study in page.studies %}
                <div class="col-md-6">
                    <div class="case-study">
                        <a href="{{study.path}}"><img src="{{study.image}}"></a>
                        <a href="{{study.path}}" class="title">{{study.title}}</a>
                    </div>
                </div>
            {% endfor %}
        </div>
    </div>
</div>
