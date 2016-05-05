### [Practices](../../practices.html) > [Organising Data](../../practices.html#organise) > Model Data 

_How to choose a model to organise your data_

____

### What is data modelling? 

Data modelling is about how you structure your database. A simple example would be deciding which columns you would use in a spreadsheet, the different sheets and how you link between them. Below we discuss data modelling in more depth, but a word of warning - data modelling is a complicated field and if you have no prior experience it’s a good idea to talk to an expert before embarking on data modelling yourself.

### Why model your data?

Your model is the structure through which you can ask what relations there are between different aspects of the data. It requires choice over how you categorise the data - into what buckets you decide to put data with certain characteristics, and how you allow those categories to relate to each other. What you can find out about your data set depends on how you group together certain elements of the data. Making the right choice at the beginning will save you a lot of work in the long run.

### How to do it

With your model you want to create a structure that reflects the real life system that the data is about. Organising your data goes hand in hand with data collection. If the “rules” of the model don’t accommodate the data you’re collecting, it can require you to “break” your model, or to start over. Say you’re studying a corporate structure, and you create a data model that lists an individual’s name against their job title.  If your data model is set up to  reference only one job for a particular person, when you come to Anthony Hu who is the Events Coordinator and Accounts Assistant, you won&#39;t be able to capture this without &quot;breaking&quot; your data model - you might create duplicate rows which would lead to duplicate Anthonys. Building on this example, if you wanted to also consider the dates between which someone held a job, you should structure your data model to make this data accessible. In that case you could add a separate sheet to hold the job&#39;s data and the start and end dates. You would also want to add an identifier for each job that links it to the person in your other sheet. 

### Choosing the right type of model for you

This process is the basis of most data modeling, and specifically relational databases. Relational databases are very common, but relational data models can be tricky to modify. There are other types of data modeling techniques that are best for different cases, such as document databases - which are more flexible - and graph databases - which are suited to particular types of queries. 

One key decision for an influence mapping project is how relationship between people and organisations or other type groups are modeled. For a large majority of cases, a simple relational model will be sufficient. Graph data models and databases are more rarely needed, for specific types of queries such as discovering paths in relations or calculating a social graphs&#39; mathematical characteristics - such as centrality or betweenness. There is an extra cost and effort related to using these types of structures because experts are harder to find and the tools are less mature.

Perhaps the most sophisticated and difficult type of data models you can use are based on the semantic web approach. It allows to describe data in a lot of detail and with a lot of flexibility which can be useful to describe complex systems. Using such data models in practice is however cumbersome and only well resourced projects with semantic web experts should attempt to go this route.

Data models should be only as sophisticated as they need to be to answer your project’s questions. It can be tempting to try to capture everything with your data model, but over-engineering your data model will affect how practicable your project is. Adding too many variables and types of entities and relations can result in making the data collection and clean up process much longer, as well as make the development of queries and applications more challenging.

### How responsive do you need your queries to be?

Database query times can vary from almost instantaneous to several days, so it’s important to consider performance as part of your project plan. If you’re hoping to make an interactive interface to your data that others will use, for instance, then your queries need to happen without a time lag for it to be useable.

Performance can be affected by your choice of database type will as will the details of your data model. Your choice of data model will also influence whether or not the data and the queries can be distributed on a large number of computers in order to make the queries faster. As performance is controlled by multiple factors you might want to consider discussing this with a data modelling expert before making your choice. 

