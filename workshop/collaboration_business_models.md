---
title: Collaboration and Business Models
layout: london
---

_Presented by Jonathan Stray, Overview._

_See [full presentation](https://youtu.be/UwCggnStdEQ)._

## Collaboration possibilities

* **One codebase to rule them all**: Either we choose one or we make a new one and everyone contributes. If we choose one, which one? We could even patch together different codebases.
* **Modules owned by different teams**: Modules as for visualizations, entity DB, file store and file ingest. It would be nice if there was an API that you could write to that would plug into an existing system rather than custom stuff that we have now.
The problem in this is that somebody still has to own certain key single points. For example, usability and workflows: Who is the systems integrator? Who owns the UI? Who supports this?
* **Interoperability APIs/formats**:  Everyone continues to work on their own platform and we have APIs to talk to each other. 
In this world we don’t get to centralize development resources, but at least they can talk to each other.
We do need an integrated system.

### More specific:

**Modules (Build)**

* Workspaces: Integrated UI that is seamless and usable
* File repository: store, manage, version millions of documents/databases
* Importers: Extract, scraper, OCR, process attachments, lots of formats
* Visualizations: specialized analysis tools

**Existing API’s and formats**

* Overview plugin API: Rapid visulization / custom workflow  development
* Whos got dirt: Federated search
* OpenCorporates: Global company identifiers

## Business Models: How do we fund any of these?

* **Grants forever**: Not a sustainable plan. It has a lot of throwbacks.
* **Commercial SAAS (Software as a service) for journalists**: The main issue is that the market size is a problem, specially for this deep investigative journalism world. You only have a few thousands of people and you have to capture them. It’s better if you can reach a broader audience, not only journalists.
* **Commercial SAAS for Legal / Business**: You don’t get journalists to pay. The technologies that we are building would be useful for other markets, such as the legal market. Most of the tools that journalists use were not made for journalists. More possibilities to get capital funding. 
* **Private access**: Sell content, not software. Media to pay for access to information they need for their stories (ICIJ).

**Suggestions for interoperability**

* Support local installs of ID, DocumentCloud
* Implement the APIs that we are already talking about (Who’s got dirt in ID, DocumentCloud, Overview

Make federation a reality

* Implement Overview API in DocumentCloud, ID

Bring analysis tools to large users bases
