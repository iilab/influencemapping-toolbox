---
title: "Demos: Solutions for Document Management - DocumentCloud"
layout: london
---

_Part of "Demos: Solutions for Document Management" (10 minute presentations of existing document platforms). Presented by Mar Cabra and Matthew Cuarua._

--

**ICIJ - Media organization that produces cross board investigative stories**
+Network of Investigative Journalists, a network of trust, +190 journalists in more than 65 countries.
50% of the team is the data + research unit. Working not only data analysis for our projects but also tools to help journalists.

Some examples of ICIJ's work:
Secrecy for sale / Offshore leaks: 260 GB, 100.000 offshore COMP.
Luxembourg Leaks: +500 secret tax agreements (PDF’s)
Swiss leaks: 100k HSBC clients, $100 billion

Work in collaboration with media & journalists from the beginning: this is key for us. They are not publishing partners, we work together for 6 to 8 months. 

## Technologies
**1) For unstructured data**
raw files (data + metadata)
     detect the type (file, attachment)
          do we know how to extract the text?
               if we don’t know, log and tackle later	
                    if we do, extract, OCR repeat

3 million x 3 seconds per file = 1 year, running in a single machine.

Through Solr+Blacklight, we managed to reduce what took us 1 year / 35 machines —> to 11 days! YOHOO

As a front-end for Solr we have a project called Blacklight, it’s Ruby on Rails, developed initially for libraries use, that plugs in directly to Solr. Works extremely well. It’s Open Source, heavy development around it, added a lot of features that journalists use. 
Some useful features are Lucene syntax queries with proximity matching and highlighted search.
200 people are using this system in a specific project, going on right now
Limit results / data update, path, year created or sent, type

**2) For us it’s about content, it’s about publishing stories, making the big splash. We work with a Social Network platform. Kind of a Facebook for Investigative Journalists **(name?).** A platform for making the journalists post their investigations, share links, files, and be updated on what happens.

It’s where most of discussions about feature development happen.

**3) Other tools**

* **Linkurious for graph analysis. ** What Linkurious has allowed us is put the data in Neo4j, plug it in the platform and have a graph database for journalists. 
Something important that it for journalists is that it let’s you do a fast analysis and “My notes”. Here’s where structured data comes together.

### Summary of our stack, the tech that we are using:

**Unstructured data extraction**
* ICIJ Extract, open source, Java: https://github.com/ICIJ/extract), leverages Apache Tika +. Much more advances than the Tika and bundles other libraries.

**Structured data extraction**
* A bunch of Python

**Database**
Apache Solr (Open source, Java)
Redis (Open source, C)
Neo4j (Open source, Java)

**Front end app**
Blacklight (Open source, Rails)
Linkurious (Closed source, JS)

***

### The next steps:
* Entity extraction
* Making our data silos talk (Big issue).

### Our current challenge (global data sharing):

Work with knowledge that our journalists have on document managing.
We did a survey, when we asked them about what kind of data they had: Word and documents.

We are trying to develop a platform idea that would connect different investigations + using the data they’ve already collected:

**Offshore laks <-> Bank accounts**
* UK Contractors
* Sanctions data / USA (One-way data check)
* Argentinians fraudsters
* Indian politicians

*We are working in a basic simple tool that can allow entity index.