The data you collect and how you’re going to use your database also impacts on performance. Different query types vary in the time needed to return results. You might want to look up a particular data point (&quot;Who was system administrator of this organisation between 2012 and 2014?&quot;), do a text search (&quot;Find all jobs with &#39;Administrator&#39; in the title&quot;) or carry out  numerical analysis (&quot;What is the average length of time that a system administrator will stay at her job?&quot;). Similarly, if you&#39;re looking at only one company with hundreds of employees it will be quicker than an equivalent search through a data set for an entire country with historical data for tens of years 

You can find information about data modelling practices here:

- [Exposing the Invisible Decoding Data Guide has a great chapter on structuring data](https://exposingtheinvisible.org/guides/decoding-data/#structuringdata)  
- The [Global Investigative Journalism Network](http://gijn.org/resources/investigative-journalism-manuals/#dataj) has a good list of data journalism guides 
- Agile Data’s Data Modeling 101 http://www.agiledata.org/essays/dataModeling101.html This rather technical guide is focussed specifically on data modeling in an agile methodology for app development, but provides a good run-down of data modeling intricacies

</div></div><!-- dirty trick. close parent container and row--> 









































































































































<div class="container">
<div class="row">
<br>
<h3>Relevant projects <small>Consult project documentation about this practice</small></h3>
</div>
</div>

<div class="container-fluid">
<div class="row">
<div class="carousel">








<div>
<div class="panel panel-primary">
<div class="panel-heading">
<h4 class="panel-title">Influence Explorer</h4>
</div>
<div class="panel-body">
<p><small>Influence Explorer lets you browse those who have contributed to US campaign finances</small></p>
<a href="../../projects/influence-explorer.html#documented-practices">Read More</a>
</div>
</div>
</div>











<div>
<div class="panel panel-primary">
<div class="panel-heading">
<h4 class="panel-title">Follow The Money </h4>
</div>
<div class="panel-body">
<p><small>Follow The Money is a free and verified archive of contributions to political campaigns in the US</small></p>
<a href="../../projects/follow-the-money.html#documented-practices">Read More</a>
</div>
</div>
</div>





<div>
<div class="panel panel-primary">
<div class="panel-heading">
<h4 class="panel-title">No Ceilings
</h4>
</div>
<div class="panel-body">
<p><small>No Ceilings compiles and visualises data on indicators of the participation of girls and women in everyday life </small></p>
<a href="../../projects/no-ceilings.html#documented-practices">Read More</a>
</div>
</div>
</div>



























<div>
<div class="panel panel-primary">
<div class="panel-heading">
<h4 class="panel-title">Dollars for Docs</h4>
</div>
<div class="panel-body">
<p><small>Dollars for Docs shows details of financial payments from pharmaceutical companies to doctors in the US</small></p>
<a href="../../projects/dollars-for-docs.html#documented-practices">Read More</a>
</div>
</div>
</div>























































<div>
<div class="panel panel-primary">
<div class="panel-heading">
<h4 class="panel-title">Corpwatch Croctail</h4>
</div>
<div class="panel-body">
<p><small>CrocTail provides an interface for browsing information about several hundred thousand U.S. publicly traded corporations and their foreign...</small></p>
<a href="../../projects/corpwatch-croctail.html#documented-practices">Read More</a>
</div>
</div>
</div>
























</div>
<br>
</div>
</div>



























































































































































































































<div class="container"><!-- dirty trick. reopen parent container -->
<div class="row">
<span class="pull-left"><h3>Relevant tools <small>Tools that can be of use to apply this practice</small></h3></span>
<span class="pull-right project-filter">
<div class="btn-group" data-toggle="buttons">
<label class="btn btn-primary glyphicon glyphicon-user active" data-toggle="tooltip" data-placement="top" title="User"><input type="checkbox" autocomplete="off" checked></label><label class="btn btn-primary glyphicon glyphicon-education active" data-toggle="tooltip" data-placement="top" title="Data User"><input type="checkbox" autocomplete="off" checked></label><label class="btn btn-primary glyphicon glyphicon-wrench active" data-toggle="tooltip" data-placement="top" title="Developer"><input type="checkbox" autocomplete="off" checked></label>
</div>
</span>
</div>
</div>

<div class="container-fluid">
<div class="row">
<br>
<div class="carousel">


<div>
<div class="panel panel-primary" data-toolbox-user="">
<div class="panel-heading">
<h4 class="panel-title">PoderVocab</h4>
</div>
<div class="panel-body">
<p><small>Ontology for Poderopedia</small></p>
<a href="../../tools/podervocab.html">Read More</a>
</div>
</div>
</div>



<div>
<div class="panel panel-primary" data-toolbox-user="">
<div class="panel-heading">
<h4 class="panel-title">Popolo</h4>
</div>
<div class="panel-body">
<p><small>Data standard for people, organisations, roles</small></p>
<a href="../../tools/popolo.html">Read More</a>
</div>
</div>
</div>



<div>
<div class="panel panel-primary" data-toolbox-user="">
<div class="panel-heading">
<h4 class="panel-title">tx_people</h4>
</div>
<div class="panel-body">
<p><small>Django app with Popolo support</small></p>
<a href="../../tools/tx_people.html">Read More</a>
</div>
</div>
</div>



























































































































































<div>
<div class="panel panel-primary" data-toolbox-user="">
<div class="panel-heading">
<h4 class="panel-title">http://www.umbel.org</h4>
</div>
<div class="panel-body">
<p><small></small></p>
<a href="../../tools/httpwwwumbelorg.html">Read More</a>
</div>
</div>
</div>


















































</div>
</div>
</div>
<div class="container"><!-- dirty trick. reopen parent container -->
<div class="row">
</div><!--- group row -->
</div><!--- group container -->
<div class="container"><div class="row"><!-- dirty trick. reopen parent container and row -->