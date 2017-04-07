---
title: "Scale, Modeling, Contributions: Lessons from OpenCorporates"
layout: london
---

_[OpenCorporates](https://opencorporates.com/) has grown to include 90mio companies, some collected via the Turbot crowd-sourcing mechanism. Chris will share some lessons. Presented by Chris Taggart._

_**API**: http://api.opencorporates.com/_
_**All company registers**: https://opencorporates.com/registers_

***

OC has just hit 90 millions companies. It started with 3 million companies 4 years ago. Right now, it's got several more jurisdictions (totalling several million more companies) going through our data quality checks at the moment, and think there’s an outside chance we may reach 100 million by the end of this year.

Focused on companies, organizations that the law treat as persons. Deal with the reality of the companies identities. It recently introduced [advanced search](http://influencemapping.org/opencorporates-introduces-advanced-search/) in the website.

### Sustainability
It works as a sustainability model because of the different publics that use OpenCorporates data. On the first hand, it’s widely used for journalists, anti-corruption investigators but also for law enforcement, banks, Governments and tax offices.

(From the [2014 Impact Report](http://blog.opencorporates.com/2015/05/26/opencorporates-impact-report-2014/): “(On 2014) our roster of clients expanded considerably to include such well-known organisations as LinkedIn, the World Bank, Creditsafe, Bureau van Dijk, Avention (One-Source) and many more. We also found out that banks, global law firms and accountants were routinely using OpenCorporates in investigations, due diligence work and onboarding of clients”.

### Modeling
We’ve been really crappy in UI and usability. We noticed that we were deploying a lot of useful stuff but nothing the user could see, so we started doing 2 or 3 weekly hours meeting where we fixed visible problems for people. 

### Scalability
Big difficulty around this. How do we OCR those other companies documents?
And we have this 90 million records. How do you search everything? Looking for leads, good quality leads. 
As for including more and more information, we have Turbot, a pipeline, shared with Open Data Institute. OC is not Open Source, we are worrying to make the data open, so that OC can be used as a source use OC. And we never pay for data. We only have what’s available publicly.

***

### More on [Turbot](http://turbot.opencorporates.com)
Turbot is a tool that allows members of the open data community to write bots to harvest publicly-available corporate data, so that that data can be imported into the OpenCorporates database and made available as open data.

**The Turbot workflow**
To write a bot and then to end up with the scraped data in the OpenCorporates database, you'll have to go through the following steps:

* Install the Turbot command line tool.
* Identify a data source: There's a list of data sets on our Missions page, and you can claim a mission there. Alternatively, if you have found a data source that you'd like to scrape, check that it meets our requirements for the kinds of data we scrape.
* Write a bot: At the moment, you can write a bot in Ruby or Python.
* Write a transformer for your data: In order for your scraped data to appear on pages on the OpenCorporates website, it needs to be transformed into a structure that the website can understand. This can be done easily by writing a transformer that takes the output of your bot and transforms each record.
* Submit your bot for review.
* Sit back and wait for your data to appear in OpenCorporates.
