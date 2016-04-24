---
title: Who's Got Dirt API
layout: default
---

<h1 class="page-heading">Who's Got Dirt API</h1>

<div class="row">
  <div class="col-md-8">
    <p>A goal of the IM project is to make it easier for researchers and investigators to aggregate and reconcile data from external sources in order to enrich their own databases and ultimately to reduce the time and effort required to do their work. The project is developing <strong>a data specification to serve as a standard way of representing this data, which various tools can implement to achieve interoperability</strong> &#8211; including importers, exporters, reconciliation services and visualization tools.</p>
    
    <p>For example, Morgan, a researcher in Ghana, is investigating the awarding of oil entitlements in the Jubilee oil field. From the published contracts, Morgan already has the names of the companies having received an award. Morgan uses a reconciliation service to match the companies with those in <a href="http://www.opencorporates.com/" target="_blank">OpenCorporates</a> and then uses an importer to add the companies’ directors from OpenCorporates to her database. Morgan then uses another service to query for any links between company directors and government ministers and imports any matches. Morgan then explores this database using a visualization tool authored by another organization.</p>
    
    <p>Presently, fulfilling this example would require writing custom &#8220;glue&#8221; code at each step, because each service and tool uses a different data interchange format for its inputs and outputs. Switching to a new visualization tool would require reformatting the data to match the tool&#8217;s expectations. Small projects in particular are unlikely to have the resources to perform this integration. The result is duplicated effort or orphaned labor, because the barriers to reuse of others&#8217; work is too great.</p>
    
    <p>If, on the other hand, each component of this workflow were to use a standard way of representing data, it would be easier to join the components together and to substitute one component for an alternative.</p>
    
    <h3>The work so far</h3>
    
    <p>As a real use case for the standards development process, an API is being developed, called <strong>&#8220;Who&#8217;s got dirt?&#8221; (WGD).</strong> The API will behave as a single point of access to multiple APIs and databases of influence data, allowing a user to query for entities, relations and lists. The WGD API will have a single request format and single response format for all the APIs and databases it connects to. Through the process of transforming the various API-specific request and response formats into one common format, a draft specification will emerge, upon which further standardization efforts can be pursued by consensus with the broader community.</p>
  </div>
  <div class="col-md-4">
    <h3>Resources</h3>
    <ul>
      <li><a href="http://influencemapping.github.io/whos_got_dirt-demo/">Demo Tool</a></li>
      <li><a href="https://influencemapping.github.io/whos_got_dirt-server/">API Documentation</a></li>
      <li><a href="https://github.com/influencemapping/whos_got_dirt-gem" target="_blank">whos_got_dirt-gem</a></li>
      <li><a href="https://github.com/influencemapping/whos_got_dirt-server" target="_blank">whos_got_dirt-server</a></li>
      <li><a href="https://github.com/influencemapping/whos_got_dirt-demo" target="_blank">whos_got_dirt-demo</a></li>
    </ul>
  </div>
</div>

