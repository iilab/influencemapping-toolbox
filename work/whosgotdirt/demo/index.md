---
title: Who's Got Dirt API Demo
layout: default
---

<h1>Search for entities across 5 influence data APIs</h1>

<p>This is a demonstration of the <a href="https://influencemapping.github.io/whos_got_dirt-server/"><i>Who's got dirt?</i> API</a>. The <i>Who's got dirt?</i> API provides a single access point to multiple APIs of influence data on the web. It proxies requests to the supported APIs, so that users only need to learn a single request format and a single response format. <a href="https://influencemapping.github.io/whos_got_dirt-server/">Read the documentation</a> to learn more about the API and how you can use it in your own projects.</p>

<p>This demo queries only <strong>entities</strong> (people and organizations) and exposes only 5 filters for entities, not all 25 implemented by the <i>Who's got dirt?</i> API and its supported APIs. In addition to entities, the <i>Who's got dirt?</i> API supports <strong>relations</strong> between entities (for example, a person holding an office in an organization) and <strong>lists</strong> of entities (for example, a corporate grouping).</p>

<form action="https://whosgotdirt-proxy.herokuapp.com/entities.csv" method="post" id="form">
  <h2>Select your filters to search for entities</h2>

  <div id="filters">
  </div>

  <div class="form-group">
    <button type="button" class="btn btn-default" id="add">
      <span class="glyphicon glyphicon-plus" aria-hidden="true"></span> Add another filter
    </button>
  </div>

  <input type="hidden" name="page" value="1">

  <h2>Select the APIs to query</h2>

  <div class="form-group">
    <div class="row">
      <div class="col-sm-3 col-lg-2">
        <div class="checkbox">
          <label>
            <input type="checkbox" name="endpoints" checked="checked" value="CorpWatch">
            <span data-toggle="tooltip" title="800,000+ companies in 200+ countries">
              CorpWatch
            </span>
          </label>
        </div>
      </div>

      <div class="col-sm-3 col-lg-2">
        <div class="checkbox">
          <label>
            <input type="checkbox" name="endpoints" checked="checked" value="OpenCorporates">
            <span data-toggle="tooltip" title="90,000,000+ companies, 120,000,000+ officers and 800+ corporate groupings in 50+ countries">
              OpenCorporates
            </span>
          </label>
        </div>
      </div>

      <div class="col-sm-3 col-lg-2">
        <div class="checkbox">
          <label>
            <input type="checkbox" name="endpoints" value="LittleSis">
            <span data-toggle="tooltip" title="200,000+ entities and 700+ lists in the United States">
              LittleSis
            </span>
            <span data-toggle="tooltip" title="API key required">
              <a href="https://api.littlesis.org/register"><span class="glyphicon glyphicon-lock" aria-hidden="true" aria-label="Register for an API key"></span></a>
            </span>
          </label>
        </div>
      </div>

      <div class="col-sm-3 col-lg-2">
        <div class="checkbox">
          <label>
            <input type="checkbox" name="endpoints" value="OpenDuka">
            <span data-toggle="tooltip" title="40,000+ entities in Kenya">
              OpenDuka
            </span>
            <span data-toggle="tooltip" title="API key required">
              <a href="http://www.openduka.org/index.php/api"><span class="glyphicon glyphicon-lock" aria-hidden="true" aria-label="Register for an API key"></span></a>
            </span>
          </label>
        </div>
      </div>

      <div class="col-sm-3 col-lg-2">
        <div class="checkbox">
          <label>
            <input type="checkbox" name="endpoints" value="Poderopedia">
            <span data-toggle="tooltip" title="Entities in Chile">
              Poderopedia
            </span>
            <span data-toggle="tooltip" title="API key required">
              <a href="https://poderopedia.3scale.net/login"><span class="glyphicon glyphicon-lock" aria-hidden="true" aria-label="Register for an API key"></span></a>
            </span>
          </label>
        </div>
      </div>
    </div>
  </div>

  <input type="hidden" name="queries" id="queries">
  <button type="button" class="btn btn-default" id="submit">Submit query</button>
  <button type="submit" class="btn">Download CSV</button>
  <span id="loading"></span>
</form>

<div id="messages">
</div>

<div class="panel panel-default" id="results">
  <div class="panel-heading"><span id="number"></span> of <span id="count"></span> results</div>
  <div class="panel-body">
    <table class="table table-bordered table-striped">
      <thead>
        <tr>
          <th>Name</th>
          <th>Country</th>
          <th>Classification</th>
          <th>Founding date</th>
          <th>Address</th>
          <th>Source</th>
          <th>JSON</th>
        </tr>
      </thead>
      <tbody>
      </tbody>
    </table>

    <p>
      <a href="#" class="btn btn-default" rel="prev" id="page-previous">Previous</a>
      <a href="#" class="btn btn-default" rel="next" id="page-next">Next</a>
    </p>
  </div>
</div>

<div id="modals">
</div>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js" integrity="sha512-K1qjQ+NcF2TYO/eI3M6v8EiNYZfA95pQumfvcVrTHtwQVDG+aHRqLi/ETn2uB+1JqwYqVG3LIvdm9lj6imS/pQ==" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.4.1/js/bootstrap-datepicker.min.js"></script>
<script src="https://influencemapping.github.io/whos_got_dirt-demo/build/build.js"></script>
