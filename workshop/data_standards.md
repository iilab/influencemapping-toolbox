---
title: "Session: 'Data Standards + Who's Got Dirt? API' (James McKinney)"
layout: london
---

_Looking at the possibilities for standard to increase data interoperability between our datasets and tools, including the idea of a common API for investigative entity mapping tools: "Who's Got Dirt?" API. Presented by James McKinney._

***

### Frame of the presentation

**Collaboration models**: How the people work together

**Interoperability APIs and formats**: How the software works together

**Workflow definitions**: What should the software do

* There are a lot of different databases out there and the usual way to know if there’s data matching your query is finally made by e-mail

API’s
* First we work with what we have:LittleSis, OpenCorporates, OpenOil, Poderopedia, Quién Manda, Open Duka, CrocTail, Grano, etc.
* The first problem around this is that you have to work around distributed queries
* End up looking at databases that might help
* So you have a big issue around discoverability: finding the information you _need_ 

### **So, the current common process is:**
1. Consult the list of websites / APIs
1. Visit each website / API
1. read each website's documentation
1. / read each API reference
1. perform searches on each website
1. / send requests to each API
1. Read the data and interpret its schema
1. (whether it’s CSV, JSON, XML, HTML)

### **The proposed process is:**
1. Consult one website / API
1. Visit one website / API
1. read one website's documentation
1. / read one API reference
1. perform searches on one website
1. / send requests to one API
1. Read the data and interpret its schema
1. (learn only one response format)

_(Shows Demo)_

### **One request format**
**`GET /entities?queries=<queries>`**

```
{
  "q0": {
    "query": {
      "type": "Entity",
      "name~=": "John Smith",
      "jurisdiction_code|=": ["gb", "ie"],
      "memberships": [{
        "role": "director",
        "inactive": false
      }]
    }
  }
}
```

### **One request format, one response format**
* Metaweb Query Language (MQL) from Freebase
* OpenRefine Reconciliation Service API
* Popolo terms for field names

### **Endpoints**
* /entities
* /relations
* /lists

### Implementation
* A library that accepts MQL parameters and returns the URL to send to each API

```
require 'whos_got_dirt'
require 'faraday'

input = {
  'name~=' => 'John Smith',
  'jurisdiction_code|=' => ['gb', 'ie'],
  'memberships' => [{
    'role' => 'director',
    'inactive' => false,
  }],
}

url = WhosGotDirt::Requests::Person::OpenCorporates.new(input).to_s
#=> "https://api.opencorporates.com/officers/search?q=John+Smith&position=director&inactive=false&jurisdiction_code=gb%7Cie&order=score"
```

* A library that accepts an API response and returns results in Popolo format

```
response = Faraday.get(url)

results = WhosGotDirt::Responses::Person::OpenCorporates.new(response).to_a
#=> [{"@type"=>"Person",
#  "name"=>"JOHN SMITH",
#  "updated_at"=>"2014-10-25T00:34:16+00:00",
#  "identifiers"=>[{"identifier"=>"46065070", "scheme"=>"OpenCorporates"}],
#  "links"=>[{"url"=>"https://opencorporates.com/officers/46065070", "note"=>"…"}],
#  "memberships"=>
#   [{"role"=>"director",
#     "organization"=>
#      {"name"=>"EVOLUTION (GB) LIMITED",
#       "identifiers"=>[{"identifier"=>"05997209", "scheme"=>"Company Registry"}],
#       "links"=>[{"url"=>"https://opencorporates.com/companies/gb/05997209", "note"=>"…"}],
#       "jurisdiction_code"=>"gb"}}],
#  "current_status"=>"CURRENT",
#  "jurisdiction_code"=>"gb",
#  "occupation"=>"MANAGER",
#  "sources"=>
#   [{"url"=>"https://api.opencorporates.com/officers/search?inactive=false&jurisdiction_code=gb%7Cie&order=score&position=director&q=John+Smith", “note"=>"OpenCorporates"}]}]
```

* A server that handles all the ugly parts (error handling, request queueing, response caching, etc.)

### Project scope
* At least two APIs must agree on something for it to even be a candidate for inclusion

### Roadmap
* Add /relations and /lists endpoints 
* Support more APIs
* Update Popolo

### Issue trackers
* [https://github.com/influencemapping/whos_got_dirt-gem/](https://github.com/influencemapping/whos_got_dirt-gem/)
* [https://github.com/influencemapping/whos_got_dirt-server/](https://github.com/influencemapping/whos_got_dirt-server/)
