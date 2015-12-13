# {{ name }}

![]({{ image }})

_{{ teaser }}_

{% if url %}{{ url }}{% endif %}
{% if code_url %}

{% if language %}
Keywords
: {{ keywords }}
{% endif %}


{% if thematic_focus %}
Thematic Focus
: {{ thematic_focus }}
{% endif %}

{% if issue_addressed %}
Issue addressed
: {{ issue_addressed }}
{% endif %}

{% if geographic_focus %}
Geographic Focus
: {{ geographic_focus }}
{% endif %}

{% if narrative or query or geographic_map or timelines or lists or network_viz or other__viz or export %}
Experience
: {% if narrative %} Narrative {% endif %} {% if query %} Query {% endif %} {% if geographic_map %} Geographic Map{% endif %} {% if timelines %} Timelines {% endif %} {% if lists %} Lists {% endif %} {% if network_viz %} Network Visualisation{% endif %} {% if other__viz %} Other Visualisation{% endif %} {% if export %} Raw Data {% endif %}
{% endif %}

## Description

__{{ description }}__

{% if rationale_why %}
Rationale (Why?)
: {{ rationale_why }}
{% endif %}

{% if approach_how %}
Approach (How?)
: {{ approach_how }}
{% endif %}

{% if language %}
Language
: {{ language }}
{% endif %}

{% if commissioner %}
Commissioner
: {{ commissioner }}
{% endif %}

{% if publisher %}
Publisher
: {{ publisher }} ({% if publisher_country %}{{ publisher_country }}){% endif %}
{% endif %}

{% if partners %}
Partners
: {{ partners }}
{% endif %}

## Impact

{% if intended_impact %}
Intended Impact
: {{ intended_impact }}
{% endif %}

{% if target_audience %}
Target Audience
: {{ target_audience }}
{% endif %}

{% if online_audience_reached %}
Online Audience Reached
: {{ online_audience_reached }}
{% endif %}

{% if does_the_project_have_a_twitter_account %}
Twitter
: {{ does_the_project_have_a_twitter_account }} {% if twitter_followers %}({{ twitter_followers }} followers){% endif %}
{% endif %}

{% if publishers_twitter_followers_if_needed %}
Publisher's Twitter Followers
: {{ publishers_twitter_followers_if_needed }}
{% endif %}

{% if google_page_rank or alexa_pange_rank %}
Online Rank
: {% if google_page_rank %} Google: {{ google_page_rank }} {% endif %} {% if alexa_pange_rank %} Alexa: {{ alexa_pange_rank }}{% endif %} {% if ose_domain_authority_rank %} OSE Domain Authority Rank: {{ ose_domain_authority_rank }}{% endif %}{% if marketing_grader_rank %} Marketing Grader Rank: {{ marketing_grader_rank }}{% endif %} {% if comments %}({{ comments }}){% endif %}
{% endif %}

{% if newspasperspublishers_page_rank_if_applicable or newspapers__publishers_alexa_page_rank_if_applicable %}
Online Rank (Publisher)
: {% if newspasperspublishers_page_rank_if_applicable %} Google: {{ newspasperspublishers_page_rank_if_applicable }}{% endif %} {% if newspapers__publishers_alexa_page_rank_if_applicable %} Alexa: {{ newspapers__publishers_alexa_page_rank_if_applicable }}{% endif %}
{% endif %}

{% if news_source %}
News Source
: {{ news_source }}
{% endif %}

{% if offline_audience_reached %}
Offline Audience Reached
: {{ offline_audience_reached }}
{% endif %}

{% if outcome %}
Outcome
: {{ outcome }}
{% endif %}

{% if update_date %}
Last updated
: {{ update_date }}
{% endif %}

{% if attempts_against_the_project_ or attempts_against_the_project_2 %}
Attempts
: {{ attempts_against_the_project_ }} {% if attempts_against_the_project_2 %} / {{ attempts_against_the_project_2 }}{% endif %}
{% endif %}

## Technology

Code Repository
: [{{ code_url }}]({{ code_url }}){% endif %}

{% if tool %}
Tool
: {{ tool }}
{% endif %}

{% if other_tools %}
Other Tools
: {{ other_tools }}
{% endif %}

## Team

{% if team_size %}
Team Size
: {{ team_size }}
{% endif %}


{% if research or data_science or engineering or design %}
Experience
: {% if research %} research {% endif %} {% if data_science %} data_science {% endif %} {% if engineering %} engineering {% endif %} {% if design %} design {% endif %}
{% endif %}

## Project Methodology

{% if project_methodology %}
Project Methodology
: {{ project_methodology }}
{% endif %}

{% if open_source %}
Open Source
: {{ open_source }}
{% endif %}

{% if open_data %}
Open Data
: {{ open_data }}
{% endif %}

{% if budget %}
Budget
: {{ budget }}
{% endif %}

{% if contracting %}
Contracting
: {{ contracting }}
{% endif %}

{% if risk_planning %}
Risk Planning
: {{ risk_planning }}
{% endif %}

{% if sustainability_planning %}
Sustainability Planning
: {{ sustainability_planning }}
{% endif %}

### Documentation

{% if data_modeling %}
Data Modeling
: {{ data_modeling }}
{% endif %}

{% if ethical_collection %}
Ethical Collection
: {{ ethical_collection }}
{% endif %}

{% if ethical_storage %}
Ethical Storage
: {{ ethical_storage }}
{% endif %}

{% if data_collection %}
Data Collection
: {{ data_collection }}
{% endif %}

{% if data_collection2 %}
Data Collection
: {{ data_collection2 }}
{% endif %}

{% if data_verification %}
Data Verification
: {{ data_verification }}
{% endif %}

{% if data_cleaning %}
Data Cleaning
: {{ data_cleaning }}
{% endif %}

{% if data_analysis %}
Data Analysis
: {{ data_analysis }}
{% endif %}

{% if data_description %}
Data Description
: {{ data_description }}
{% endif %}

{% if data_licencing %}
Data Licensing
: {{ data_licencing }}
{% endif %}

{% if ethical_publishing %}
Ethical Publishing
: {{ ethical_publishing }}
{% endif %}

{% if ethical_publishing2 %}
Ethical Publishing
: {{ ethical_publishing2 }}
{% endif %}

{% if data_publishing_mode %}
Data Publishing Mode
: {{ data_publishing_mode }}
{% endif %}

{% if most_recent_update %}
Most Recent Update
: {{ most_recent_update }}
{% endif %}

{% if regularly_updated %}
Regularly Updated
: {{ regularly_updated }}
{% endif %}

