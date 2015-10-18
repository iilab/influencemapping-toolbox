---
layout: boxed
title: A standard for influence data
description: 
home: true
---

## A standard for influence data

A goal of the project is to make it easier for researchers and investigators to aggregate and reconcile data from external sources in order to enrich their own databases and ultimately to reduce the time and effort required to do their work. The project is developing a data specification to serve as a standard way of representing this data, which various tools can implement to achieve interoperability - including importers, exporters, reconciliation services and visualization tools.

For example, Morgan, a researcher in Ghana, is investigating the awarding of oil entitlements in the Jubilee oil field. From the published contracts, Morgan already has the names of the companies having received an award. Morgan uses a reconciliation service to match the companies with those in [OpenCorporates](http://www.opencorporates.com/) and then uses an importer to add the companies' directors from OpenCorporates to her database. Morgan then uses another service to query for any links between company directors and government ministers and imports any matches. Morgan then explores this database using a visualization tool authored by another organization.

Presently, fulfilling this example would require writing custom "glue" code at each step, because each service and tool uses a different data interchange format for its inputs and outputs. Switching to a new visualization tool would require reformatting the data to match the tool's expectations. Small projects in particular are unlikely to have the resources to perform this integration. The result is duplicated effort or orphaned labor, because the barriers to reuse of others' work is too great.

If, on the other hand, each component of this workflow were to use a standard way of representing data, it would be easier to join the components together and to substitute one component for an alternative.

## The work so far

As a real use case for the standards development process, an API is being developed, called "Who's got dirt?" (WGD). The API will behave as a single point of access to multiple APIs and databases of influence data, allowing a user to query for entities, relations and lists. The WGD API will have a single request format and single response format for all the APIs and databases it connects to. Through the process of transforming the various API-specific request and response formats into one common format, a draft specification will emerge, upon which further standardization efforts can be pursued by consensus with the broader community.

Watch for updates on these [InfluenceMapping GitHub repositories](https://github.com/influencemapping):

* [whos_got_dirt-gem](https://github.com/influencemapping/whos_got_dirt-gem)
* [whos_got_dirt-server](https://github.com/influencemapping/whos_got_dirt-server/)
* [whos_got_dirt-demo](https://github.com/influencemapping/whos_got_dirt-demo/)

Prior to developing the WGD API, the terms used by several APIs for influence data were [inventoried](https://drive.google.com/open?id=1on99aF9QVWOwqZDtla9RLX5Wza6MHxbb4apZwbtHK-w).
