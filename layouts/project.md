# {{ name }}

{% if notes != "" %}<div class="alert alert-success" role="alert">{{ notes }}</div>{% endif %}

Logo
:   {% if image != "N/A" %}![]({{ image }}){% endif %}

{{ description }}

URL
:   {{ url }}


Keywords
:   {{ keywords }}



Project Current Phase
:   {{ phase }}

    

Project Start Date
:   {{ project_start_date }}



Launch Date
:   {{ launch_date }}



Most Recent Update
:   {{ most_recent_update }}



Update Frequency
:   {{ regularly_updated }}



Thematic Focus
:   {{ thematic_focus }}



Issue addressed
:   {{ issue_addressed }}



Geographic Focus
:   {{ geographic_focus }}


### Experience

_How does a user interact with and navigate the project?_

Narrative
:   {{ narrative }} 

Query
:   {{ query }} 

Geographic Map
:   {{ geographic_map }}  

Timelines
:   {{ timelines }} 

Lists
:   {{ lists }} 

Network Visualisation
:   {{ network_viz }}

Other Visualisation
:   {{ other__viz }}

Raw Data 
:   {{ export }}

## Description

_Summary of the project and its approach_

__{{ description2 }}__


Rationale (Why?)
:   {{ rationale_why }}



Approach (How?)
:   {{ approach_how }}



Language
:   {{ language }}



Commissioner
:   {{ commissioner }}



Publisher
:   {{ publisher }} ({{ publisher_country }})



Partners
:   {{ partners }}


## Impact

_Indicators of reach and impact of the project_

Intended Impact
:   {{ intended_impact }}



Target Audience
:   {{ target_audience }}



Online Audience Reached
:   {{ online_audience_reached }}



Twitter
:   {{ does_the_project_have_a_twitter_account }} ({{ twitter_followers }} followers)



Publisher's Twitter Followers
:   {{ publishers_twitter_followers_if_needed }}



Online Rank
:    Google:   {{ google_page_rank }}   Alexa:   {{ alexa_pange_rank }}  OSE Domain Authority Rank:   {{ ose_domain_authority_rank }} Marketing Grader Rank:   {{ marketing_grader_rank }} ({{ comments }})


Online Rank (Publisher)
:    Google:   {{ newspasperspublishers_page_rank_if_applicable }}  Alexa:   {{ newspapers__publishers_alexa_page_rank_if_applicable }}



News Source
:   {{ news_source }}



Offline Audience Reached
:   {{ offline_audience_reached }}



Outcome
:   {{ outcome }}



Last updated
:   {{ update_date }}


Attempts against the project
:   {{ attempts_against_the_project_ }}  / {{ attempts_against_the_project_2 }}


## Technology

_What tools and code were used to create the project?_

Tech Best Practices:
:    {{ tech_best_practice_1 }}
:    {{ tech_best_practice_2 }} 
:    {{ tech_best_practice_3 }}

Code Repository
:   [{{ code_url }}]({{ code_url }})
:   [{{ code_url_2 }}]({{ code_url_2 }})

Tool
:   {{ tool }}
:   {{ tool2 }}
:   {{ tool3 }}
:   {{ other_tools }}

Database
:   {{ db }}
:   {{ other_db }}

Frontend
:   {{ frontend }}
:   {{ frontend2 }}
:   {{ frontend3 }}
:   {{ frontend_language }}
:   {{ frontend_language_2 }}

Backend
:   {{ backend }}
:   {{ backend2 }}
:   {{ backend3 }}
:   {{ backend_language }}
:   {{ backend_language_2 }}

Data Format
:   {{ data_format}}
:   {{ data_format_2}}

Data Standard
:   {{ data_format}}

Technical Documentation URL
:   {{ technical_documentation_url }}
:   {{ technical_documentation_url_2 }}

Technical Architecture Documentation
:   {{ technical_architecture_documentation}}

Schema Documentation
:   {{ schema_documentation}}

Design Documentation
:   {{ design_documentation}}

API Documentation
:   {{ api_documentation}}


## Data Sources

Data Sources
:   {{ data_source_1}}
:   {{ data_source_2}}
:   {{ data_source_3}}
:   {{ data_source_4}}
:   {{ data_source_5}}
:   {{ data_source_6}}

## Team

_Team size and expertise_

Team Size
:   {{ team_size }}



Team Experience
:    

Research
:   {{ research }} 

Data Science
:   {{ data_science }} 

Engineering
:    {{ engineering }}

Design
:   {{ design }}


## Project Methodology

_What strategies were in place for managing the project? _

Project Methodology
:   {{ project_methodology }}



Open Source
:   {{ open_source }}



Open Data
:   {{ open_data }}



Budget
:   {{ budget }}


Contracting
:   {{ contracting }}



Risk Planning
:   {{ risk_planning }}



Sustainability Planning
:   {{ sustainability_planning }}


## Documented Practices

_Documentation about project practices_

{{ practice1 }} {% if subpractice1 %} / {{ subpractice1 }} {% endif %}
{% if practice1url %} :   [{{practice1url}}]({{practice1url}}) {% endif %} 

{{ practice2 }} {% if subpractice2 %} / {{ subpractice2 }} {% endif %}
{% if practice2url %} :   [{{ practice2url }}]({{practice2url}}) {% endif %}

{{ practice3 }} {% if subpractice3 %} / {{ subpractice3 }} {% endif %}
{% if practice3url %} :   [{{ practice3url }}]({{practice3url}}) {% endif %}


## Practices

_How projects handle different aspects of data management_


Data Modeling
:   {{ data_modeling }}



Ethical Collection
:   {{ ethical_collection }}



Ethical Storage
:   {{ ethical_storage }}



Data Collection
:   {{ data_collection }}



Data Collection
:   {{ data_collection2 }}



Data Verification
:   {{ data_verification }}



Data Cleaning
:   {{ data_cleaning }}



Data Analysis
:   {{ data_analysis }}



Data Description
:   {{ data_description }}



Data Licensing
:   {{ data_licencing }}



Ethical Publishing
:   {{ ethical_publishing }}



Ethical Publishing
:   {{ ethical_publishing2 }}



Data Publishing Mode
:   {{ data_publishing_mode }}
