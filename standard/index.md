---
layout: boxed
title: A standard for influence data
description: 
home: true
---

## A standard for influence mapping data

A major goal of the project is to make it easier for influence mappers to aggregate and reconcile data from external sources in order to enrich their own databases and ultimately to reduce the time and effort required to do their work. The project is developing a data specification to serve as a standard way of representing the data used by influence mappers, which various tools can implement to achieve interoperability - including importers, exporters, reconciliation services and visualization tools.

For example, Morgan, a researcher in Ghana, is investigating the awarding of oil entitlements in the Jubilee oil field. From the published contracts, Morgan already has the names of the companies having received an award. Morgan uses a reconciliation service to match the companies with those in [OpenCorporates](http://www.opencorporates.com/) and then uses an importer to add the companies' directors from OpenCorporates to her database. Morgan then uses another service to query for any links between company directors and government ministers and imports any matches. Morgan then explores this database using a visualization tool authored by another organization.

Presently, fulfilling this example would require writing custom "glue" code at each step, because each service and tool uses a different data interchange format for its inputs and outputs. Switching to a new visualization tool would require reformatting the data to match the tool's expectations. Small projects in particular are unlikely to have the resources to perform this integration. The result is duplicated effort or orphaned labor, as the barriers to reuse of others' work is too great.

If, on the other hand, each component of this workflow were to adopt a standard way of representing data, it would be much easier to join the components together and to substitute one component for an alternative.

The standards development process is just starting and will roughly follow this schedule:

* Ongoing: Identify stakeholders.
* Jan/Feb: Do first round of invitations of stakeholders to the group.
* Jan: Start use cases and requirements document.
* Jan: Start editor’s draft specification document.
* Feb: Complete first **editor’s** draft specification.
* Apr: Complete first version of cases and requirements document.
* May: Complete first **public draft** specification.
* Mar-Apr: Collect and implement feedback from early adopters and testers.
* May-Jul: Collect and implement feedback from stakeholders.
* Jul-Sep: Collect implementations, and collect and implement feedback from stakeholders.

We will add links to documents are the work progresses.
