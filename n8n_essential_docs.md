# n8n Essential Documentation for Builders

This is a curated subset of n8n documentation focused on building workflows and nodes.

## Quick Reference

- **Expressions**: Use `{{ }}` for JavaScript expressions
- **Variables**: `$json` (current node data), `$node['NodeName'].json` (other node data)
- **Code Node**: Write JavaScript or Python in workflows
- **HTTP Request**: Make API calls with built-in auth
- **Webhook**: Create endpoints to trigger workflows

---

## Table of Contents


### General

- [Readme](#readme)

### _Snippets

- [Workflow Values](#workflow-values)
- [Code Node](#code-node)
- [Custom Execution Data Availability](#custom-execution-data-availability)
- [Retry Options](#retry-options)
- [Custom Templates Library](#custom-templates-library)
- [Disable Templates](#disable-templates)
- [Submit Templates](#submit-templates)

### Docs

- [Index](#index)
- [Index](#index)
- [Convenience](#convenience)
- [Current Node Input](#current-node-input)
- [Index](#index)
- [Date Time](#date-time)
- [Http Node Variables](#http-node-variables)
- [Jmespath](#jmespath)
- [Langchain Methods](#langchain-methods)
- [N8N Metadata](#n8n-metadata)
- [Output Other Nodes](#output-other-nodes)
- [Overview](#overview)
- [Code Node](#code-node)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Jmespath](#jmespath)
- [Luxon](#luxon)
- [Expressions](#expressions)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Workflow Templates](#workflow-templates)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Workflow Development](#workflow-development)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Quickstart](#quickstart)
- [Index](#index)
- [Index](#index)
- [Index](#index)
- [Connections](#connections)
- [Index](#index)
- [Nodes](#nodes)
- [Sticky Notes](#sticky-notes)
- [All Executions](#all-executions)
- [Custom Executions Data](#custom-executions-data)
- [Debug](#debug)
- [Index](#index)
- [Manual Partial And Production Executions](#manual-partial-and-production-executions)
- [Single Workflow Executions](#single-workflow-executions)
- [Index](#index)
- [Workflow Id](#workflow-id)

### Docs Site Feature Tests

- [Index](#index)

### Styles

- [Readme](#readme)

---



## Readme {#readme}

*Source: README.md*

![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

##### n8n Docs

This repository hosts the documentation for [n8n](https://n8n.io/), an extendable workflow automation tool which enables you to connect anything to everything. The documentation is live at [docs.n8n.io](https://docs.n8n.io/).


#### Previewing and building the documentation locally

##### Prerequisites

* Python 3.8 or above
* Pip
* n8n recommends using a virtual environment when working with Python, such as [venv](https://docs.python.org/3/tutorial/venv.html).
* Follow the [recommended configuration and auto-complete](https://squidfunk.github.io/mkdocs-material/creating-your-site/#minimal-configuration) guidance for the theme. This will help when working with the `mkdocs.yml` file.
* The repo includes a `.editorconfig` file. Make sure your local editor settings **do not override** these settings. In particular:
	- Don't allow your editor to replace tabs with spaces. This can affect our code samples (which must retain tabs for people building nodes).
	- One tab must be equivalent to four spaces.

##### Steps

#### For members of the n8n GitHub organization:

1. Set up an SSH token and add it to your GitHub account. Refer to [GitHub | About SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh) for guidance.
2. Then run these commands:

	```bash
	git clone --recurse-submodules git@github.com:n8n-io/n8n-docs.git
	cd n8n-docs
 	# Set up virtual environment if using one (steps depend on your system)
 	# Install dependencies
	pip install -r requirements.txt
	pip install _submodules/insiders
	```

#### For external contributors:

Rely on the preview builds on pull requests, or use the free version of Material for MkDocs (most things are the same, some formatting may be missing)

Fork the repository, then:

```
git clone https://github.com/<your-username>/n8n-docs.git
cd n8n-docs
pip install -r requirements.txt
pip install mkdocs-material
```

#### To serve a local preview:

```
mkdocs serve
```

#### Contributing

Please read the [CONTRIBUTING](CONTRIBUTING.md) guide.

You can find [style guidance](https://github.com/n8n-io/n8n-docs/wiki/Styles) in the wiki.


#### Support

If you have problems or questions, head to n8n's forum: https://community.n8n.io


#### License

n8n-docs is [fair-code](https://faircode.io/) licensed under the [**Sustainable Use License**](https://github.com/n8n-io/n8n/blob/master/LICENSE.md).

More information about the license is available in the [License documentation](https://docs.n8n.io/reference/license/).



---



## Workflow Values {#workflow-values}

*Source: _snippets/integrations/builtin/cluster-nodes/langchain-sub-nodes/workflow-values.md*

Set values to pass to the workflow you're calling.

These values appear in the output data of the trigger node in the workflow you call. You can access these values in expressions in the workflow. For example, if you have:

* **Workflow Values** with a **Name** of `myCustomValue`
* A workflow with an Execute Sub-workflow Trigger node as its trigger

The expression to access the value of `myCustomValue` is `{{ $('Execute Sub-workflow Trigger').item.json.myCustomValue }}`.


---



## Code Node {#code-node}

*Source: _snippets/integrations/builtin/core-nodes/code-node.md*

Use the Code node to write custom JavaScript or Python and run it as a step in your workflow.

/// note | Coding in n8n
This page gives usage information about the Code node. For more guidance on coding in n8n, refer to the [Code](/code/index.md) section. It includes:

* Reference documentation on [Built-in methods and variables](/code/builtin/overview.md)
* Guidance on [Handling dates](/code/cookbook/luxon.md) and [Querying JSON](/code/cookbook/jmespath.md)
* A growing collection of examples in the [Cookbook](/code/cookbook/code-node/index.md)
///

/// note | Examples and templates
For usage examples and templates to help you get started, refer to n8n's [Code integrations](https://n8n.io/integrations/code/){:target=_blank .external-link} page.
///

/// note | Function and Function Item nodes
The Code node replaces the Function and Function Item nodes from version 0.198.0. If you're using an older version of n8n, you can still view the [Function node documentation](https://github.com/n8n-io/n8n-docs/blob/67935ad2528e2e30d7984ea917e4af2910a096ec/docs/integrations/builtin/core-nodes/n8n-nodes-base.function.md){:target=_blank .external-link} and [Function Item node documentation](https://github.com/n8n-io/n8n-docs/blob/67935ad2528e2e30d7984ea917e4af2910a096ec/docs/integrations/builtin/core-nodes/n8n-nodes-base.functionItem.md){:target=_blank .external-link}.
///
#### Usage

How to use the Code node.

##### Choose a mode

There are two modes:

* **Run Once for All Items**: this is the default. When your workflow runs, the code in the code node executes once, regardless of how many input items there are.
* **Run Once for Each Item**: choose this if you want your code to run for every input item.

#### JavaScript

The Code node supports Node.js.

##### Supported JavaScript features

The Code node supports:

* Promises. Instead of returning the items directly, you can return a promise which resolves accordingly.
* Writing to your browser console using `console.log`. This is useful for debugging and troubleshooting your workflows.

##### External libraries

If you self-host n8n, you can import and use built-in and external npm modules in the Code node. To learn how to enable external modules, refer to the [Enable modules in Code node](/hosting/configuration/configuration-examples/modules-in-code-node.md) guide.

If you use n8n Cloud, you can't import external npm modules. n8n makes two modules available for you:

* [crypto Node.js module](https://nodejs.org/docs/latest-v18.x/api/crypto.html){:target=_blank .external-link}
* [moment npm package](https://www.npmjs.com/package/moment){:target=_blank .external-link}

##### Built-in methods and variables

n8n provides built-in methods and variables for working with data and accessing n8n data. Refer to [Built-in methods and variables](/code/builtin/overview.md) for more information.

The syntax to use the built-in methods and variables is `$variableName` or `$methodName()`. Type `$` in the Code node or expressions editor to see a list of suggested methods and variables.

##### Keyboard shortcuts

The Code node editing environment supports time-saving and useful keyboard shortcuts for a range of operations from autocompletion to code-folding and using multiple-cursors. A full list can be found in the [list of keyboard shortcuts](/integrations/builtin/core-nodes/n8n-nodes-base.code/keyboard-shortcuts.md).

#### Python

n8n added Python support in version 1.0. It doesn't include a Python executable. Instead, n8n provides Python support using [Pyodide](https://pyodide.org/en/stable/){:target=_blank .external-link}, which is a port of CPython to WebAssembly. This limits the available Python packages to the [Packages included with Pyodide](https://pyodide.org/en/stable/usage/packages-in-pyodide.html#packages-in-pyodide){:target=_blank .external-link}. n8n downloads the package automatically the first time you use it.

/// note | Slower than JavaScript
The Code node takes longer to process Python than JavaScript. This is due to the extra compilation steps.
///
##### Built-in methods and variables

n8n provides built-in methods and variables for working with data and accessing n8n data. Refer to [Built-in methods and variables](/code/builtin/overview.md) for more information.

The syntax to use the built-in methods and variables is `_variableName` or `_methodName()`. Type `_` in the Code node to see a list of suggested methods and variables.

##### Keyboard shortcuts

The Code node editing environment supports time-saving and useful keyboard shortcuts for a range of operations from autocompletion to code-folding and using multiple-cursors. A full list can be found in the [list of keyboard shortcuts](/integrations/builtin/core-nodes/n8n-nodes-base.code/keyboard-shortcuts.md).

#### File system and HTTP requests

You can't access the file system or make HTTP requests. Use the following nodes instead:

* [Read/Write File From Disk](/integrations/builtin/core-nodes/n8n-nodes-base.readwritefile.md)
* [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md)

#### Coding in n8n

There are two places where you can use code in n8n: the Code node and the expressions editor. When using either area, there are some key concepts you need to know, as well as some built-in methods and variables to help with common tasks.

##### Key concepts

When working with the Code node, you need to understand the following concepts:

* [Data structure](/data/data-structure.md): understand the data you receive in the Code node, and requirements for outputting data from the node.
* [Item linking](/data/data-mapping/data-item-linking/index.md): learn how data items work, and how to link to items from previous nodes. You need to handle item linking in your code when the number of input and output items doesn't match.

##### Built-in methods and variables

n8n includes built-in methods and variables. These provide support for:

* Accessing specific item data
* Accessing data about workflows, executions, and your n8n environment
* Convenience variables to help with data and time

Refer to [Built-in methods and variables](/code/builtin/overview.md) for more information.



#### Use AI in the Code node

--8<-- "_snippets/code/ai-how-to.md"


---



## Custom Execution Data Availability {#custom-execution-data-availability}

*Source: _snippets/workflows/executions/custom-execution-data-availability.md*

/// info | Feature availability
Custom executions data is available on:

* Cloud: Pro, Enterprise
* Self-Hosted: Enterprise, registered Community

Available in version 0.222.0 and above.
///


---



## Retry Options {#retry-options}

*Source: _snippets/workflows/executions/retry-options.md*

3. Select either of the following options to retry the execution:
    * **Retry with currently saved workflow**: Once you make changes to your workflow, you can select this option to execute the workflow with the previous execution data.
    * **Retry with original workflow**: If you want to retry the execution without making changes to your workflow, you can select this option to retry the execution with the previous execution data.


---



## Custom Templates Library {#custom-templates-library}

*Source: _snippets/workflows/templates/custom-templates-library.md*

In your environment variables, set `N8N_TEMPLATES_HOST` to the base URL of your API.

##### Endpoints

Your API must provide the same endpoints and data structure as n8n's.

The endpoints are:

| Method | Path |
| ------ | ---- |
| GET | /templates/workflows/`<id>` |
| GET | /templates/search |
| GET | /templates/collections/`<id>` |
| GET | /templates/collections | 
| GET | /templates/categories |
| GET | /health |

##### Query parameters

The `/templates/search` endpoint accepts the following query parameters:

| Parameter  | Type                                         | Description                                      |
|------------|----------------------------------------------|--------------------------------------------------|
| `page`     | integer                                      | The page of results to return                    |
| `rows`     | integer                                      | The maximum number of results to return per page |
| `category` | comma-separated list of strings (categories) | The categories to search within                  |
| `search`   | string                                       | The search query                                 |

The `/templates/collections` endpoint accepts the following query parameters:

| Parameter  | Type                                         | Description                     |
|------------|----------------------------------------------|---------------------------------|
| `category` | comma-separated list of strings (categories) | The categories to search within |
| `search`   | string                                       | The search query                |

##### Data schema

You can explore the data structure of the items in the response object returned by endpoints here:

??? note "Show `workflow` item data schema"
	```json title="Workflow item data schema"
	{
	  "$schema": "http://json-schema.org/draft-07/schema#",
	  "title": "Generated schema for Root",
	  "type": "object",
	  "properties": {
	    "id": {
	      "type": "number"
	    },
	    "name": {
	      "type": "string"
	    },
	    "totalViews": {
	      "type": "number"
	    },
	    "price": {},
	    "purchaseUrl": {},
	    "recentViews": {
	      "type": "number"
	    },
	    "createdAt": {
	      "type": "string"
	    },
	    "user": {
	      "type": "object",
	      "properties": {
	        "username": {
	          "type": "string"
	        },
	        "verified": {
	          "type": "boolean"
	        }
	      },
	      "required": [
	        "username",
	        "verified"
	      ]
	    },
	    "nodes": {
	      "type": "array",
	      "items": {
	        "type": "object",
	        "properties": {
	          "id": {
	            "type": "number"
	          },
	          "icon": {
	            "type": "string"
	          },
	          "name": {
	            "type": "string"
	          },
	          "codex": {
	            "type": "object",
	            "properties": {
	              "data": {
	                "type": "object",
	                "properties": {
	                  "details": {
	                    "type": "string"
	                  },
	                  "resources": {
	                    "type": "object",
	                    "properties": {
	                      "generic": {
	                        "type": "array",
	                        "items": {
	                          "type": "object",
	                          "properties": {
	                            "url": {
	                              "type": "string"
	                            },
	                            "icon": {
	                              "type": "string"
	                            },
	                            "label": {
	                              "type": "string"
	                            }
	                          },
	                          "required": [
	                            "url",
	                            "label"
	                          ]
	                        }
	                      },
	                      "primaryDocumentation": {
	                        "type": "array",
	                        "items": {
	                          "type": "object",
	                          "properties": {
	                            "url": {
	                              "type": "string"
	                            }
	                          },
	                          "required": [
	                            "url"
	                          ]
	                        }
	                      }
	                    },
	                    "required": [
	                      "primaryDocumentation"
	                    ]
	                  },
	                  "categories": {
	                    "type": "array",
	                    "items": {
	                      "type": "string"
	                    }
	                  },
	                  "nodeVersion": {
	                    "type": "string"
	                  },
	                  "codexVersion": {
	                    "type": "string"
	                  }
	                },
	                "required": [
	                  "categories"
	                ]
	              }
	            }
	          },
	          "group": {
	            "type": "string"
	          },
	          "defaults": {
	            "type": "object",
	            "properties": {
	              "name": {
	                "type": "string"
	              },
	              "color": {
	                "type": "string"
	              }
	            },
	            "required": [
	              "name"
	            ]
	          },
	          "iconData": {
	            "type": "object",
	            "properties": {
	              "icon": {
	                "type": "string"
	              },
	              "type": {
	                "type": "string"
	              },
	              "fileBuffer": {
	                "type": "string"
	              }
	            },
	            "required": [
	              "type"
	            ]
	          },
	          "displayName": {
	            "type": "string"
	          },
	          "typeVersion": {
	            "type": "number"
	          },
	          "nodeCategories": {
	            "type": "array",
	            "items": {
	              "type": "object",
	              "properties": {
	                "id": {
	                  "type": "number"
	                },
	                "name": {
	                  "type": "string"
	                }
	              },
	              "required": [
	                "id",
	                "name"
	              ]
	            }
	          }
	        },
	        "required": [
	          "id",
	          "icon",
	          "name",
	          "codex",
	          "group",
	          "defaults",
	          "iconData",
	          "displayName",
	          "typeVersion"
	        ]
	      }
	    }
	  },
	  "required": [
	    "id",
	    "name",
	    "totalViews",
	    "price",
	    "purchaseUrl",
	    "recentViews",
	    "createdAt",
	    "user",
	    "nodes"
	  ]
	}
	```

??? note "Show `category` item data schema"
	```json title="Category item data schema"
	{
	  "$schema": "http://json-schema.org/draft-07/schema#",
	  "type": "object",
	  "properties": {
	    "id": {
	      "type": "number"
	    },
	    "name": {
	      "type": "string"
	    }
	  },
	  "required": [
	    "id",
	    "name"
	  ]
	}
	```

??? note "Show `collection` item data schema"
	```json title="Collection item data schema"
	{
	  "$schema": "http://json-schema.org/draft-07/schema#",
	  "type": "object",
	  "properties": {
	    "id": {
	      "type": "number"
	    },
	    "rank": {
	      "type": "number"
	    },
	    "name": {
	      "type": "string"
	    },
	    "totalViews": {},
	    "createdAt": {
	      "type": "string"
	    },
	    "workflows": {
	      "type": "array",
	      "items": {
	        "type": "object",
	        "properties": {
	          "id": {
	            "type": "number"
	          }
	        },
	        "required": [
	          "id"
	        ]
	      }
	    },
	    "nodes": {
	      "type": "array",
	      "items": {}
	    }
	  },
	  "required": [
	    "id",
	    "rank",
	    "name",
	    "totalViews",
	    "createdAt",
	    "workflows",
	    "nodes"
	  ]
	}
	```

You can also interactively explore n8n's API endpoints:

[https://api.n8n.io/templates/categories](https://api.n8n.io/templates/categories)  
[https://api.n8n.io/templates/collections](https://api.n8n.io/templates/collections)  
[https://api.n8n.io/templates/search](https://api.n8n.io/templates/search)  
[https://api.n8n.io/health](https://api.n8n.io/health)  


You can [contact us](mailto:help@n8n.io) for more support.


---



## Disable Templates {#disable-templates}

*Source: _snippets/workflows/templates/disable-templates.md*

In your environment variables, set `N8N_TEMPLATES_ENABLED` to false.


---



## Submit Templates {#submit-templates}

*Source: _snippets/workflows/templates/submit-templates.md*

You can submit your workflows to n8n's template library.

n8n is working on a creator program, and developing a marketplace of templates. This is an ongoing project, and details are likely to change.

Refer to [n8n Creator hub](https://www.notion.so/n8n/n8n-Creator-hub-7bd2cbe0fce0449198ecb23ff4a2f76f){:target=_blank .external-link} for information on how to submit templates and become a creator.


---



## Index {#index}

*Source: docs/advanced-ai/index.md*


##### Advanced AI

Build AI functionality using n8n: from creating your own chat bot, to using AI to process documents and data from other sources.

/// info | Feature availability
This feature is available on Cloud and self-hosted n8n, in version 1.19.4 and above.
///

<div class="grid cards" markdown>

-   __Get started__

    Work through the short tutorial to learn the basics of building AI workflows in n8n.

    [:octicons-arrow-right-24: Tutorial](/advanced-ai/intro-tutorial.md)

-   __Use a Starter Kit__

    Try n8n's Self-hosted AI Starter Kit to quickly start building AI workflows.

    [:octicons-arrow-right-24: Self-hosted AI Starter Kit](/hosting/starter-kits/ai-starter-kit.md)

-   __Explore examples and concepts__

	Browse examples and workflow templates to help you build. Includes explanations of important AI concepts.

    [:octicons-arrow-right-24: Examples](/advanced-ai/examples/introduction.md)

-   __How n8n uses LangChain__

    Learn more about how n8n builds on LangChain.

    [:octicons-arrow-right-24: LangChain in n8n](/advanced-ai/langchain/overview.md)

-   __Browse AI templates__

    Explore a wide range of AI workflow templates on the n8n website.

    [:octicons-arrow-right-24: AI workflows on n8n.io](https://n8n.io/workflows/?categories=25){:target=_blank .external-link}

</div>

#### Related resources

Related documentation and tools.

##### Node types

This feature uses [Cluster nodes](/integrations/builtin/cluster-nodes/index.md): groups of [root](/integrations/builtin/cluster-nodes/root-nodes/index.md) and [sub](/integrations/builtin/cluster-nodes/sub-nodes/index.md) nodes that work together.

--8<-- "_snippets/integrations/builtin/cluster-nodes/cluster-nodes-summary.md"

##### Workflow templates

You can browse [workflow templates](/glossary.md#template-n8n) in-app or on the n8n website [Workflows](https://n8n.io/workflows/?categories=25,26){:target=_blank .external-link} page.

Refer to [Templates](/workflows/templates.md) for information on accessing templates in-app.

##### Chat trigger

Use the [n8n Chat Trigger](/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/index.md) to trigger a workflow based on chat interactions.

##### Chatbot widget

n8n provides a chatbot widget that you can use as a frontend for AI-powered chat workflows. Refer to the [@n8n/chat npm page](https://www.npmjs.com/package/@n8n/chat){:target=_blank .external-link} for usage information.


---



## Index {#index}

*Source: docs/api/index.md*


##### n8n public REST API

/// info | Feature availability
The n8n API isn't available during the free trial. Please upgrade to access this feature.  
///

Using n8n's public [API](/glossary.md#api), you can programmatically perform many of the same tasks as you can in the GUI. This section introduces n8n's REST API, including:

* How to [authenticate](/api/authentication.md)
* [Paginating](/api/pagination.md) results
* Using the [built-in API playground](/api/using-api-playground.md) (self-hosted n8n only)
* [Endpoint reference](/api/api-reference.md)

n8n provides an [n8n API node](/integrations/builtin/core-nodes/n8n-nodes-base.n8n.md) to access the API in your workflows.

#### Learn about REST APIs

The API documentation assumes you are familiar with REST APIs. If you're not, these resources may be helpful:

* [KnowledgeOwl's guide to working with APIs](https://support.knowledgeowl.com/help/working-with-apis){:target=_blank .external-link}: a basic introduction, including examples of how to call REST APIs.
* [IBM Cloud Learn Hub - What is an Application Programming Interface (API)](https://www.ibm.com/cloud/learn/api){:target=_blank .external-link}: this gives a general, but technical, introduction to APIs.
* [IBM Cloud Learn Hub - What is a REST API?](https://www.ibm.com/cloud/learn/rest-apis){:target=_blank .external-link}: more detailed information about REST APIs.
* [MDN web docs - An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview){:target=_blank .external-link}: REST APIs work over HTTP and use HTTP verbs, or methods, to specify the action to perform.

/// tip | Use the API playground (self-hosted n8n only)
Trying out the API in the [playground](/api/using-api-playground.md) can help you understand how APIs work. If you're worried about changing live data, consider setting up a test workflow, or test n8n instance, to explore safely.
///


---



## Convenience {#convenience}

*Source: docs/code/builtin/convenience.md*


##### Convenience methods

n8n provides these methods to make it easier to perform common tasks in [expressions](/glossary.md#expression-n8n).

/// note | Python support
You can use Python in the Code node. It isn't available in expressions.
///

=== "JavaScript"
	| Method | Description | Available in Code node? |
	| ------ | ----------- | :---------------------: |
	| `$evaluateExpression(expression: string, itemIndex?: number)` | Evaluates a string as an expression. If you don't provide `itemIndex`, n8n uses the data from item 0 in the Code node. | :white_check_mark: |
	| `$ifEmpty(value, defaultValue)` | The `$ifEmpty()` function takes two parameters, tests the first to check if it's empty, then returns either the parameter (if not empty) or the second parameter (if the first is empty). The first parameter is empty if it's:<ul><li>`undefined`</li><li>`null`</li><li>An empty string `''`</li><li>An array where `value.length` returns `false`</li><li>An object where `Object.keys(value).length` returns `false`</li></ul> | :white_check_mark: |
	| `$if()` | The `$if()` function takes three parameters: a condition, the value to return if true, and the value to return if false. | :x: | 
	| `$max()` | Returns the highest of the provided numbers. | :x: |
	| `$min()` | Returns the lowest of the provided numbers. | :x: |
=== "Python"
	| Method | Description |
	| ------ | ----------- | 
	| `_evaluateExpression(expression: string, itemIndex?: number)` | Evaluates a string as an expression. If you don't provide `itemIndex`, n8n uses the data from item 0 in the Code node. |
	| `_ifEmpty(value, defaultValue)` | The `_ifEmpty()` function takes two parameters, tests the first to check if it's empty, then returns either the parameter (if not empty) or the second parameter (if the first is empty). The first parameter is empty if it's:<ul><li>`undefined`</li><li>`null`</li><li>An empty string `''`</li><li>An array where `value.length` returns `false`</li><li>An object where `Object.keys(value).length` returns `false`</li></ul> | :white_check_mark: |


---



## Current Node Input {#current-node-input}

*Source: docs/code/builtin/current-node-input.md*


##### Current node input

Methods for working with the input of the current node. Some methods and variables aren't available in the Code node.

/// note | Python support
You can use Python in the Code node. It isn't available in expressions.
///
=== "JavaScript"
	| Method | Description | Available in Code node? |
	| ------ | ----------- | :-------------------------: |
	| `$binary` | Shorthand for `$input.item.binary`. Incoming binary data from a node | :x: |
	| `$input.item` | The input item of the current node that's being processed. Refer to [Item linking](/data/data-mapping/data-item-linking/index.md) for more information on paired items and item linking. | :white_check_mark: |
	| `$input.all()` | All input items in current node. | :white_check_mark: |
	| `$input.first()` | First input item in current node. | :white_check_mark: |
	| `$input.last()` | Last input item in current node. | :white_check_mark: |
	| `$input.params` | Object containing the query settings of the previous node. This includes data such as the operation it ran, result limits, and so on.  | :white_check_mark: |
	| `$json` | Shorthand for `$input.item.json`. Incoming JSON data from a node. Refer to [Data structure](/data/data-structure.md) for information on item structure. | :white_check_mark: (when running once for each item) |
	| `$input.context.noItemsLeft` | Boolean. Only available when working with the Loop Over Items node. Provides information about what's happening in the node. Use this to determine whether the node is still processing items. | :white_check_mark: |
=== "Python"
	| Method | Description | 
	| ------ | ----------- | 
	| `_input.item` | The input item of the current node that's being processed. Refer to [Item linking](/data/data-mapping/data-item-linking/index.md) for more information on paired items and item linking. | 
	| `_input.all()` | All input items in current node. | 
	| `_input.first()` | First input item in current node. | 
	| `_input.last()` | Last input item in current node. | 
	| `_input.params` | Object containing the query settings of the previous node. This includes data such as the operation it ran, result limits, and so on.  | 
	| `_json` | Shorthand for `_input.item.json`. Incoming JSON data from a node. Refer to [Data structure](/data/data-structure.md) for information on item structure. Available when you set **Mode** to **Run Once for Each Item**. | 
	| `_input.context.noItemsLeft` | Boolean. Only available when working with the Loop Over Items node. Provides information about what's happening in the node. Use this to determine whether the node is still processing items. | 


---



## Index {#index}

*Source: docs/code/builtin/data-transformation-functions/index.md*


##### Data transformation functions

Data transformation functions are helper functions to make data transformation easier in [expressions](/glossary.md#expression-n8n).

/// note | JavaScript in expressions
You can use any JavaScript in expressions. Refer to [Expressions](/code/expressions.md) for more information.
///
For a list of available functions, refer to the page for your data type:

* [Arrays](/code/builtin/data-transformation-functions/arrays.md)
* [Dates](/code/builtin/data-transformation-functions/dates.md)
* [Numbers](/code/builtin/data-transformation-functions/numbers.md)
* [Objects](/code/builtin/data-transformation-functions/objects.md)
* [Strings](/code/builtin/data-transformation-functions/strings.md)

#### Usage

Data transformation functions are available in the expressions editor.

The syntax is:

```js
{{ dataItem.function() }}
```

For example, to check if a string is an email:

```js
{{ "example@example.com".isEmail() }}

// Returns true
```


---



## Date Time {#date-time}

*Source: docs/code/builtin/date-time.md*


##### Built-in date and time methods

Methods for working with date and time. 

/// note | Python support
You can use Python in the Code node. It isn't available in expressions.
///
=== "JavaScript"
	| Method | Description | Available in Code node? |
	| ------ | ----------- | :-------------------------: |
	| `$now` | A Luxon object containing the current timestamp. Equivalent to `DateTime.now()`. | :white_check_mark: |
	| `$today` | A Luxon object containing the current timestamp, rounded down to the day. Equivalent to `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 })`. | :white_check_mark: |
=== "Python"
	| Method | Description | 
	| ------ | ----------- | 
	| `_now` | A Luxon object containing the current timestamp. Equivalent to `DateTime.now()`. | 
	| `_today` | A Luxon object containing the current timestamp, rounded down to the day. Equivalent to `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 })`. | 

n8n passes dates between nodes as strings, so you need to parse them. Luxon helps you do this. Refer to [Date and time with Luxon](/code/cookbook/luxon.md) for more information.

n8n provides built-in convenience functions to support data transformation in expressions for dates. Refer to [Data transformation functions | Dates](/code/builtin/data-transformation-functions/dates.md) for more information.


---



## Http Node Variables {#http-node-variables}

*Source: docs/code/builtin/http-node-variables.md*


##### HTTP node variables

Variables for working with HTTP node requests and responses when using pagination.

Refer to [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) for guidance on using the HTTP node, including configuring pagination.

Refer to [HTTP Request node cookbook | Pagination](/code/cookbook/http-node/pagination.md) for example pagination configurations.

/// note | HTTP node only
These variables are for use in expressions in the HTTP node. You can't use them in other nodes.
///
--8<-- "_snippets/integrations/builtin/core-nodes/http/pagination-variables.md"


---



## Jmespath {#jmespath}

*Source: docs/code/builtin/jmespath.md*


##### JMESPath method

This is an n8n-provided method for working with the [JMESPath](/code/cookbook/jmespath.md) library.

/// note | Python support
You can use Python in the Code node. It isn't available in expressions.
///
=== "JavaScript"
	| Method | Description | Available in Code node? |
	| ------ | ----------- | :-------------------------: |
	| `$jmespath()` | Perform a search on a JSON object using JMESPath. | :white_check_mark: |
=== "Python"
	| Method | Description | 
	| ------ | ----------- | 
	| `_jmespath()` | Perform a search on a JSON object using JMESPath. | 


---



## Langchain Methods {#langchain-methods}

*Source: docs/code/builtin/langchain-methods.md*

##### LangChain Code node methods

n8n provides these methods to make it easier to perform common tasks in the [LangChain Code node](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.code.md).

/// note | LangChain Code node only
These variables are for use in expressions in the LangChain Code node. You can't use them in other nodes.
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-root-nodes/langchaincode/builtin-methods.md"


---



## N8N Metadata {#n8n-metadata}

*Source: docs/code/builtin/n8n-metadata.md*


##### n8n metadata

Methods for working with n8n metadata.

This includes:

* Access to n8n environment variables for self-hosted n8n.
* Metadata about workflows, executions, and nodes.
* Information about instance [Variables](/code/variables.md) and [External secrets](/external-secrets.md).

/// note | Python support
You can use Python in the Code node. It isn't available in expressions.
///
=== "JavaScript"
	| Method | Description | Available in Code node? |
	| ------ | ----------- | :-------------------------: |
	| `$env` | Contains n8n instance configuration [environment variables](/hosting/configuration/environment-variables/index.md). | :white_check_mark: |
	| `$execution.customData` | Set and get custom execution data. Refer to [Custom executions data](/workflows/executions/custom-executions-data.md) for more information. | :white_check_mark: | 
	| `$execution.id` | The unique ID of the current workflow execution. | :white_check_mark: |
	| `$execution.mode` | Whether the execution was triggered automatically, or by manually running the workflow. Possible values are `test` and `production`. | :white_check_mark: |
	| `$execution.resumeUrl` | The webhook URL to call to resume a workflow waiting at a [Wait node](/integrations/builtin/core-nodes/n8n-nodes-base.wait.md). | :white_check_mark: |
	| `$getWorkflowStaticData(type)` | View an [example](/code/cookbook/builtin/get-workflow-static-data.md). Static data doesn't persist when testing workflows. The workflow must be active and called by a trigger or webhook to save static data. This gives access to the static workflow data. | :white_check_mark: |
	| `$("<node-name>").isExecuted` | Check whether a node has already executed. | :white_check_mark: |
	| `$itemIndex` | The index of an item in a list of items. | :x: |
	| `$nodeVersion` | Get the version of the current node. | :white_check_mark: |
	| `$prevNode.name` | The name of the node that the current input came from. When using the Merge node, note that `$prevNode` always uses the first input connector. | :white_check_mark: |
	| `$prevNode.outputIndex` | The index of the output connector that the current input came from. Use this when the previous node had multiple outputs (such as an If or Switch node).  When using the Merge node, note that `$prevNode` always uses the first input connector. | :white_check_mark: |
	| `$prevNode.runIndex` | The run of the previous node that generated the current input. When using the Merge node, note that `$prevNode` always uses the first input connector. | :white_check_mark: |
	| `$runIndex` | How many times n8n has executed the current node. Zero-based (the first run is 0, the second is 1, and so on). | :white_check_mark: |
	| `$secrets` | Contains information about your [External secrets](/external-secrets.md) setup. | :white_check_mark: |
	| `$vars` | Contains the [Variables](/code/variables.md) available in the active environment. | :white_check_mark: |
	| `$version` | The node version. | :x: |
	| `$workflow.active` | Whether the workflow is active (true) or not (false). | :white_check_mark: |
	| `$workflow.id` | The workflow ID. | :white_check_mark: |
	| `$workflow.name` | The workflow name. | :white_check_mark: |
=== "Python"
	| Method | Description |
	| ------ | ----------- |
	| `_env` | Contains n8n instance configuration [environment variables](/hosting/configuration/environment-variables/index.md). |
	| `_execution.customData` | Set and get custom execution data. Refer to [Custom executions data](/workflows/executions/custom-executions-data.md) for more information. | 
	| `_execution.id` | The unique ID of the current workflow execution. | 
	| `_execution.mode` | Whether the execution was triggered automatically, or by manually running the workflow. Possible values are `test` and `production`. | 
	| `_execution.resumeUrl` | The webhook URL to call to resume a workflow waiting at a [Wait node](/integrations/builtin/core-nodes/n8n-nodes-base.wait.md). |
	| `_getWorkflowStaticData(type)` | View an [example](/code/cookbook/builtin/get-workflow-static-data.md). Static data doesn't persist when testing workflows. The workflow must be active and called by a trigger or webhook to save static data. This gives access to the static workflow data. |
	| `_("<node-name>").isExecuted` | Check whether a node has already executed. |
	| `_nodeVersion` | Get the version of the current node. | :white_check_mark: |
	| `_prevNode.name` | The name of the node that the current input came from. When using the Merge node, note that `_prevNode` always uses the first input connector. | 
	| `_prevNode.outputIndex` | The index of the output connector that the current input came from. Use this when the previous node had multiple outputs (such as an If or Switch node).  When using the Merge node, note that `_prevNode` always uses the first input connector. | 
	| `_prevNode.runIndex` | The run of the previous node that generated the current input. When using the Merge node, note that `_prevNode` always uses the first input connector. |
	| `_runIndex` | How many times n8n has executed the current node. Zero-based (the first run is 0, the second is 1, and so on). |
	| `_secrets` | Contains information about your [External secrets](/external-secrets.md) setup. | 
	| `_vars` | Contains the [Variables](/code/variables.md) available in the active environment. | 
	| `_workflow.active` | Whether the workflow is active (true) or not (false). |
	| `_workflow.id` | The workflow ID. | 
	| `_workflow.name` | The workflow name. |


---



## Output Other Nodes {#output-other-nodes}

*Source: docs/code/builtin/output-other-nodes.md*


##### Output of other nodes

Methods for working with the output of other nodes. Some methods and variables aren't available in the Code node.

/// note | Python support
You can use Python in the Code node. It isn't available in expressions.
///
=== "JavaScript"
	| Method | Description | Available in Code node? |
	| ------ | ----------- | :-------------------------: |
	| `$("<node-name>").all(branchIndex?, runIndex?)` | Returns all items from a given node. If `branchIndex` isn't given it will default to the output that connects `node-name` with the node where you use the expression or code. | :white_check_mark: |
	| `$("<node-name>").first(branchIndex?, runIndex?)` | The first item output by the given node. If `branchIndex` isn't given it will default to the output that connects `node-name` with the node where you use the expression or code. | :white_check_mark: |
	| `$("<node-name>").last(branchIndex?, runIndex?)` | The last item output by the given node. If `branchIndex` isn't given it will default to the output that connects `node-name` with the node where you use the expression or code. | :white_check_mark: |
	| `$("<node-name>").item` | The linked item. This is the item in the specified node used to produce the current item. Refer to [Item linking](/data/data-mapping/data-item-linking/index.md) for more information on item linking. | :x: |
	| `$("<node-name>").params` | Object containing the query settings of the given node. This includes data such as the operation it ran, result limits, and so on. | :white_check_mark: |
	| `$("<node-name>").context` | Boolean. Only available when working with the Loop Over Items node. Provides information about what's happening in the node. Use this to determine whether the node is still processing items. | :white_check_mark: |
	| `$("<node-name>").itemMatching(currentNodeInputIndex)` | Use instead of `$("<node-name>").item` in the Code node if you need to trace back from an input item. | :white_check_mark: |
=== "Python"
	| Method | Description | Available in Code node? |
	| ------ | ----------- | :-------------------------: |
	| `_("<node-name>").all(branchIndex?, runIndex?)` | Returns all items from a given node. If `branchIndex` isn't given it will default to the output that connects`node-name` with the node where you use the expression or code. | :white_check_mark: |
	| `_("<node-name>").first(branchIndex?, runIndex?)` | The first item output by the given node. If `branchIndex` isn't given it will default to the output that connects`node-name` with the node where you use the expression or code. | :white_check_mark: |
	| `_("<node-name>").last(branchIndex?, runIndex?)` | The last item output by the given node. If `branchIndex` isn't given it will default to the output that connects`node-name` with the node where you use the expression or code. | :white_check_mark: |
	| `_("<node-name>").item` | The linked item. This is the item in the specified node used to produce the current item. Refer to [Item linking](/data/data-mapping/data-item-linking/index.md) for more information on item linking. | :x: |
	| `_("<node-name>").params` | Object containing the query settings of the given node. This includes data such as the operation it ran, result limits, and so on. | :white_check_mark: |
	| `_("<node-name>").context` | Boolean. Only available when working with the Loop Over Items node. Provides information about what's happening in the node. Use this to determine whether the node is still processing items. | :white_check_mark: |
	| `_("<node-name>").itemMatching(currentNodeInputIndex)` | Use instead of `_("<node-name>").item` in the Code node if you need to trace back from an input item. Refer to [Retrieve linked items from earlier in the workflow](/code/cookbook/builtin/itemmatching.md) for an example. | :white_check_mark: |


---



## Overview {#overview}

*Source: docs/code/builtin/overview.md*


##### Built-in methods and variables

n8n provides built-in methods and variables for working with data and accessing n8n data. This section provides a reference of available methods and variables for use in [expressions](/glossary.md#expression-n8n), with a short description. 

/// note | Availability in the expressions editor and the Code node
Some methods and variables aren't available in the Code node. These aren't in the documentation.

All data transformation functions are only available in the expressions editor.
///		


The [Cookbook](/code/index.md) contains examples for some common tasks, including some [Code node only](/code/cookbook/code-node/index.md) functions.

[[% import "_macros/section-toc.html" as sectionToc %]]

[[ sectionToc.sectionToc(page) ]]


---



## Code Node {#code-node}

*Source: docs/code/code-node.md*


##### Using the Code node

--8<-- "_snippets/integrations/builtin/core-nodes/code-node.md"


---



## Index {#index}

*Source: docs/code/cookbook/builtin/index.md*


##### Examples using n8n's built-in methods and variables

n8n provides built-in methods and variables for working with data and accessing n8n data. This section provides usage examples.

[[% import "_macros/section-toc.html" as sectionToc %]]

[[ sectionToc.sectionToc(page) ]]

#### Related resources

* [Built-in methods and variables reference](/code/builtin/overview.md)
* [Expressions](/code/expressions.md)
* [Code node](/code/code-node.md)


---



## Index {#index}

*Source: docs/code/cookbook/code-node/index.md*


##### Code node cookbook

This section contains examples and recipes for tasks you can do with the Code node.

[[% import "_macros/section-toc.html" as sectionToc %]]

[[ sectionToc.sectionToc(page) ]]

#### Related resources

* [Built-in methods and variables reference](/code/builtin/overview.md)
* [Code node](/code/code-node.md)


---



## Index {#index}

*Source: docs/code/cookbook/expressions/index.md*


##### Expressions cookbook

This section contains examples and recipes for tasks you can do with [expressions](/glossary.md#expression-n8n).

/// note | Python support
You can use Python in the Code node. It isn't available in expressions.
///
[[% import "_macros/section-toc.html" as sectionToc %]]

[[ sectionToc.sectionToc(page) ]]

#### Related resources

* [Built-in methods and variables reference](/code/builtin/overview.md)
* [Expressions](/code/expressions.md)


---



## Index {#index}

*Source: docs/code/cookbook/http-node/index.md*


##### Examples using n8n's HTTP Request node

The HTTP Request node is one of the most versatile nodes in n8n. Use this node to make HTTP requests to query data from any app or service with a REST API.

Refer to [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) for information on node settings.

[[% import "_macros/section-toc.html" as sectionToc %]]

[[ sectionToc.sectionToc(page) ]]

#### Related resources

* [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md)
* [Built-in methods and variables reference](/code/builtin/overview.md)
* [Expressions](/code/expressions.md)


---



## Jmespath {#jmespath}

*Source: docs/code/cookbook/jmespath.md*


##### Query JSON with JMESPath

[JMESPath](https://jmespath.org/){:target=_blank .external-link} is a query language for JSON that you can use to extract and transform elements from a JSON document. For full details of how to use JMESPath, refer to the [JMESPath documentation](https://jmespath.org/tutorial.html){:target=_blank .external-link}.


#### The `jmespath()` method

n8n provides a custom method, `jmespath()`. Use this method to perform a search on a JSON object using the JMESPath query language.

The basic syntax is: 

=== "JavaScript"
	```js
	$jmespath(object, searchString)
	```
=== "Python"
	```python
	_jmespath(object, searchString)
	```


To help understand what the method does, here is the equivalent longer JavaScript:


```js
var jmespath = require('jmespath');
jmespath.search(object, searchString);
```

/// note | Expressions must be single-line
The longer code example doesn't work in Expressions, as they must be single-line.
///

`object` is a JSON object, such as the output of a previous node. `searchString` is an expression written in the JMESPath query language. The [JMESPath Specification](https://jmespath.org/specification.html#jmespath-specification){:target=_blank .external-link} provides a list of supported expressions, while their [Tutorial](https://jmespath.org/tutorial.html) and [Examples](https://jmespath.org/examples.html){:target=_blank .external-link} provide interactive examples.

/// warning | Search parameter order
The examples in the [JMESPath Specification](https://jmespath.org/specification.html#jmespath-specification){:target=_blank .external-link} follow the pattern `search(searchString, object)`. The [JMESPath JavaScript library](https://github.com/jmespath/jmespath.js/){:target=_blank .external-link}, which n8n uses, supports `search(object, searchString)` instead. This means that when using examples from the JMESPath documentation, you may need to change the order of the search function parameters.
///

#### Common tasks

This section provides examples for some common operations. More examples, and detailed guidance, are available in [JMESPath's own documentation](https://jmespath.org/tutorial.html){:target=_blank .external-link}.

When trying out these examples, you need to set the Code node **Mode** to **Run Once for Each Item**.

##### Apply a JMESPath expression to a collection of elements with projections

From the [JMESPath projections documentation](https://jmespath.org/tutorial.html#projections){:target=_blank .external-link}:

> Projections are one of the key features of JMESPath. Use it to apply an expression to a collection of elements. JMESPath supports five kinds of projections:
> 
> * List Projections
> * Slice Projections
> * Object Projections
> * Flatten Projections
> * Filter Projections

The following example shows basic usage of list, slice, and object projections. Refer to the [JMESPath projections documentation](https://jmespath.org/tutorial.html#projections){:target=_blank .external-link} for detailed explanations of each projection type, and more examples.

Given this JSON from a webhook node:


```js
[
  {
    "headers": {
      "host": "n8n.instance.address",
      ...
    },
    "params": {},
    "query": {},
    "body": {
      "people": [
        {
          "first": "James",
          "last": "Green"
        },
        {
          "first": "Jacob",
          "last": "Jones"
        },
        {
          "first": "Jayden",
          "last": "Smith"
        }
      ],
      "dogs": {
        "Fido": {
          "color": "brown",
          "age": 7
        },
        "Spot": {
          "color": "black and white",
          "age": 5
        }
      }
    }
  }
]

```


Retrieve a [list](https://jmespath.org/tutorial.html#list-and-slice-projections){:target=_blank .external-link} of all the people's first names:

=== "Expressions (JavaScript)"

	```js
	{{$jmespath($json.body.people, "[*].first" )}}
	// Returns ["James", "Jacob", "Jayden"]
	```

=== "Code node (JavaScript)"

	```js
	let firstNames = $jmespath($json.body.people, "[*].first" )
	return {firstNames};
	/* Returns:
	[
		{
			"firstNames": [
				"James",
				"Jacob",
				"Jayden"
			]
		}
	]
	*/
	```
=== "Code node (Python)"
	```python
	firstNames = _jmespath(_json.body.people, "[*].first" )
	return {"firstNames":firstNames}
	"""
	Returns:
	[
	 	{
			"firstNames": [
				"James",
				"Jacob",
				"Jayden"
			]
		}
	]
	"""
	```

Get a [slice](https://jmespath.org/tutorial.html#list-and-slice-projections){:target=_blank .external-link} of the first names:

=== "Expressions (JavaScript)"

	```js
	{{$jmespath($json.body.people, "[:2].first")}}
	// Returns ["James", "Jacob"]
	```

=== "Code node (JavaScript)"
	```js
	let firstTwoNames = $jmespath($json.body.people, "[:2].first");
	return {firstTwoNames};
	/* Returns:
	[
		{
			"firstNames": [
				"James",
				"Jacob",
				"Jayden"
			]
		}
	]
	*/
	```
=== "Code node (Python)"
	```python
	firstTwoNames = _jmespath(_json.body.people, "[:2].first" )
	return {"firstTwoNames":firstTwoNames}
	"""
	Returns:
	[
  		{
			"firstTwoNames": [
			"James",
			"Jacob"
			]
		}
	]
	"""
	```

Get a list of the dogs' ages using [object projections](https://jmespath.org/tutorial.html#object-projections){:target=_blank .external-link}:

=== "Expressions (JavaScript)"

	```js
	{{$jmespath($json.body.dogs, "*.age")}}
	// Returns [7,5]
	```

=== "Code node (JavaScript)"
	```js
	let dogsAges = $jmespath($json.body.dogs, "*.age");
	return {dogsAges};
	/* Returns:
	[
		{
			"dogsAges": [
				7,
				5
			]
		}
	]
	*/
	```
=== "Code node (Python)"
	```python
	dogsAges = _jmespath(_json.body.dogs, "*.age")
	return {"dogsAges": dogsAges}
	"""
	Returns:
	[
		{
			"dogsAges": [
				7,
				5
			]
		}
	]
	"""
	```

##### Select multiple elements and create a new list or object

Use [Multiselect](https://jmespath.org/tutorial.html#multiselect){:target=_blank .external-link} to select elements from a JSON object and combine them into a new list or object.

Given this JSON from a webhook node:


```js
[
  {
    "headers": {
      "host": "n8n.instance.address",
      ...
    },
    "params": {},
    "query": {},
    "body": {
      "people": [
        {
          "first": "James",
          "last": "Green"
        },
        {
          "first": "Jacob",
          "last": "Jones"
        },
        {
          "first": "Jayden",
          "last": "Smith"
        }
      ],
      "dogs": {
        "Fido": {
          "color": "brown",
          "age": 7
        },
        "Spot": {
          "color": "black and white",
          "age": 5
        }
      }
    }
  }
]

```

<!-- vale off -->
Use multiselect list to get the first and last names and create new lists containing both names:
<!-- vale on -->
=== "Expressions (JavaScript)"

	[[% raw %]]
	```js
	{{$jmespath($json.body.people, "[].[first, last]")}}
	// Returns [["James","Green"],["Jacob","Jones"],["Jayden","Smith"]]
	```
	[[% endraw %]]

=== "Code node (JavaScript)"

	```js
	let newList = $jmespath($json.body.people, "[].[first, last]");
	return {newList};
	/* Returns:
	[
		{
			"newList": [
				[
					"James",
					"Green"
				],
				[
					"Jacob",
					"Jones"
				],
				[
					"Jayden",
					"Smith"
				]
			]
		}
	]
	*/
	```
=== "Code node (Python)"
	```python
	newList = _jmespath(_json.body.people, "[].[first, last]")
	return {"newList":newList}
	"""
	Returns:
	[
		{
			"newList": [
				[
					"James",
					"Green"
				],
				[
					"Jacob",
					"Jones"
				],
				[
					"Jayden",
					"Smith"
				]
			]
		}
	]
	"""
	```

##### An alternative to arrow functions in expressions

For example, generate some input data by returning the below code from the Code node:

```js
return[
  {
    "json": {      
      "num_categories": "0",
      "num_products": "45",
      "category_id": 5529735,
      "parent_id": 1407340,
      "pos_enabled": 1,
      "pos_favorite": 0,
      "name": "HP",
      "description": "",
      "image": ""
    }
  },
  {
    "json": {
      "num_categories": "0",
      "num_products": "86",
      "category_id": 5529740,
      "parent_id": 1407340,
      "pos_enabled": 1,
      "pos_favorite": 0,
      "name": "Lenovo",
      "description": "",
      "image": ""
    }
  }  
]
```

You could do a search like "find the item with the name Lenovo and tell me their category ID."

```js
{{ $jmespath($("Code").all(), "[?json.name=='Lenovo'].json.category_id") }}
```


---



## Luxon {#luxon}

*Source: docs/code/cookbook/luxon.md*


##### Date and time with Luxon

[Luxon](https://github.com/moment/luxon/){:target=_blank .external-link} is a JavaScript library that makes it easier to work with date and time. For full details of how to use Luxon, refer to [Luxon's documentation](https://moment.github.io/luxon/#/?id=luxon){:target=_blank .external-link}. 

n8n passes dates between nodes as strings, so you need to parse them. Luxon makes this easier.

/// note | Python support
Luxon is a JavaScript library. The two convenience [variables](#variables) created by n8n are available when using Python in the Code node, but their functionality is limited:

* You can't perform Luxon operations on these variables. For example, there is no Python equivalent for `$today.minus(...)`.
* The generic Luxon functionality, such as [Convert date string to Luxon](#convert-date-string-to-luxon), isn't available for Python users.
///	


#### Variables

n8n uses Luxon to provide two custom variables:

- `now`: a Luxon object containing the current timestamp. Equivalent to `DateTime.now()`.
- `today`: a Luxon object containing the current timestamp, rounded down to the day. Equivalent to `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 })`.

Note that these variables can return different time formats when cast as a string. This is the same behavior as Luxon's `DateTime.now()`.

=== "Expressions (JavaScript)"

	``` js
	{{$now}}
	// n8n displays the ISO formatted timestamp
	// For example 2022-03-09T14:02:37.065+00:00
	{{"Today's date is " + $now}}
	// n8n displays "Today's date is <unix timestamp>"
	// For example "Today's date is 1646834498755"
	```

=== "Code node (JavaScript)"

	``` js
	$now
	// n8n displays <ISO formatted timestamp>
	// For example 2022-03-09T14:00:25.058+00:00
	let rightNow = "Today's date is " + $now
	// n8n displays "Today's date is <unix timestamp>"
	// For example "Today's date is 1646834498755"
	```
=== "Code node (Python)"
	``` python
	_now
	# n8n displays <ISO formatted timestamp>
	# For example 2022-03-09T14:00:25.058+00:00
	rightNow = "Today's date is " + str(_now)
	# n8n displays "Today's date is <unix timestamp>"
	# For example "Today's date is 1646834498755"
	```

n8n provides built-in convenience functions to support data transformation in expressions for dates. Refer to [Data transformation functions | Dates](/code/builtin/data-transformation-functions/dates.md) for more information.

#### Date and time behavior in n8n

Be aware of the following:

* In a workflow, n8n converts dates and times to strings between nodes. Keep this in mind when doing arithmetic on dates and times from other nodes.
* With vanilla JavaScript, you can convert a string to a date with `new Date('2019-06-23')`. In Luxon, you must use a function explicitly stating the format, such as `DateTime.fromISO('2019-06-23')` or `DateTime.fromFormat("23-06-2019", "dd-MM-yyyy")`.

#### Setting the timezone in n8n

Luxon uses the n8n timezone. This value is either:

* Default: `America/New York`
* A custom timezone for your n8n instance, set using the `GENERIC_TIMEZONE` environment variable.
* A custom timezone for an individual workflow, configured in workflow settings.

#### Common tasks

This section provides examples for some common operations. More examples, and detailed guidance, are available in [Luxon's own documentation](https://moment.github.io/luxon/#/?id=luxon){:target="_blank" .external-link}.


##### Convert date string to Luxon

You can convert date strings and other date formats to a Luxon DateTime object. You can convert from standard formats and from arbitrary strings.

/// note | A difference between Luxon DateTime and JavaScript Date
With vanilla JavaScript, you can convert a string to a date with `new Date('2019-06-23')`. In Luxon, you must use a function explicitly stating the format, such as `DateTime.fromISO('2019-06-23')` or `DateTime.fromFormat("23-06-2019", "dd-MM-yyyy")`.
///
#### If you have a date in a supported standard technical format: 

Most dates use `fromISO()`. This creates a Luxon DateTime from an ISO 8601 string. For example:

=== "Expressions (JavaScript)"

	```js
	{{DateTime.fromISO('2019-06-23T00:00:00.00')}}
	```

=== "Code node (JavaScript)"

	```js
	let luxonDateTime = DateTime.fromISO('2019-06-23T00:00:00.00')
	```


Luxon's API documentation has more information on [fromISO](https://moment.github.io/luxon/api-docs/index.html#datetimefromiso){:target="_blank" .external-link}.

Luxon provides functions to handle conversions for a range of formats. Refer to Luxon's guide to [Parsing technical formats](https://moment.github.io/luxon/#/parsing?id=parsing-technical-formats) for details.

#### If you have a date as a string that doesn't use a standard format: 

Use Luxon's [Ad-hoc parsing](https://moment.github.io/luxon/#/parsing?id=ad-hoc-parsing){:target="_blank" .external-link}. To do this, use the `fromFormat()` function, providing the string and a set of [tokens](https://moment.github.io/luxon/#/parsing?id=table-of-tokens){:target="_blank" .external-link} that describe the format.

For example, you have n8n's founding date, 23rd June 2019, formatted as `23-06-2019`. You want to turn this into a Luxon object:

=== "Expressions (JavaScript)"

	```js
	{{DateTime.fromFormat("23-06-2019", "dd-MM-yyyy")}}
	```

=== "Code node (JavaScript)"

	```js
	let newFormat = DateTime.fromFormat("23-06-2019", "dd-MM-yyyy")
	```

When using ad-hoc parsing, note Luxon's warning about [Limitations](https://moment.github.io/luxon/#/parsing?id=limitations){:target="_blank" .external-link}. If you see unexpected results, try their [Debugging](https://moment.github.io/luxon/#/parsing?id=debugging){:target="_blank" .external-link} guide.

##### Get n days from today

Get a number of days before or after today. 

=== "Expressions (JavaScript)"

	For example, you want to set a field to always show the date seven days before the current date.

	In the expressions editor, enter:


	``` js
	{{$today.minus({days: 7})}}
	```

	On the 23rd June 2019, this returns `[Object: "2019-06-16T00:00:00.000+00:00"]`.

	This example uses n8n's custom variable `$today` for convenience. It's the equivalent of `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 }).minus({days: 7})`.

=== "Code node (JavaScript)"

	For example, you want a variable containing the date seven days before the current date.

	In the code editor, enter:

	``` js
	let sevenDaysAgo = $today.minus({days: 7})
	```

	On the 23rd June 2019, this returns `[Object: "2019-06-16T00:00:00.000+00:00"]`.

	This example uses n8n's custom variable `$today` for convenience. It's the equivalent of `DateTime.now().set({ hour: 0, minute: 0, second: 0, millisecond: 0 }).minus({days: 7})`.

For more detailed information and examples, refer to:

* Luxon's [guide to math](https://moment.github.io/luxon/#/math)
* Their API documentation on [DateTime plus](https://moment.github.io/luxon/api-docs/index.html#datetimeplus) and [DateTime minus](https://moment.github.io/luxon/api-docs/index.html#datetimeminus)

##### Create human-readable dates

In [Get n days from today](#get-n-days-from-today), the example gets the date seven days before the current date, and returns it as `[Object: "yyyy-mm-dd-T00:00:00.000+00:00"]` (for expressions) or `yyyy-mm-dd-T00:00:00.000+00:00` (in the Code node). To make this more readable, you can use Luxon's formatting functions.

For example, you want the field containing the date to be formatted as DD/MM/YYYY, so that on the 23rd June 2019, it returns `23/06/2019`.

This expression gets the date seven days before today, and converts it to the DD/MM/YYYY format.

=== "Expressions (JavaScript)"

	```js
	{{$today.minus({days: 7}).toLocaleString()}}
	```

=== "Code node (JavaScript)"

	```js
	let readableSevenDaysAgo = $today.minus({days: 7}).toLocaleString()
	```

You can alter the format. For example:

=== "Expressions (JavaScript)"

	```js
	{{$today.minus({days: 7}).toLocaleString({month: 'long', day: 'numeric', year: 'numeric'})}}
	```

	On 23rd June 2019, this returns "16 June 2019".

=== "Code node (JavaScript)"

	```js
	let readableSevenDaysAgo = $today.minus({days: 7}).toLocaleString({month: 'long', day: 'numeric', year: 'numeric'})
	```

	On 23rd June 2019, this returns "16 June 2019".

Refer to Luxon's guide on [toLocaleString (strings for humans)](https://moment.github.io/luxon/#/formatting?id=tolocalestring-strings-for-humans){:target="_blank" .external-link} for more information.


##### Get the time between two dates

To get the time between two dates, use Luxon's diffs feature. This subtracts one date from another and returns a duration.

For example, get the number of months between two dates:

=== "Expressions (JavaScript)"

	```js
	{{DateTime.fromISO('2019-06-23').diff(DateTime.fromISO('2019-05-23'), 'months').toObject()}}
	```

	This returns `[Object: {"months":1}]`.

=== "Code node (JavaScript)"

	```js
	let monthsBetweenDates = DateTime.fromISO('2019-06-23').diff(DateTime.fromISO('2019-05-23'), 'months').toObject()
	```

	This returns `{"months":1}`.

Refer to Luxon's [Diffs](https://moment.github.io/luxon/#/math?id=diffs){:target=_blank .external-link} for more information.

##### A longer example: How many days to Christmas?

This example brings together several Luxon features, uses JMESPath, and does some basic string manipulation. 

The scenario: you want a countdown to 25th December. Every day, it should tell you the number of days remaining to Christmas. You don't want to update it for next year - it needs to seamlessly work for every year.

=== "Expressions (JavaScript)"

	```js
	{{"There are " + $today.diff(DateTime.fromISO($today.year + '-12-25'), 'days').toObject().days.toString().substring(1) + " days to Christmas!"}}
	```

	This outputs `"There are <number of days> days to Christmas!"`. For example, on 9th March, it outputs "There are 291 days to Christmas!".

	A detailed explanation of what the expression does:

	* `{{`: indicates the start of the expression.
	* `"There are "`: a string. 
	* `+`: used to join two strings.
	* `$today.diff()`: This is similar to the example in [Get the time between two dates](#get-the-time-between-two-dates), but it uses n8n's custom `$today` variable.
	* `DateTime.fromISO($today.year + '-12-25'), 'days'`: this part gets the current year using `$today.year`, turns it into an ISO string along with the month and date, and then takes the whole ISO string and converts it to a Luxon DateTime data structure. It also tells Luxon that you want the duration in days.
	* `toObject()` turns the result of diff() into a more usable object. At this point, the expression returns `[Object: {"days":-<number-of-days>}]`. For example, on 9th March, `[Object: {"days":-291}]`.
	* `.days` uses JMESPath syntax to retrieve just the number of days from the object. For more information on using JMESPath with n8n, refer to our [JMESpath](/code/cookbook/jmespath.md) documentation. This gives you the number of days to Christmas, as a negative number.
	* `.toString().substring(1)` turns the number into a string and removes the `-`.
	* `+ " days to Christmas!"`: another string, with a `+` to join it to the previous string.
	* `}}`: indicates the end of the expression.

=== "Code node (JavaScript)"

	```js
	let daysToChristmas = "There are " + $today.diff(DateTime.fromISO($today.year + '-12-25'), 'days').toObject().days.toString().substring(1) + " days to Christmas!";
	```

	This outputs `"There are <number of days> days to Christmas!"`. For example, on 9th March, it outputs "There are 291 days to Christmas!".

	A detailed explanation of what the code does:

	* `"There are "`: a string. 
	* `+`: used to join two strings.
	* `$today.diff()`: This is similar to the example in [Get the time between two dates](#get-the-time-between-two-dates), but it uses n8n's custom `$today` variable.
	* `DateTime.fromISO($today.year + '-12-25'), 'days'`: this part gets the current year using `$today.year`, turns it into an ISO string along with the month and date, and then takes the whole ISO string and converts it to a Luxon DateTime data structure. It also tells Luxon that you want the duration in days.
	* `toObject()` turns the result of diff() into a more usable object. At this point, the expression returns `[Object: {"days":-<number-of-days>}]`. For example, on 9th March, `[Object: {"days":-291}]`.
	* `.days` uses JMESPath syntax to retrieve just the number of days from the object. For more information on using JMESPath with n8n, refer to our [JMESpath](/code/cookbook/jmespath.md) documentation. This gives you the number of days to Christmas, as a negative number.
	* `.toString().substring(1)` turns the number into a string and removes the `-`.
	* `+ " days to Christmas!"`: another string, with a `+` to join it to the previous string.


---



## Expressions {#expressions}

*Source: docs/code/expressions.md*


##### Expressions

Expressions are a powerful feature implemented in all n8n nodes. They allow node parameters to be set dynamically based on data from:

- Previous node executions
- The workflow
- Your n8n environment

You can also execute JavaScript within an expression, making this a convenient and easy way to manipulate data into useful parameter values without writing extensive extra code.

n8n created and uses a templating language called [Tournament](https://github.com/n8n-io/tournament){:target=_blank .external-link}, and extends it with [custom methods and variables](/code/builtin/overview.md) and [data transformation functions](/code/builtin/data-transformation-functions/index.md). These features make it easier to perform common tasks like getting data from other nodes or accessing workflow metadata.

n8n additionally supports two libraries:

- [Luxon](https://github.com/moment/luxon/){:target=_blank .external-link}, for working with dates and time.
- [JMESPath](https://jmespath.org/){:target=_blank .external-link}, for querying JSON.

/// note | Data in n8n
When writing expressions, it's helpful to understand data structure and behavior in n8n. Refer to [Data](/data/index.md) for more information on working with data in your workflows.
///

#### Writing expressions

To use an expression to set a parameter value:

1. Hover over the parameter where you want to use an expression.
2. Select **Expressions** in the **Fixed/Expression** toggle.
3. Write your expression in the parameter, or select **Open expression editor** <span class="inline-image">![Open expressions editor icon](/_images/common-icons/open-expression-editor.png){.off-glb}</span> to open the expressions editor. If you use the expressions editor, you can browse the available data in the **Variable selector**. All expressions have the format `{{ your expression here }}`.


##### Example: Get data from webhook body

Consider the following scenario: you have a webhook trigger that receives data through the webhook body. You want to extract some of that data for use in the workflow.

Your webhook data looks similar to this:


```json
[
  {
    "headers": {
      "host": "n8n.instance.address",
      ...
    },
    "params": {},
    "query": {},
    "body": {
      "name": "Jim",
      "age": 30,
      "city": "New York"
    }
  }
]
```


In the next node in the workflow, you want to get just the value of `city`. You can use the following expression:


```js
{{$json.body.city}}
```

This expression:

1. Accesses the incoming JSON-formatted data using n8n's custom `$json` variable.
2. Finds the value of `city` (in this example, "New York"). Note that this example uses JMESPath syntax to query the JSON data. You can also write this expression as `{{$json['body']['city']}}`.


##### Example: Writing longer JavaScript

An expression contains one line of JavaScript. This means you cannot do things like variable assignments or multiple standalone operations.

To understand the limitations of JavaScript in expressions, and start thinking about workarounds, look at the following two pieces of code. Both code examples use the Luxon date and time library to find the time between two dates in months, and encloses the code in handlebar brackets, like an expression.

However, the first example isn't a valid n8n expression:

```js
// This example is split over multiple lines for readability
// It's still invalid when formatted as a single line
{{
  function example() {
    let end = DateTime.fromISO('2017-03-13');
    let start = DateTime.fromISO('2017-02-13');
    let diffInMonths = end.diff(start, 'months');
    return diffInMonths.toObject();
  }
  example();
}}
```

While the second example is valid:

```js
{{DateTime.fromISO('2017-03-13').diff(DateTime.fromISO('2017-02-13'), 'months').toObject()}}
```

#### Common issues

For common errors or issues with expressions and suggested resolution steps, refer to [Common Issues](/code/cookbook/expressions/common-issues.md).


---



## Index {#index}

*Source: docs/code/index.md*


##### Code in n8n

n8n is a low-code tool. This means you can do a lot without code, then add code when needed.

#### Code in your workflows

There are two places in your workflows where you can use code:

<div class="grid-cards-vertical cards" markdown>

- __Expressions__

	Use [expressions](/glossary.md#expression-n8n) to transform [data](/data/index.md) in your nodes. You can use JavaScript in expressions, as well as n8n's [Built-in methods and variables](/code/builtin/overview.md) and [Data transformation functions](/code/builtin/data-transformation-functions/index.md).

	[:octicons-arrow-right-24: Expressions](/code/expressions.md)

- __Code node__

	Use the Code node to add JavaScript or Python to your workflow.

	[:octicons-arrow-right-24: Code node](/code/code-node.md)

</div>


#### Other technical resources

These are features that are relevant to technical users.

##### Technical nodes

n8n provides core nodes, which simplify adding key functionality such as API requests, webhooks, scheduling, and file handling.

<div class="grid-cards-vertical cards" markdown>

- __Write a backend__

	The [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md), [Webhook](/integrations/builtin/core-nodes/n8n-nodes-base.webhook/index.md), and [Code](/code/code-node.md) nodes help you make API calls, respond to webhooks, and write any JavaScript in your workflow.

	Use this do things like [Create an API endpoint](https://n8n.io/workflows/1750-creating-an-api-endpoint/){:target=_blank .external-link}.

	[:octicons-arrow-right-24: Core nodes](/integrations/builtin/core-nodes/index.md)

- __Represent complex logic__

	You can build complex flows, using nodes like [If](/integrations/builtin/core-nodes/n8n-nodes-base.if.md), [Switch](/integrations/builtin/core-nodes/n8n-nodes-base.switch.md), and [Merge](/integrations/builtin/core-nodes/n8n-nodes-base.merge.md) nodes. 

	[:octicons-arrow-right-24: Flow logic](/flow-logic/index.md)

</div>

##### Other developer resources

<div class="grid-cards-vertical cards" markdown>

- __The n8n API__

	n8n provides an API, where you can programmatically perform many of the same tasks as you can in the GUI. There's an [n8n API node](/integrations/builtin/core-nodes/n8n-nodes-base.n8n.md) to access the API in your workflows.

	[:octicons-arrow-right-24: API](/api/index.md)

- __Self-host__

	You can self-host n8n. This keeps your data on your own infrastructure.

	[:octicons-arrow-right-24: Hosting](/hosting/index.md)

- __Build your own nodes__

	You can build custom nodes, install them on your n8n instance, and publish them to [npm](https://www.npmjs.com/){:target=_blank .external-link}.

	[:octicons-arrow-right-24: Creating nodes](/integrations/creating-nodes/overview.md)

</div>


---



## Index {#index}

*Source: docs/courses/index.md*


##### Text courses

If you've found your way here, it means you're serious about your interest in automation. Maybe you're tired of manually entering data into the same spreadsheet every day, of clicking through a series of tabs and buttons for that one piece of information you need, of managing tens of different tools and systems.

Whatever the reason, one thing is clear: you shouldn't spend precious time doing things that don't spark joy or contribute to your personal and professional growth.

These tasks can and should be automated! And you don't need advanced technical knowledge or excellent coding skills to do this–with no-code tools like n8n, automation is for everyone.

#### Available courses

- [Level 1: Beginner course](/courses/level-one/index.md)
- [Level 2: Intermediate course](/courses/level-two/index.md)


---



## Index {#index}

*Source: docs/courses/level-one/index.md*


<!-- vale from-microsoft.We = NO -->
<!-- vale from-microsoft.FirstPerson = NO -->
##### Level one: Introduction

Welcome to the **n8n Course Level 1**!

#### Is this course right for me?

This course introduces you to the fundamental concepts within n8n and develops your low-code automation expertise.

This course is for you if you:

- Are starting to use n8n for the first time.
- Are looking for some extra help creating your first workflow.
- Want to automate processes in your personal or working life.

This course introduces n8n concepts and demonstrates practical workflow building without assuming any prior familiarity with n8n. If you'd like to get a feel for the basics without as much explanation, consult our [quickstart guide](/try-it-out/tutorial-first-workflow.md).

#### What will I learn in this course?

We believe in learning by doing. You can expect some theoretical information about the basic concepts and components of n8n, followed by practice of building workflows step by step.

By the end of this course you will know:

- How to set up n8n and navigate the Editor UI.
- How n8n structures data.
- How to configure different node parameters and add credentials.
- When and how to use conditional logic in workflows.
- How to schedule and control workflows.
- How to import, download, and share workflows with others.

You will build two workflows:

- A two-node workflow to get articles from Hacker News
- A seven-node workflow to help your client get records from a data warehouse, filter them, make calculations, and notify team members about the results

#### What do I need to get started?

1. **n8n set up**: You can use [n8n Cloud](/manage-cloud/overview.md) (or the [self-hosted version](/hosting/installation/docker.md) if you have experience hosting services).
2. **A course user ID**: [Sign up here](https://n8n-community.typeform.com/to/PDEMrevI) to get your unique ID and other credentials you will need in the course.
3. Basic knowledge of JavaScript and [APIs](https://blog.n8n.io/what-are-apis-how-to-use-them-with-no-code/) would be helpful, but isn't necessary.
4. An [account on the n8n community forum](https://community.n8n.io/) if you wish to receive a profile badge and avatar upon successful completion.

#### How long does the course take?

Completing the course should take around **two hours**. You don't have to complete it in one go; feel free to take breaks and resume whenever you are ready.

#### How do I complete the course?

There are two milestones in this course that test your knowledge of what you have learned in the lessons:

- [x] Building the [main workflow](/courses/level-one/chapter-5/chapter-5.1.md)
- [x] Passing the [quiz](https://n8n-community.typeform.com/to/JMoBXeGA) at the end of the course

/// note | Check your progress
You can always **check your progress** throughout the course by entering your unique ID [here](https://internal.users.n8n.cloud/webhook/course-level-1/verify).
///

If you complete the milestones above, you will get [**a badge and an avatar**](https://community.n8n.io/badges/104/completed-n8n-course-level-1) in your forum profile. You can then share your profile and course verification ID to showcase your n8n skills to others.

[Let's get started!](/courses/level-one/chapter-1.md){ .md-button }


---



## Index {#index}

*Source: docs/courses/level-two/index.md*


##### Level two: Introduction

Welcome to the **n8n Course Level 2**!


#### Is this course right for me?

This course is for you if you:

- Want to automate somewhat complex business processes.
- Want to dive deeper into n8n after taking the [Level 1 course](/courses/level-one/index.md).

#### What will I learn in this course?

The focus in this course is on working with data. You will learn how to:

- Use the data structure of n8n correctly.
- Process different data types (for example, XML, HTML, date, time, and binary data).
- Merge data from different sources (for example, a database, spreadsheet, or CRM).
- Use functions and JavaScript code in the [Code node](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md).
- Deal with error workflows and workflow errors.

You will learn all this by completing short practical exercises after the theoretical explanations and building a business workflow following instructions.

#### What do I need to get started?

To follow along this course (at a comfortable pace) you will need the following:

- **n8n set up**: You can use the [self-hosted version](/hosting/installation/npm.md) or [n8n Cloud](/manage-cloud/overview.md).
- **A user ID**: [Sign up here](https://n8n-community.typeform.com/to/HQoQ7nXg){:target="_blank" .external-link} to get your unique ID and other credentials you will need in the course.
- **Basic n8n skills**: We strongly recommend taking the [Level 1 course](/courses/level-one/index.md) before this one.
- **Basic JavaScript understanding**

#### How long does the course take?

Completing the course should take around **two hours**. You don't have to complete it in one go; feel free to take breaks and resume whenever you are ready.

#### How do I complete the course?

There are two milestones in this course that test your knowledge of what you have learned in the lessons:

- [x] Building the [main workflow](/courses/level-two/chapter-5/chapter-5.0.md)
- [x] Passing the [quiz](https://n8n-community.typeform.com/to/r9hDbytg){:target="_blank" .external} at the end of the course

You can always **check your progress** throughout the course by entering your unique ID [here](https://internal.users.n8n.cloud/webhook/course-level-2/verify){:target="_blank" .external-link}.

If you successfully complete the milestones above, you will get [**a badge and an avatar**](https://community.n8n.io/badges/105/completed-n8n-course-level-2){:target="_blank" .external} in your forum profile. You can then share your profile and course verification ID to showcase your n8n skills to others.

[Let's get started!](/courses/level-two/chapter-1.md){ .md-button }


---



## Index {#index}

*Source: docs/credentials/index.md*


##### Credentials

[Credentials](/glossary.md#credential-n8n) are private pieces of information issued by apps and services to authenticate you as a user and allow you to connect and share information between the app or service and the n8n node.

Access the credentials UI by opening the left menu and selecting **Credentials**. n8n lists credentials you created on the **My credentials** tab. The **All credentials** tab shows all credentials you can use, included credentials shared with you by other users.

* [Create and edit credentials](/credentials/add-edit-credentials.md).
* Learn about [credential sharing](/credentials/credential-sharing.md).
* Find information on setting up credentials for your services in the [credentials library](/integrations/builtin/credentials/index.md).




---



## Index {#index}

*Source: docs/data/data-mapping/data-item-linking/index.md*


##### Data item linking

An item is a single piece of data. Nodes receive one or more items, operate on them, and output new items. Each item links back to previous items. 

You need to understand this behavior if you're:

* Building a programmatic-style node that implements complex behaviors with its input and output data.
* Using the Code node or expressions editor to access data from earlier items in the workflow. 
* Using the Code node for complex behaviors with input and output data.

This section provides:

* A conceptual overview of [Item linking concepts](/data/data-mapping/data-item-linking/item-linking-concepts.md). 
* Information on [Item linking for node creators](/data/data-mapping/data-item-linking/item-linking-node-building.md).
* Support for end users who need to [Work with the data path](/data/data-mapping/data-item-linking/item-linking-code-node.md) to retrieve item data from previous nodes, and link items when using the Code node.
* Guidance on troubleshooting [Errors](/data/data-mapping/data-item-linking/item-linking-errors.md).




---



## Index {#index}

*Source: docs/data/data-mapping/index.md*


##### Data mapping

Data mapping means referencing data from previous nodes. 

This section contains guidance on:

* Mapping data in most scenarios: [Data mapping in the UI](/data/data-mapping/data-mapping-ui.md) and [Data mapping in expression](/data/data-mapping/data-mapping-expressions.md)
* How to handle [item linking](/data/data-mapping/data-item-linking/index.md) when using the Code node or building your own nodes. 


---



## Index {#index}

*Source: docs/data/index.md*


##### Data

Data is the information that n8n nodes receive and process. For basic usage of n8n you don't need to understand data structures and manipulation. However, it becomes important if you want to:

 - Create your own node
 - Write custom [expressions](/glossary.md#expression-n8n)
 - Use the Function or Function Item node

This section covers: 

* [Data structure](/data/data-structure.md)
* [Data flow within nodes](/data/data-flow-nodes.md)
* [Transforming data](/data/transforming-data.md)
* [Process data using code](/data/code.md)
* [Pinning](/data/data-pinning.md) and [editing](/data/data-editing.md) data during workflow development.
* [Data mapping](/data/data-mapping/index.md) and [Item linking](/data/data-mapping/data-item-linking/index.md): how data items link to each other.

#### Related resources

##### Data transformation nodes

n8n provides a collection of nodes to transform data:

* [Aggregate](/integrations/builtin/core-nodes/n8n-nodes-base.aggregate.md): take separate items, or portions of them, and group them together into individual items.
* [Limit](/integrations/builtin/core-nodes/n8n-nodes-base.aggregate.md): remove items beyond a defined maximum number.
* [Remove Duplicates](/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/index.md): identify and delete items that are identical across all fields or a subset of fields.
* [Sort](/integrations/builtin/core-nodes/n8n-nodes-base.sort.md): organize lists of in a desired ordering, or generate a random selection.
* [Split Out](/integrations/builtin/core-nodes/n8n-nodes-base.splitout.md): separate a single data item containing a list into multiple items.
* [Summarize](/integrations/builtin/core-nodes/n8n-nodes-base.summarize.md): aggregate items together, in a manner similar to Excel pivot tables. 


---



## Index {#index}

*Source: docs/embed/index.md*


##### n8n Embed

n8n Embed is part of n8n's paid offering. Using Embed, you can white label n8n, or incorporate it in your software as part of your commercial product.

For more information about when to use Embed, as well as costs and licensing processes, refer to [Embed](https://n8n.io/embed/){:target=_blank .external-link} on the n8n website.

#### Support

The [community forum](https://community.n8n.io/) can help with various issues. If you are a current Embed customer, you can also contact n8n support, using the email provided when you bought the license.

#### Russia and Belarus

n8n Embed isn't available in Russia and Belarus. Refer to n8n's blog post [Update on n8n cloud accounts in Russia and Belarus](https://blog.n8n.io/update-on-n8n-cloud-accounts-in-russia-and-belarus/){:target=_blank .external-link} for more information.


---



## Workflow Templates {#workflow-templates}

*Source: docs/embed/workflow-templates.md*


##### Workflow templates

--8<-- "_snippets/embed-license.md"

n8n provides a library of workflow [templates](/glossary.md#template-n8n). When embedding n8n, you can:

* Continue to use n8n's workflow templates library (this is the default behavior)
* Disable workflow templates
* Create your own workflow templates library

#### Disable workflow templates

--8<-- "_snippets/workflows/templates/disable-templates.md"

#### Use your own workflow templates library

--8<-- "_snippets/workflows/templates/custom-templates-library.md"

#### Add your workflows to the n8n library

--8<-- "_snippets/workflows/templates/submit-templates.md"



---



## Index {#index}

*Source: docs/flow-logic/index.md*


##### Flow logic

n8n allows you to represent complex logic in your workflows.

[[% import "_macros/section-toc.html" as sectionToc %]]

This section covers:

[[ sectionToc.sectionToc(page) ]]

#### Related sections

You need some understanding of [Data](/data/index.md) in n8n, including [Data structure](/data/data-structure.md) and [Data flow within nodes](/data/data-flow-nodes.md).

When building your logic, you'll use n8n's [Core nodes](/integrations/builtin/core-nodes/index.md), including:

* Splitting: [IF](/integrations/builtin/core-nodes/n8n-nodes-base.if.md) and [Switch](/integrations/builtin/core-nodes/n8n-nodes-base.switch.md).
* Merging: [Merge](/integrations/builtin/core-nodes/n8n-nodes-base.merge.md), [Compare Datasets](/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets.md), and [Code](/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md).
* Looping: [IF](/integrations/builtin/core-nodes/n8n-nodes-base.if.md) and [Loop Over Items](/integrations/builtin/core-nodes/n8n-nodes-base.splitinbatches.md).
* Waiting: [Wait](/integrations/builtin/core-nodes/n8n-nodes-base.wait.md).
* Creating sub-workflows: [Execute Workflow](/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflow.md) and [Execute Workflow Trigger](/integrations/builtin/core-nodes/n8n-nodes-base.executeworkflowtrigger.md).
* Error handling: [Stop And Error](/integrations/builtin/core-nodes/n8n-nodes-base.stopanderror.md) and [Error Trigger](/integrations/builtin/core-nodes/n8n-nodes-base.errortrigger.md).


---



## Index {#index}

*Source: docs/hosting/configuration/configuration-examples/index.md*


##### Configuration examples

This section contains examples for how to configure n8n to solve particular use cases.

[[% import "_macros/section-toc.html" as sectionToc %]]

[[ sectionToc.sectionToc(page) ]]


---



## Index {#index}

*Source: docs/hosting/configuration/environment-variables/index.md*


##### Environment variables overview

This section lists the environment variables that you can use to change n8n's configuration settings when self-hosting n8n.

/// note | File-based configuration
You can provide a [configuration file](/hosting/configuration/configuration-methods.md) for n8n. You can also append `_FILE` to certain variables to provide their configuration in a separate file. 
///

[[% import "_macros/section-toc.html" as sectionToc %]]

[[ sectionToc.sectionToc(page) ]]


---



## Index {#index}

*Source: docs/hosting/index.md*


##### Self-hosting n8n

This section provides guidance on setting up n8n for both the Enterprise and Community self-hosted editions. The Community edition is free, the Enterprise edition isn't. 

See [Community edition features](/hosting/community-edition-features.md) for a list of available features. 

<div class="grid-cards-vertical cards" markdown>

- __Installation and server setups__

	Install n8n on any platform using npm or Docker. Or follow our guides to popular hosting platforms.

	[:octicons-arrow-right-24: Docker installation guide](/hosting/installation/docker.md)

- __Configuration__

	Learn how to configure n8n with environment variables.

	[:octicons-arrow-right-24: Environment Variables](/hosting/configuration/environment-variables/index.md)

- __Users and authentication__

	Choose and set up user authentication for your n8n instance.

	[:octicons-arrow-right-24: Authentication](/hosting/configuration/user-management-self-hosted.md)

- __Scaling__

	Manage data, modes, and processes to keep n8n running smoothly at scale.

	[:octicons-arrow-right-24: Scaling](/hosting/scaling/queue-mode.md)

- __Securing n8n__

	Secure your n8n instance by setting up SSL, SSO, or 2FA or blocking or opting out of some data collection or features.

	[:octicons-arrow-right-24: Securing n8n guide](/hosting/securing/overview.md)

- __Starter kits__

	New to n8n or AI? Try our Self-hosted AI Starter Kit. Curated by n8n, it combines the self-hosted n8n platform with compatible AI products and components to get you started building self-hosted AI workflows.

	[:octicons-arrow-right-24: Starter kits](/hosting/starter-kits/ai-starter-kit.md)

</div>

--8<-- "_snippets/self-hosting/warning.md"


---



## Index {#index}

*Source: docs/hosting/installation/server-setups/index.md*


##### Server setups

Self-host with Docker Compose:

* [Digital Ocean](/hosting/installation/server-setups/digital-ocean.md)
* [Heroku](/hosting/installation/server-setups/heroku.md)
* [Hetzner Cloud](/hosting/installation/server-setups/hetzner.md)

Starting points for a Kubernetes setup:

* [AWS](/hosting/installation/server-setups/aws.md)
* [Azure](/hosting/installation/server-setups/azure.md)
* [Google Cloud Platform](/hosting/installation/server-setups/google-cloud.md)

Configuration guides to help you get started on other platforms:

* [Docker Compose](/hosting/installation/server-setups/docker-compose.md)


---



## Index {#index}

*Source: docs/index.md*


##### Welcome to n8n Docs


This is the documentation for [n8n](https://n8n.io/){:target=_blank .external-link}, a [fair-code](https://faircode.io){:target=_blank .external-link} licensed workflow automation tool that combines AI capabilities with business process automation.

It covers everything from setup to usage and development. It's a work in progress and all [contributions](/help-community/contributing.md) are welcome.


#### Where to start

<div class="grid cards" markdown>

-   __Quickstarts__

    Jump in with n8n's quickstart guides.

    [:octicons-arrow-right-24: Try it out](/try-it-out/index.md)

-   __Choose the right n8n for you__

	Cloud, npm, self-host . . . 

    [:octicons-arrow-right-24: Options](/choose-n8n.md)


-   __Explore integrations__

    Browse n8n's integrations library.

    [:octicons-arrow-right-24: Find your apps](/integrations/index.md)

-   __Build AI functionality__

    n8n supports building AI functionality and tools.

    [:octicons-arrow-right-24: Advanced AI](/advanced-ai/index.md)    
</div>

#### About n8n

n8n (pronounced n-eight-n) helps you to connect any app with an API with any other, and manipulate its data with little or no code.

* Customizable: highly flexible workflows and the option to build custom nodes.
* Convenient: use the npm or Docker to try out n8n, or the Cloud hosting option if you want us to handle the infrastructure.
* Privacy-focused: self-host n8n for privacy and security.


---



## Index {#index}

*Source: docs/integrations/builtin/app-nodes/index.md*


##### Actions library

This section provides information about n8n's Actions.



---



## Index {#index}

*Source: docs/integrations/builtin/app-nodes/n8n-nodes-base.airtable/index.md*


##### Airtable node

Use the Airtable node to automate work in Airtable, and integrate Airtable with other applications. n8n has built-in support for a wide range of Airtable features, including creating, reading, listing, updating and deleting tables.

On this page, you'll find a list of operations the Airtable node supports and links to more resources.

/// note | Credentials
Refer to [Airtable credentials](/integrations/builtin/credentials/airtable.md) for guidance on setting up authentication. 
///

#### Operations

* Append the data to a table
* Delete data from a table
* List data from a table
* Read data from a table
* Update data in a table

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'airtable') ]]

#### Related resources

n8n provides a trigger node for Airtable. You can find the trigger node docs [here](/integrations/builtin/trigger-nodes/n8n-nodes-base.airtabletrigger.md).

Refer to [Airtable's documentation](https://airtable.com/developers/web/api/introduction){:target=_blank .external-link} for more information about the service.

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"


#### Node reference

##### Get the Record ID

To fetch data for a particular record, you need the Record ID. There are two ways to get the Record ID.

##### Create a Record ID column in Airtable

To create a `Record ID` column in your table, refer to this [article](https://support.airtable.com/docs/finding-airtable-ids){:target=_blank .external-link}. You can then use this Record ID in your Airtable node.

##### Use the List operation

To get the Record ID of your record, you can use the **List** operation of the Airtable node. This operation will return the Record ID along with the fields. You can then use this Record ID in your Airtable node.

##### Filter records when using the List operation

To filter records from your Airtable base, use the **Filter By Formula** option. For example, if you want to return all the users that belong to the organization `n8n`, follow the steps mentioned below:

1. Select 'List' from the **Operation** dropdown list.
2. Enter the base ID and the table name in the **Base ID** and **Table** field, respectively.
3. Click on **Add Option** and select 'Filter By Formula' from the dropdown list.
4. Enter the following formula in the **Filter By Formula** field: `{Organization}='n8n'`.

Similarly, if you want to return all the users that don't belong to the organization `n8n`, use the following formula: `NOT({Organization}='n8n')`.

Refer to the Airtable [documentation](https://support.airtable.com/hc/en-us/articles/203255215-Formula-Field-Reference){:target=_balnk .external-link} to learn more about the formulas.

#### Common issues

For common errors or issues and suggested resolution steps, refer to [Common Issues](/integrations/builtin/app-nodes/n8n-nodes-base.airtable/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/builtin/app-nodes/n8n-nodes-base.discord/index.md*


##### Discord node

Use the Discord node to automate work in Discord, and integrate Discord with other applications. n8n has built-in support for a wide range of Discord features, including sending messages in a Discord channel and managing channels.

On this page, you'll find a list of operations the Discord node supports and links to more resources.

/// note | Credentials
Refer to [Discord credentials](/integrations/builtin/credentials/discord.md) for guidance on setting up authentication. 
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

#### Operations
<!-- vale off -->
<!-- "Many" triggers warnings -->

- Channel
	- Create
	- Delete
	- Get
	- Get Many
	- Update
- Message
	- Delete
	- Get
	- Get Many
	- React with Emoji
	- Send
	* Send and Wait for Response
- Member
	- Get Many
	- Role Add
	- Role Remove

--8<-- "_snippets/integrations/builtin/send-and-wait-operation.md"

<!-- vale on -->

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'discord') ]]

#### Related resources

Refer to [Discord's documentation](https://discord.com/developers/docs/intro){:target=_blank .external-link} for more information about the service.

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

#### Common issues

For common errors or issues and suggested resolution steps, refer to [Common Issues](/integrations/builtin/app-nodes/n8n-nodes-base.discord/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/builtin/app-nodes/n8n-nodes-base.gmail/index.md*


##### Gmail node

Use the Gmail node to automate work in Gmail, and integrate Gmail with other applications. n8n has built-in support for a wide range of Gmail features, including creating, updating, deleting, and getting drafts, messages, labels, thread.  

On this page, you'll find a list of operations the Gmail node supports and links to more resources.

/// note | Credentials
Refer to [Google credentials](/integrations/builtin/credentials/google/index.md) for guidance on setting up authentication. 
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

#### Operations

* **Draft**
	* [**Create**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations.md#create-a-draft) a draft
	* [**Delete**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations.md#delete-a-draft) a draft
	* [**Get**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations.md#get-a-draft) a draft
	* [**Get Many**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/draft-operations.md#get-many-drafts) drafts
* **Label**
	* [**Create**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/label-operations.md#create-a-label) a label
	* [**Delete**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/label-operations.md#delete-a-label) a label
	* [**Get**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/label-operations.md#get-a-label) a label
	* [**Get Many**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/label-operations.md#get-many-labels) labels
* **Message**
	* [**Add Label**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md#add-label-to-a-message) to a message
	* [**Delete**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md#delete-a-message) a message
	* [**Get**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md#get-a-message) a message
	* [**Get Many**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md#get-many-messages) messages
	* [**Mark as Read**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md#mark-as-read)
	* [**Mark as Unread**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md#mark-as-unread)
	* [**Remove Label**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md#remove-label-from-a-message) from a message
	* [**Reply**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md#reply-to-a-message) to a message
	* [**Send**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/message-operations.md#send-a-message) a message
* **Thread**
	* [**Add Label**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations.md#add-label-to-a-thread) to a thread
	* [**Delete**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations.md#delete-a-thread) a thread
	* [**Get**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations.md#get-a-thread) a thread
	* [**Get Many**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations.md#get-many-threads) threads
	* [**Remove Label**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations.md#remove-label-from-a-thread) from thread
	* [**Reply**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations.md#reply-to-a-message) to a message
	* [**Trash**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations.md#trash-a-thread) a thread
	* [**Untrash**](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/thread-operations.md#untrash-a-thread) a thread

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'gmail') ]]

#### Related resources

Refer to Google's [Gmail API documentation](https://developers.google.com/gmail/api) for detailed information about the API that this node integrates with.

n8n provides a trigger node for Gmail. You can find the trigger node docs [here](/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/index.md).

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

#### Common issues

For common errors or issues and suggested resolution steps, refer to [Common Issues](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/index.md*


##### Google Calendar node

Use the Google Calendar node to automate work in Google Calendar, and integrate Google Calendar with other applications. n8n has built-in support for a wide range of Google Calendar features, including adding, retrieving, deleting and updating calendar events.

On this page, you'll find a list of operations the Google Calendar node supports and links to more resources.

/// note | Credentials
Refer to [Google Calendar credentials](/integrations/builtin/credentials/google/index.md) for guidance on setting up authentication. 
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

#### Operations

* **Calendar**
    * [**Availability**](/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/calendar-operations.md#availability): If a time-slot is available in a calendar
* **Event**
    * [**Create**](/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations.md#create): Add an event to calendar
    * [**Delete**](/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations.md#delete): Delete an event
    * [**Get**](/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations.md#get): Retrieve an event
    * [**Get Many**](/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations.md#get-many): Retrieve all events from a calendar
    * [**Update**](/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/event-operations.md#update): Update an event

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'google-calendar') ]]

#### Related resources

n8n provides a trigger node for Google Calendar. You can find the trigger node docs [here](/integrations/builtin/trigger-nodes/n8n-nodes-base.googlecalendartrigger.md).

Refer to [Google Calendar's documentation](https://developers.google.com/calendar/api/v3/reference){:target=_blank .external-link} for more information about the service.

View [example workflows and related content](https://n8n.io/integrations/google-calendar/){:target=_blank .external-link} on n8n's website.


---



## Index {#index}

*Source: docs/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/index.md*


##### Google Drive node

Use the Google Drive node to automate work in Google Drive, and integrate Google Drive with other applications. n8n has built-in support for a wide range of Google Drive features, including creating, updating, listing, deleting, and getting drives, files, and folders. 

On this page, you'll find a list of operations the Google Drive node supports and links to more resources.

/// note | Credentials
Refer to [Google Drive credentials](/integrations/builtin/credentials/google/index.md) for guidance on setting up authentication. 
///

#### Operations

* **File**
    * [**Copy**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md#copy-a-file) a file
    * [**Create from text**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md#create-from-text)
    * [**Delete**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md#delete-a-file) a file
    * [**Download**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md#download-a-file) a file
    * [**Move**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md#move-a-file) a file
    * [**Share**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md#share-a-file) a file
    * [**Update**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md#update-a-file) a file
    * [**Upload**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-operations.md#upload-a-file) a file
* **File/Folder**
    * [**Search**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/file-folder-operations.md#search-files-and-folders) files and folders
* **Folder**
    * [**Create**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/folder-operations.md#create-a-folder) a folder
    * [**Delete**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/folder-operations.md#delete-a-folder) a folder
    * [**Share**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/folder-operations.md#share-a-folder) a folder
* **Shared Drive**
    * [**Create**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations.md#create-a-shared-drive) a shared drive
    * [**Delete**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations.md#delete-a-shared-drive) a shared drive
    * [**Get**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations.md#get-a-shared-drive) a shared drive
    * [**Get Many**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations.md#get-many-shared-drives) shared drives
    * [**Update**](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/shared-drive-operations.md#update-a-shared-drive) a shared drive

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'google-drive') ]]

#### Common issues

For common questions or issues and suggested solutions, refer to [Common issues](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/common-issues.md).

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"


---



## Index {#index}

*Source: docs/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/index.md*


##### Google Sheets

Use the Google Sheets node to automate work in Google Sheets, and integrate Google Sheets with other applications. n8n has built-in support for a wide range of Google Sheets features, including creating, updating, deleting, appending, removing and getting documents. 

On this page, you'll find a list of operations the Google Sheets node supports and links to more resources.

/// note | Credentials
Refer to [Google Sheets credentials](/integrations/builtin/credentials/google/index.md) for guidance on setting up authentication. 
///

#### Operations

* **Document**
    * [**Create**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations.md#create-a-spreadsheet) a spreadsheet.
	* [**Delete**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/document-operations.md#delete-a-spreadsheet) a spreadsheet.
* **Sheet Within Document**
	* [**Append or Update Row**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md#append-or-update-row): Append a new row, or update the current one if it already exists.
	* [**Append Row**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md#append-row): Create a new row.
	* [**Clear**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md#clear-a-sheet) all data from a sheet.
	* [**Create**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md#create-a-new-sheet) a new sheet.
	* [**Delete**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md#delete-a-sheet) a sheet.
	* [**Delete Rows or Columns**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md#delete-rows-or-columns): Delete columns and rows from a sheet.
	* [**Get Row(s)**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md#get-rows): Read all rows in a sheet.
	* [**Update Row**](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/sheet-operations.md#update-row): Update a row in a sheet. 


#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'google-sheets') ]]

#### Related resources

Refer to [Google Sheet's API documentation](https://developers.google.com/sheets/api){:target=_blank .external-link} for more information about the service.

<!-- ## Examples
This example uses the Customer Datastore node to provide sample data to load into Google Sheets. It assumes you've already set up your [credentials](/integrations/builtin/credentials/google/index.md).	
	1. Set up a Google Sheet with two columns, `test1` and `test`. In `test1`, enter the names from the Customer Datastore node:  
	![The spreadsheet set up for testing](/_images/integrations/builtin/app-nodes/googlesheets/test-sheet-before.png)  
	2. Create the workflow: use the manual trigger, Customer Datastore, and Google Sheets nodes.  
	![The spreadsheet set up for testing](/_images/integrations/builtin/app-nodes/googlesheets/workflow.png)  
	3. Open the Customer Datastore node, enable **Return All**, then select **Execute step**.
	4. In the Google Sheets node, go through the steps above, using these settings:
		* Select **Update Row** as the **Operation**.
		* In **Column to Match On**, select `test1`.
		* For the first field of **Values to Update**, drag in the **name** from the input view.
		* For the second field of **Values to Update**, drag in the **email** from the input view.
	5. Select **Execute step**.
	6. View your spreadsheet. **test2** should now contain the email addresses that match to the names in the input data.  
	![The spreadsheet set up for testing](/_images/integrations/builtin/app-nodes/googlesheets/test-sheet-after.png)   -->

#### Common issues

For common questions or issues and suggested solutions, refer to [Common issues](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/common-issues.md).

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"


---



## Index {#index}

*Source: docs/integrations/builtin/app-nodes/n8n-nodes-base.mysql/index.md*


##### MySQL node

Use the MySQL node to automate work in MySQL, and integrate MySQL with other applications. n8n has built-in support for a wide range of MySQL features, including executing an SQL query, as well as inserting, and updating rows in a database.

On this page, you'll find a list of operations the MySQL node supports and links to more resources.

/// note | Credentials
Refer to [MySQL credentials](/integrations/builtin/credentials/mysql.md) for guidance on setting up authentication. 
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

#### Operations

* Delete
* Execute SQL
* Insert
* Insert or Update
* Select
* Update

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'mysql') ]]

#### Related resources

Refer to [MySQL's Connectors and APIs documentation](https://dev.mysql.com/doc/index-connectors.html){:target=_blank .external-link} for more information about the service.

Refer to MySQL's [SELECT statement documentation](https://dev.mysql.com/doc/refman/8.4/en/select.html){:target=_blank .external-link} for more information on writing SQL queries.

#### Use query parameters

When creating a query to run on a MySQL database, you can use the **Query Parameters** field in the **Options** section to load data into the query. n8n sanitizes data in query parameters, which prevents SQL injection.

For example, you want to find a person by their email address. Given the following input data:

```js
[
    {
        "email": "alex@example.com",
        "name": "Alex",
        "age": 21 
    },
    {
        "email": "jamie@example.com",
        "name": "Jamie",
        "age": 33 
    }
]
```

You can write a query like:

```sql
SELECT * FROM $1:name WHERE email = $2;
```

Then in **Query Parameters**, provide the field values to use. You can provide fixed values or expressions. For this example, use expressions so the node can pull the email address from each input item in turn:

```js
// users is an example table name
users, {{ $json.email }} 
```

#### Common issues

For common errors or issues and suggested resolution steps, refer to [Common issues](/integrations/builtin/app-nodes/n8n-nodes-base.mysql/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/builtin/app-nodes/n8n-nodes-base.notion/index.md*


##### Notion node

Use the Notion node to automate work in Notion, and integrate Notion with other applications. n8n has built-in support for a wide range of Notion features, including getting and searching databases, creating pages, and getting users.

On this page, you'll find a list of operations the Notion node supports and links to more resources.

/// note | Credentials
Refer to [Notion credentials](/integrations/builtin/credentials/notion.md) for guidance on setting up authentication. 
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

#### Operations

* Block
	* Append After
	* Get Child Blocks
* Database
	* Get
	* Get Many
	* Search
* Database Page
	* Create
	* Get
	* Get Many
	* Update
* Page
	* Archive
	* Create
	* Search
* User
	* Get
	* Get Many

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'notion') ]]

#### Related resources

n8n provides an app node for Notion. You can find the trigger node docs [here](/integrations/builtin/trigger-nodes/n8n-nodes-base.notiontrigger.md).

Refer to [Notion's documentation](https://developers.notion.com/){:target=_blank .external-link} for details about their API.

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

#### Common issues

For common errors or issues and suggested resolution steps, refer to [Common issues](/integrations/builtin/app-nodes/n8n-nodes-base.notion/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/builtin/app-nodes/n8n-nodes-base.postgres/index.md*


##### Postgres node

Use the Postgres node to automate work in Postgres, and integrate Postgres with other applications. n8n has built-in support for a wide range of Postgres features, including executing queries, as well as inserting and updating rows in a database. 

On this page, you'll find a list of operations the Postgres node supports and links to more resources.

/// note | Credentials
Refer to [Postgres credentials](/integrations/builtin/credentials/postgres.md) for guidance on setting up authentication. 
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

#### Operations

* [**Delete**](#delete): Delete an entire table or rows in a table
* [**Execute Query**](#execute-query): Execute an SQL query
* [**Insert**](#insert): Insert rows in a table
* [**Insert or Update**](#insert-or-update): Insert or update rows in a table
* [**Select**](#select): Select rows from a table
* [**Update**](#update): Update rows in a table

##### Delete

Use this operation to delete an entire table or rows in a table.

Enter these parameters:

- **Credential to connect with**: Create or select an existing [Postgres credential](/integrations/builtin/credentials/postgres.md).
- **Operation**: Select **Delete**.
- **Schema**: Choose the schema that contains the table you want to work on. Select **From list** to choose the schema from the dropdown list or **By Name** to enter the schema name.
- **Table**: Choose the table that you want to work on. Select **From list** to choose the table from the dropdown list or **By Name** to enter the table name.
- **Command**: The deletion action to take:
	- **Truncate**: Removes the table's data but preserves the table's structure.
		- **Restart Sequences**: Whether to reset auto increment columns to their initial values as part of the Truncate process.
	- **Delete**: Delete the rows that match the "Select Rows" condition. If you don't select anything, Postgres deletes all rows.
		- **Select Rows**: Define a **Column**, **Operator**, and **Value** to match rows on.
		- **Combine Conditions**: How to combine the conditions in "Select Rows". **AND** requires all conditions to be true, while **OR** requires at least one condition to be true.
	- **Drop**: Deletes the table's data and structure permanently.

#### Delete options

- **Cascade**: Whether to also drop all objects that depend on the table, like views and sequences. Available if using **Truncate** or **Drop** commands.
- **Connection Timeout**: The number of seconds to try to connect to the database.
- **Delay Closing Idle Connection**: The number of seconds to wait before considering idle connections eligible for closing.
- **Query Batching**: The way to send queries to the database:
	- **Single Query**: A single query for all incoming items.
	- **Independently**: Execute one query per incoming item of the execution.
	- **Transaction**: Execute all queries in a transaction. If a failure occurs, Postgres rolls back all changes.
- **Output Large-Format Numbers As**: The format to output `NUMERIC` and `BIGINT` columns as:
	- **Numbers**: Use this for standard numbers.
	- **Text**: Use this if you expect numbers longer than 16 digits. Without this, numbers may be incorrect.

##### Execute Query

Use this operation to execute an SQL query.

Enter these parameters:

- **Credential to connect with**: Create or select an existing [Postgres credential](/integrations/builtin/credentials/postgres.md).
- **Operation**: Select **Execute Query**.
- **Query**: The SQL query to execute. You can use n8n [expressions](/code/expressions.md) and tokens like `$1`, `$2`, and `$3` to build [prepared statements](https://www.postgresql.org/docs/current/sql-prepare.html) to use with [query parameters](#use-query-parameters).

#### Execute Query options

- **Connection Timeout**: The number of seconds to try to connect to the database.
- **Delay Closing Idle Connection**: The number of seconds to wait before considering idle connections eligible for closing.
- **Query Batching**: The way to send queries to the database:
	- **Single Query**: A single query for all incoming items.
	- **Independently**: Execute one query per incoming item of the execution.
	- **Transaction**: Execute all queries in a transaction. If a failure occurs, Postgres rolls back all changes.
- **Query Parameters**: A comma-separated list of values that you want to use as [query parameters](#use-query-parameters).
- **Output Large-Format Numbers As**: The format to output `NUMERIC` and `BIGINT` columns as:
	- **Numbers**: Use this for standard numbers.
	- **Text**: Use this if you expect numbers longer than 16 digits. Without this, numbers may be incorrect.
- **Replace Empty Strings with NULL**: Whether to replace empty strings with NULL in input. This may be useful when working with data exported from spreadsheet software.

##### Insert

Use this operation to insert rows in a table.

Enter these parameters:

- **Credential to connect with**: Create or select an existing [Postgres credential](/integrations/builtin/credentials/postgres.md).
- **Operation**: Select **Insert**.
- **Schema**: Choose the schema that contains the table you want to work on. Select **From list** to choose the schema from the dropdown list or **By Name** to enter the schema name.
- **Table**: Choose the table that you want to work on. Select **From list** to choose the table from the dropdown list or **By Name** to enter the table name.
- **Mapping Column Mode**: How to map column names to incoming data:
	- **Map Each Column Manually**: Select the values to use for each column.
	- **Map Automatically**: Automatically map incoming data to matching column names in Postgres. The incoming data field names must match the column names in Postgres for this to work. If necessary, consider using the [edit fields (set) node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set/) before this node to adjust the format as needed.

#### Insert options

- **Connection Timeout**: The number of seconds to try to connect to the database.
- **Delay Closing Idle Connection**: The number of seconds to wait before considering idle connections eligible for closing.
- **Query Batching**: The way to send queries to the database:
	- **Single Query**: A single query for all incoming items.
	- **Independently**: Execute one query per incoming item of the execution.
	- **Transaction**: Execute all queries in a transaction. If a failure occurs, Postgres rolls back all changes.
- **Output Columns**: Choose which columns to output. You can select from a list of available columns or specify IDs using [expressions](/code/expressions.md).
- **Output Large-Format Numbers As**: The format to output `NUMERIC` and `BIGINT` columns as:
	- **Numbers**: Use this for standard numbers.
	- **Text**: Use this if you expect numbers longer than 16 digits. Without this, numbers may be incorrect.
- **Skip on Conflict**: Whether to skip the row if the insert violates a unique or exclusion constraint instead of throwing an error.
- **Replace Empty Strings with NULL**: Whether to replace empty strings with NULL in input. This may be useful when working with data exported from spreadsheet software.

##### Insert or Update

Use this operation to insert or update rows in a table.

Enter these parameters:

- **Credential to connect with**: Create or select an existing [Postgres credential](/integrations/builtin/credentials/postgres.md).
- **Operation**: Select **Insert or Update**.
- **Schema**: Choose the schema that contains the table you want to work on. Select **From list** to choose the schema from the dropdown list or **By Name** to enter the schema name.
- **Table**: Choose the table that you want to work on. Select **From list** to choose the table from the dropdown list or **By Name** to enter the table name.
- **Mapping Column Mode**: How to map column names to incoming data:
	- **Map Each Column Manually**: Select the values to use for each column.
	- **Map Automatically**: Automatically map incoming data to matching column names in Postgres. The incoming data field names must match the column names in Postgres for this to work. If necessary, consider using the [edit fields (set) node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set/) before this node to adjust the format as needed.

#### Insert or Update options

- **Connection Timeout**: The number of seconds to try to connect to the database.
- **Delay Closing Idle Connection**: The number of seconds to wait before considering idle connections eligible for closing.
- **Query Batching**: The way to send queries to the database:
	- **Single Query**: A single query for all incoming items.
	- **Independently**: Execute one query per incoming item of the execution.
	- **Transaction**: Execute all queries in a transaction. If a failure occurs, Postgres rolls back all changes.
- **Output Columns**: Choose which columns to output. You can select from a list of available columns or specify IDs using [expressions](/code/expressions.md).
- **Output Large-Format Numbers As**: The format to output `NUMERIC` and `BIGINT` columns as:
	- **Numbers**: Use this for standard numbers.
	- **Text**: Use this if you expect numbers longer than 16 digits. Without this, numbers may be incorrect.
- **Replace Empty Strings with NULL**: Whether to replace empty strings with NULL in input. This may be useful when working with data exported from spreadsheet software.

##### Select

Use this operation to select rows in a table.

Enter these parameters:

- **Credential to connect with**: Create or select an existing [Postgres credential](/integrations/builtin/credentials/postgres.md).
- **Operation**: Select **Select**.
- **Schema**: Choose the schema that contains the table you want to work on. Select **From list** to choose the schema from the dropdown list or **By Name** to enter the schema name.
- **Table**: Choose the table that you want to work on. Select **From list** to choose the table from the dropdown list or **By Name** to enter the table name.
- **Return All**: Whether to return all results or only up to a given limit.
- **Limit**: The maximum number of items to return when **Return All** is disabled.
- **Select Rows**: Set the conditions to select rows. Define a **Column**, **Operator**, and **Value** to match rows on. If you don't select anything, Postgres selects all rows.
- **Combine Conditions**: How to combine the conditions in **Select Rows**. **AND** requires all conditions to be true, while **OR** requires at least one condition to be true.
- **Sort**: Choose how to sort the selected rows. Choose a **Column** from a list or by ID and a sort **Direction**.

#### Select options

- **Connection Timeout**: The number of seconds to try to connect to the database.
- **Delay Closing Idle Connection**: The number of seconds to wait before considering idle connections eligible for closing.
- **Query Batching**: The way to send queries to the database:
	- **Single Query**: A single query for all incoming items.
	- **Independently**: Execute one query per incoming item of the execution.
	- **Transaction**: Execute all queries in a transaction. If a failure occurs, Postgres rolls back all changes.
- **Output Columns**: Choose which columns to output. You can select from a list of available columns or specify IDs using [expressions](/code/expressions.md).
- **Output Large-Format Numbers As**: The format to output `NUMERIC` and `BIGINT` columns as:
	- **Numbers**: Use this for standard numbers.
	- **Text**: Use this if you expect numbers longer than 16 digits. Without this, numbers may be incorrect.

##### Update

Use this operation to update rows in a table.

Enter these parameters:

- **Credential to connect with**: Create or select an existing [Postgres credential](/integrations/builtin/credentials/postgres.md).
- **Operation**: Select **Update**.
- **Schema**: Choose the schema that contains the table you want to work on. Select **From list** to choose the schema from the dropdown list or **By Name** to enter the schema name.
- **Table**: Choose the table that you want to work on. Select **From list** to choose the table from the dropdown list or **By Name** to enter the table name.
- **Mapping Column Mode**: How to map column names to incoming data:
	- **Map Each Column Manually**: Select the values to use for each column.
	- **Map Automatically**: Automatically map incoming data to matching column names in Postgres. The incoming data field names must match the column names in Postgres for this to work. If necessary, consider using the [edit fields (set) node](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.set/) before this node to adjust the format as needed.

#### Update options

- **Connection Timeout**: The number of seconds to try to connect to the database.
- **Delay Closing Idle Connection**: The number of seconds to wait before considering idle connections eligible for closing.
- **Query Batching**: The way to send queries to the database:
	- **Single Query**: A single query for all incoming items.
	- **Independently**: Execute one query per incoming item of the execution.
	- **Transaction**: Execute all queries in a transaction. If a failure occurs, Postgres rolls back all changes.
- **Output Columns**: Choose which columns to output. You can select from a list of available columns or specify IDs using [expressions](/code/expressions.md).
- **Output Large-Format Numbers As**: The format to output `NUMERIC` and `BIGINT` columns as:
	- **Numbers**: Use this for standard numbers.
	- **Text**: Use this if you expect numbers longer than 16 digits. Without this, numbers may be incorrect.
- **Replace Empty Strings with NULL**: Whether to replace empty strings with NULL in input. This may be useful when working with data exported from spreadsheet software.

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'postgres') ]]

#### Related resources

n8n provides a trigger node for Postgres. You can find the trigger node docs [here](/integrations/builtin/trigger-nodes/n8n-nodes-base.postgrestrigger.md).

#### Use query parameters

When creating a query to run on a Postgres database, you can use the **Query Parameters** field in the **Options** section to load data into the query. n8n sanitizes data in query parameters, which prevents SQL injection.

For example, you want to find a person by their email address. Given the following input data:

```js
[
    {
        "email": "alex@example.com",
        "name": "Alex",
        "age": 21 
    },
    {
        "email": "jamie@example.com",
        "name": "Jamie",
        "age": 33 
    }
]
```

You can write a query like:

```sql
SELECT * FROM $1:name WHERE email = $2;
```

Then in **Query Parameters**, provide the field values to use. You can provide fixed values or expressions. For this example, use expressions so the node can pull the email address from each input item in turn:

```js
// users is an example table name
{{ [ 'users', $json.email ] }} 
```

#### Common issues

For common questions or issues and suggested solutions, refer to [Common issues](/integrations/builtin/app-nodes/n8n-nodes-base.postgres/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/builtin/app-nodes/n8n-nodes-base.supabase/index.md*


##### Supabase node

Use the Supabase node to automate work in Supabase, and integrate Supabase with other applications. n8n has built-in support for a wide range of Supabase features, including creating, deleting, and getting rows. 

On this page, you'll find a list of operations the Supabase node supports and links to more resources.

/// note | Credentials
Refer to [Supabase credentials](/integrations/builtin/credentials/supabase.md) for guidance on setting up authentication. 
///

--8<-- "_snippets/integrations/builtin/app-nodes/ai-tools.md"

#### Operations

* Row
    * Create a new row
    * Delete a row
    * Get a row
    * Get all rows
    * Update a row

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'supabase') ]]

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

#### Common issues

For common errors or issues and suggested resolution steps, refer to [Common issues](/integrations/builtin/app-nodes/n8n-nodes-base.supabase/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/builtin/app-nodes/n8n-nodes-base.telegram/index.md*


##### Telegram node

Use the Telegram node to automate work in [Telegram](https://telegram.org/){:target=_blank .external-link} and integrate Telegram with other applications. n8n has built-in support for a wide range of Telegram features, including getting files as well as deleting and editing messages. 

On this page, you'll find a list of operations the Telegram node supports and links to more resources.

/// note | Credentials
Refer to [Telegram credentials](/integrations/builtin/credentials/telegram.md) for guidance on setting up authentication. 
///

#### Operations

* [**Chat** operations](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations.md)
    * [**Get**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations.md#get-chat) up-to-date information about a chat.
    * [**Get Administrators**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations.md#get-administrators): Get a list of all administrators in a chat.
    * [**Get Member**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations.md#get-chat-member): Get the details of a chat member.
    * [**Leave**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations.md#leave-chat) a chat.
    * [**Set Description**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations.md#set-description) of a chat.
    * [**Set Title**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/chat-operations.md#set-title) of a chat.
* [**Callback** operations](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/callback-operations.md)
    * [**Answer Query**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/callback-operations.md#answer-query): Send answers to callback queries sent from [inline keyboards](https://core.telegram.org/bots/features#inline-keyboards){:target=_blank .external-link}.
    * [**Answer Inline Query**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/callback-operations.md#answer-inline-query): Send answers to callback queries sent from inline queries.
* [**File** operations](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/file-operations.md)
    * [**Get File**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/file-operations.md#get-file) from Telegram.
* [**Message** operations](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md)
    * [**Delete Chat Message**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md#delete-chat-message).
    * [**Edit Message Text**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md#edit-message-text): Edit the text of an existing message.
    * [**Pin Chat Message**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md#pin-chat-message) for the chat.
    * [**Send Animation**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md#send-animation) to the chat.
        * For use with GIFs or H.264/MPEG-4 AVC videos without sound up to 50 MB in size.
    * [**Send Audio**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md#send-audio) file to the chat and display it in the music player.
    * [**Send Chat Action**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md#send-chat-action): Tell the user that something is happening on the bot's side. The status is set for 5 seconds or less.
    * [**Send Document**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md#send-document) to the chat.
    * [**Send Location**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md#send-location): Send a geolocation to the chat.
    * [**Send Media Group**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md#send-media-group): Send a group of photos and/or videos.
    * [**Send Message**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md#send-message) to the chat.
    * [**Send Photo**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md#send-photo) to the chat.
    * [**Send Sticker**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md#send-sticker) to the chat.
        * For use with static .WEBP, animated .TGS, or video .WEBM stickers.
    * [**Send Video**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md#send-video) to the chat.
    * [**Unpin Chat Message**](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/message-operations.md#unpin-chat-message) from the chat.
    
    /// note | Add bot to channel
    To use most of the **Message** operations, you must add your bot to a channel so that it can send messages to that channel. Refer to [Common Issues | Add a bot to a Telegram channel](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues.md#add-a-bot-to-a-telegram-channel) for more information.
    ///

    ## Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'telegram') ]]

#### Related resources

Refer to [Telegram's API documentation](https://core.telegram.org/bots/api){:target=_blank .external-link} for more information about the service.

n8n provides a trigger node for Telegram. Refer to the trigger node docs [here](/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/index.md) for more information.

#### Common issues

For common errors or issues and suggested resolution steps, refer to [Common Issues](/integrations/builtin/app-nodes/n8n-nodes-base.telegram/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/index.md*


##### WhatsApp Business Cloud node

Use the WhatsApp Business Cloud node to automate work in WhatsApp Business, and integrate WhatsApp Business with other applications. n8n has built-in support for a wide range of WhatsApp Business features, including sending messages, and uploading, downloading, and deleting media. 

On this page, you'll find a list of operations the WhatsApp Business Cloud node supports and links to more resources.

/// note | Credentials
Refer to [WhatsApp Business Cloud credentials](/integrations/builtin/credentials/whatsapp.md) for guidance on setting up authentication. 
///

#### Operations

* Message
	* Send
	* Send and Wait for Response
	* Send Template
* Media
	* Upload
	* Download
	* Delete

--8<-- "_snippets/integrations/builtin/send-and-wait-operation.md"

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'whatsapp-business-cloud') ]]

#### Related resources

Refer to [WhatsApp Business Platform's Cloud API documentation](https://developers.facebook.com/docs/whatsapp/cloud-api){:target=_blank} for details about the operations.

#### Common issues

For common errors or issues and suggested resolution steps, refer to [Common Issues](/integrations/builtin/app-nodes/n8n-nodes-base.whatsapp/common-issues.md).

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"


---



## Index {#index}

*Source: docs/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/index.md*


##### OpenAI node

Use the OpenAI node to automate work in OpenAI and integrate OpenAI with other applications. n8n has built-in support for a wide range of OpenAI features, including creating images and assistants, as well as chatting with models. 

On this page, you'll find a list of operations the OpenAI node supports and links to more resources.

/// note | OpenAI Assistant node
The OpenAI node replaces the OpenAI assistant node from version 1.29.0 on.
///

/// note | Credentials
Refer to [OpenAI credentials](/integrations/builtin/credentials/openai.md) for guidance on setting up authentication. 
///

#### Operations

- **Assistant** 
	- [**Create an Assistant**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations.md#create-an-assistant)
	- [**Delete an Assistant**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations.md#delete-an-assistant)
	- [**List Assistants**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations.md#list-assistants)
	- [**Message an Assistant**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations.md#message-an-assistant)
	- [**Update an Assistant**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations.md#update-an-assistant)
- **Text**
	- [**Message a Model**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations.md#message-a-model)
	- [**Classify Text for Violations**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations.md#classify-text-for-violations)
- **Image**
	- [**Analyze Image**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/image-operations.md#analyze-image)
	- [**Generate an Image**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/image-operations.md#generate-an-image)
- **Audio**
	- [**Generate Audio**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations.md#generate-audio)
	- [**Transcribe a Recording**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations.md#transcribe-a-recording)
	- [**Translate a Recording**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/audio-operations.md#translate-a-recording)
- **File**
	- [**Delete a File**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations.md#delete-a-file)
	- [**List Files**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations.md#list-files)
	- [**Upload a File**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/file-operations.md#upload-a-file)

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'openai') ]]

#### Related resources

Refer to [OpenAI's documentation](https://beta.openai.com/docs/introduction){:target=_blank .external-link} for more information about the service.

Refer to [OpenAI's assistants documentation](https://platform.openai.com/docs/assistants/how-it-works/objects){:target=_blank .external-link} for more information about how assistants work.

For help dealing with rate limits, refer to [Handling rate limits](/integrations/builtin/rate-limits.md).

--8<-- "_snippets/integrations/builtin/app-nodes/operation-not-supported.md"

#### Using tools with OpenAI assistants

Some operations allow you to connect tools. [Tools](https://docs.n8n.io/advanced-ai/examples/understand-tools/) act like addons that your AI can use to access extra context or resources.

Select the **Tools** connector to browse the available tools and add them.

Once you add a tool connection, the OpenAI node becomes a [root node](/glossary.md#root-node-n8n), allowing it to form a [cluster node](/glossary.md#cluster-node-n8n) with the tools [sub-nodes](/glossary.md#sub-node-n8n). See [Node types](/integrations/builtin/node-types.md#cluster-nodes) for more information on cluster nodes and root nodes.

##### Operations that support tool connectors

- **Assistant**
	- [**Message an Assistant**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/assistant-operations.md#message-an-assistant)
- **Text**
	- [**Message a Model**](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations.md#message-a-model)

#### Common issues

For common questions or issues and suggested solutions, refer to [Common issues](/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/builtin/cluster-nodes/index.md*


##### Cluster nodes

--8<-- "_snippets/integrations/builtin/cluster-nodes/cluster-nodes-summary.md"


#### Root nodes

Each cluster starts with one [root node](/glossary.md#root-node-n8n).

#### Sub-nodes

Each root node can have one or more [sub-nodes](/glossary.md#sub-node-n8n) attached to it.



---



## Index {#index}

*Source: docs/integrations/builtin/cluster-nodes/root-nodes/index.md*


##### Root nodes

Root nodes are the foundational nodes within a group of cluster nodes.

--8<-- "_snippets/integrations/builtin/cluster-nodes/cluster-nodes-summary.md"
--8<-- "_glossary/ai-glossary.md"


---



## Index {#index}

*Source: docs/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md*


##### AI Agent node

An [AI agent](/glossary.md#ai-agent) is an autonomous system that receives data, makes rational decisions, and acts within its environment to achieve specific goals. The AI agent's environment is everything the agent can access that isn't the agent itself. This agent uses external [tools](/glossary.md#ai-tool) and APIs to perform actions and retrieve information. It can understand the capabilities of different tools and determine which tool to use depending on the task. 

/// note | Connect a tool
You must connect at least one tool [sub-node](/integrations/builtin/cluster-nodes/sub-nodes/index.md) to an AI Agent node.
///

/// note | Agent type
Prior to version 1.82.0, the AI Agent had a setting for working as different agent types. This has now been removed and all AI Agent nodes work as a `Tools Agent` which was the recommended and most frequently used setting. If you're working with older versions of the AI Agent in workflows or templates, as long as they were set to 'Tools Agent', they should continue to behave as intended with the updated node.
///


#### Templates and examples
<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'agent') ]]

#### Related resources

Refer to [LangChain's documentation on agents](https://js.langchain.com/docs/concepts/agents/){:target=_blank .external-link} for more information about the service.

New to AI Agents? Read the [n8n blog introduction to AI agents](https://blog.n8n.io/ai-agents/){:target=_blank .external-link}.

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

#### Common issues

For common errors or issues and suggested resolution steps, refer to [Common Issues](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/common-issues.md).

--8<-- "_glossary/ai-glossary.md"


---



## Index {#index}

*Source: docs/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/index.md*


##### Question and Answer Chain node

Use the Question and Answer Chain node to use a [vector store](/glossary.md#ai-vector-store) as a retriever.

On this page, you'll find the node parameters for the Question and Answer Chain node, and links to more resources.

#### Node parameters

##### Query

The question you want to ask.

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'retrieval-qanda-chain') ]]

#### Related resources

Refer to [LangChain's documentation on retrieval chains](https://js.langchain.com/docs/tutorials/rag/){:target=_blank .external-link} for examples of how LangChain can use a vector store as a retriever.

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

#### Common issues

For common errors or issues and suggested resolution steps, refer to [Common Issues](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainretrievalqa/common-issues.md).

--8<-- "_glossary/ai-glossary.md"


---



## Index {#index}

*Source: docs/integrations/builtin/cluster-nodes/sub-nodes/index.md*


##### Sub nodes

Sub nodes attach to root nodes within a group of cluster nodes. They configure the overall functionality of the cluster.

--8<-- "_snippets/integrations/builtin/cluster-nodes/cluster-nodes-summary.md"
--8<-- "_glossary/ai-glossary.md"


---



## Index {#index}

*Source: docs/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/index.md*


##### Ollama Chat Model node

The Ollama Chat Model node allows you use local Llama 2 models with conversational [agents](/glossary.md#ai-agent).

On this page, you'll find the node parameters for the Ollama Chat Model node, and links to more resources.

/// note | Credentials
You can find authentication information for this node [here](/integrations/builtin/credentials/ollama.md).
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

#### Node parameters

* **Model**: Select the model that generates the completion. Choose from:
	* **Llama2**
	* **Llama2 13B**
	* **Llama2 70B**
	* **Llama2 Uncensored**

Refer to the Ollama [Models Library documentation](https://ollama.com/library){:target=_blank .external-link} for more information about available models.

#### Node options

* **Sampling Temperature**: Use this option to control the randomness of the sampling process. A higher temperature creates more diverse sampling, but increases the risk of hallucinations.
* **Top K**: Enter the number of token choices the model uses to generate the next token.
* **Top P**: Use this option to set the probability the completion should use. Use a lower value to ignore less probable options. 

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'ollama-chat-model') ]]

#### Related resources

Refer to [LangChains's Ollama Chat Model documentation](https://js.langchain.com/docs/integrations/chat/ollama/){:target=_blank .external-link} for more information about the service.

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

#### Common issues

For common questions or issues and suggested solutions, refer to [Common issues](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues.md).

--8<-- "_glossary/ai-glossary.md"

--8<-- "_snippets/self-hosting/starter-kits/self-hosted-ai-starter-kit.md"


---



## Index {#index}

*Source: docs/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/index.md*


##### OpenAI Chat Model node

Use the OpenAI Chat Model node to use OpenAI's chat models with conversational [agents](/glossary.md#ai-agent).

On this page, you'll find the node parameters for the OpenAI Chat Model node and links to more resources.

/// note | Credentials
You can find authentication information for this node [here](/integrations/builtin/credentials/openai.md).
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

#### Node parameters

##### Model

Select the model to use to generate the completion.

n8n dynamically loads models from OpenAI and you'll only see the models available to your account.

#### Node options

Use these options to further refine the node's behavior.

##### Base URL

Enter a URL here to override the default URL for the API.

##### Frequency Penalty

Use this option to control the chances of the model repeating itself. Higher values reduce the chance of the model repeating itself.

##### Maximum Number of Tokens

Enter the maximum number of tokens used, which sets the completion length.

##### Response Format

Choose **Text** or **JSON**. **JSON** ensures the model returns valid JSON.

##### Presence Penalty

Use this option to control the chances of the model talking about new topics. Higher values increase the chance of the model talking about new topics.

##### Sampling Temperature

Use this option to control the randomness of the sampling process. A higher temperature creates more diverse sampling, but increases the risk of hallucinations.

##### Timeout

Enter the maximum request time in milliseconds.

##### Max Retries

Enter the maximum number of times to retry a request.

##### Top P

Use this option to set the probability the completion should use. Use a lower value to ignore less probable options. 

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'openai-chat-model') ]]

#### Related resources

Refer to [LangChains's OpenAI documentation](https://js.langchain.com/docs/integrations/chat/openai/){:target=_blank .external-link} for more information about the service.

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

#### Common issues

For common questions or issues and suggested solutions, refer to [Common issues](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai/common-issues.md).

--8<-- "_glossary/ai-glossary.md"


---



## Index {#index}

*Source: docs/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama/index.md*


##### Ollama Model node

The Ollama Model node allows you use local Llama 2 models.

On this page, you'll find the node parameters for the Ollama Model node, and links to more resources.

This node lacks tools support, so it won't work with the [AI Agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/index.md) node. Instead, connect it with the [Basic LLM Chain](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.chainllm.md) node.

/// note | Credentials
You can find authentication information for this node [here](/integrations/builtin/credentials/ollama.md).
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

#### Node parameters

* **Model**: Select the model that generates the completion. Choose from:
	* **Llama2**
	* **Llama2 13B**
	* **Llama2 70B**
	* **Llama2 Uncensored**

Refer to the Ollama [Models Library documentation](https://ollama.com/library){:target=_blank .external-link} for more information about available models.

#### Node options

* **Sampling Temperature**: Use this option to control the randomness of the sampling process. A higher temperature creates more diverse sampling, but increases the risk of hallucinations.
* **Top K**: Enter the number of token choices the model uses to generate the next token.
* **Top P**: Use this option to set the probability the completion should use. Use a lower value to ignore less probable options.

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'ollama-model') ]]

#### Related resources

Refer to [LangChains's Ollama documentation](https://js.langchain.com/docs/integrations/llms/ollama/){:target=_blank .external-link} for more information about the service.

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

#### Common issues

For common questions or issues and suggested solutions, refer to [Common issues](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmollama/common-issues.md).

--8<-- "_glossary/ai-glossary.md"

--8<-- "_snippets/self-hosting/starter-kits/self-hosted-ai-starter-kit.md"


---



## Index {#index}

*Source: docs/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/index.md*


##### Simple Memory node

Use the Simple Memory node to [persist](/glossary.md#ai-memory) chat history in your workflow.

On this page, you'll find a list of operations the Simple Memory node supports, and links to more resources.

/// warning | Don't use this node if running n8n in queue mode
If your n8n instance uses [queue mode](/hosting/scaling/queue-mode.md), this node doesn't work in an active production workflow. This is because n8n can't guarantee that every call to Simple Memory will go to the same worker.
///

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

#### Node parameters

Configure these parameters to configure the node:

* **Session Key**: Enter the key to use to store the memory in the workflow data.
* **Context Window Length**: Enter the number of previous interactions to consider for context.

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'window-buffer-memory') ]]

#### Related resources

Refer to [LangChain's Buffer Window Memory documentation](https://v03.api.js.langchain.com/classes/langchain.memory.BufferWindowMemory.html){:target=_blank .external-link} for more information about the service.

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

#### Common issues

For common questions or issues and suggested solutions, refer to [Common issues](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow/common-issues.md).

--8<-- "_glossary/ai-glossary.md"


---



## Index {#index}

*Source: docs/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/index.md*


##### Structured Output Parser node

Use the Structured Output Parser node to return fields based on a JSON Schema.

On this page, you'll find the node parameters for the Structured Output Parser node, and links to more resources.

--8<-- "_snippets/integrations/builtin/cluster-nodes/sub-node-expression-resolution.md"

#### Node parameters

* **Schema Type**: Define the output structure and validation. You have two options to provide the schema:

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-sub-nodes/schema-type-structuring.md"

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'structured-output-parser') ]]

#### Related resources

Refer to [LangChain's output parser documentation](https://js.langchain.com/docs/concepts/output_parsers){:target=_blank .external-link} for more information about the service.

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

#### Common issues

For common questions or issues and suggested solutions, refer to [Common issues](/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.outputparserstructured/common-issues.md).

--8<-- "_glossary/ai-glossary.md"


---



## Index {#index}

*Source: docs/integrations/builtin/core-nodes/index.md*


##### Core nodes library

This section provides information about n8n's core [nodes](/glossary.md#node-n8n).






---



## Index {#index}

*Source: docs/integrations/builtin/core-nodes/n8n-nodes-base.code/index.md*


##### Code node

--8<-- "_snippets/integrations/builtin/core-nodes/code-node.md"

#### Common issues

For common questions or issues and suggested solutions, refer to [Common Issues](/integrations/builtin/core-nodes/n8n-nodes-base.code/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/index.md*


##### Execute Command

The Execute Command node runs shell commands on the host machine that runs n8n.

/// note | Which shell runs the command?
This node executes the command in the default shell of the host machine. For example, `cmd` on Windows and `zsh` on macOS.

If you run n8n with Docker, your command will run in the n8n container and not the Docker host.
///

/// note | Not available on Cloud
This node isn't available on n8n Cloud.
///

#### Node parameters

Configure the node using the following parameters.

##### Execute Once

Choose whether you want the node to execute only once (turned on) or once for every item it receives as input (turned off).

##### Command

Enter the command to execute on the host machine. Refer to sections below for examples of running [multiple commands](#run-multiple-commands) and [cURL commands](#run-curl-command).

#### Run multiple commands

Use one of two methods to run multiple commands in one Execute Command node:

* Enter each command on one line separated by `&&`. For example, you can combine the change directory (cd) command with the list (ls) command using `&&`.

    ```bash
    cd bin && ls
    ```

* Enter each command on a separate line. For example, you can write the list (ls) command on a new line after the change directory (cd) command.

    ```bash
    cd bin
    ls
    ```

#### Run cURL command

You can also use the [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) node to make a cURL request.

If you want to run the curl command in the Execute Command node, you will have to build a Docker image based on the existing n8n image. The default n8n Docker image uses Alpine Linux. You will have to install the curl package.

1. Create a file named `Dockerfile`.
2. Add the below code snippet to the Dockerfile.

    ```shell
    FROM docker.n8n.io/n8nio/n8n
    USER root
    RUN apk --update add curl
    USER node
    ```

3. In the same folder, execute the command below to build the Docker image.

    ```shell
    docker build -t n8n-curl
    ```

4. Replace the Docker image you used before. For example, replace `docker.n8n.io/n8nio/n8n` with `n8n-curl`.
5. Run the newly created Docker image. You'll now be able to execute ssh using the Execute Command Node.

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'execute-command') ]]

#### Common issues

For common questions or issues and suggested solutions, refer to [Common Issues](/integrations/builtin/core-nodes/n8n-nodes-base.executecommand/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md*


##### HTTP Request node

The HTTP Request node is one of the most versatile nodes in n8n. It allows you to make HTTP requests to query data from any app or service with a REST API. You can use the HTTP Request node a regular node or attached to an [AI agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md) to use as a [tool](/advanced-ai/examples/understand-tools.md){ data-preview }.

When using this node, you're creating a REST API call. You need some understanding of basic API terminology and concepts.

There are two ways to create an HTTP request: configure the [node parameters](#node-parameters) or [import a curl command](#import-curl-command).

/// note | Credentials
Refer to [HTTP Request credentials](/integrations/builtin/credentials/httprequest.md) for guidance on setting up authentication. 
///

#### Node parameters

##### Method

Select the method to use for the request:

- DELETE
- GET
- HEAD
- OPTIONS
- PATCH
- POST
- PUT

##### URL

Enter the endpoint you want to use.

##### Authentication

n8n recommends using the **Predefined Credential Type** option when it's available. It offers an easier way to set up and manage credentials, compared to configuring generic credentials.

#### Predefined credentials

Credentials for integrations supported by n8n, including both built-in and community nodes. Use **Predefined Credential Type** for custom operations without extra setup. Refer to [Custom API operations](/integrations/custom-operations.md) for more information.

#### Generic credentials

Credentials for integrations not supported by n8n. You'll need to manually configure the authentication process, including specifying the required API endpoints, necessary parameters, and the authentication method. 

You can select one of the following methods:

* Basic auth
* Custom auth
* Digest auth
* Header auth
* OAuth1 API
* OAuth2 API
* Query auth

Refer to [HTTP request credentials](/integrations/builtin/credentials/httprequest.md) for more information on setting up each credential type.

##### Send Query Parameters

Query parameters act as filters on HTTP requests. If the API you're interacting with supports them and the request you're making needs a filter, turn this option on.

**Specify your query parameters** using one of the available options:

* **Using Fields Below**: Enter **Name**/**Value** pairs of **Query Parameters**. To enter more query parameter name/value pairs, select **Add Parameter**. The name is the name of the field you're filtering on, and the value is the filter value.
* **Using JSON**: Enter **JSON** to define your query parameters.

Refer to your service's API documentation for detailed guidance.

##### Send Headers

Use this parameter to send headers with your request. Headers contain metadata or context about your request.

**Specify Headers** using one of the available options:

* **Using Fields Below**: Enter **Name**/**Value** pairs of **Header Parameters**. To enter more header parameter name/value pairs, select **Add Parameter**. The name is the header you wish to set, and the value is the value you want to pass for that header.
* **Using JSON**: Enter **JSON** to define your header parameters.

Refer to your service's API documentation for detailed guidance.

##### Send Body

If you need to send a body with your API request, turn this option on.

Then select the **Body Content Type** that best matches the format for the body content you wish to send.

<!-- vale Vale.Spelling = NO -->
#### Form URLencoded
<!-- vale Vale.Spelling = YES -->

Use this option to send your body as `application/x-www-form-urlencoded`.

**Specify Body** using one of the available options:

* **Using Fields Below**: Enter **Name**/**Value** pairs of **Body Parameters**. To enter more body parameter name/value pairs, select **Add Parameter**. The name should be the form field name, and the value is what you wish to set that field to.
* **Using Single Field**: Enter your name/value pairs in a single **Body** parameter with format `fieldname1=value1&fieldname2=value2`.

Refer to your service's API documentation for detailed guidance.

#### Form-Data

Use this option to send your body as `multipart/form-data`.

Configure your **Body Parameters** by selecting the **Parameter Type**:

* Choose **Form Data** to enter **Name**/**Value** pairs.
* Choose **n8n Binary File** to pull the body from a file the node has access to.
    * **Name**: Enter the ID of the field to set.
    * **Input Data Field Name**: Enter the name of the incoming field containing the binary file data you want to process.

Select **Add Parameter** to enter more parameters.

Refer to your service's API documentation for detailed guidance.

#### JSON

Use this option to send your body as JSON.

**Specify Body** using one of the available options:

* **Using Fields Below**: Enter **Name**/**Value** pairs of **Body Parameters**. To enter more body parameter name/value pairs, select **Add Parameter**.
* **Using JSON**: Enter **JSON** to define your body.

Refer to your service's API documentation for detailed guidance.

#### n8n Binary File

Use this option to send the contents of a file stored in n8n as the body.

Enter the name of the incoming field that contains the file as the **Input Data Field Name**.

Refer to your service's API documentation for detailed guidance on how to format the file.

#### Raw

Use this option to send raw data in the body.

* **Content Type**: Enter the `Content-Type` header to use for the raw body content. Refer to the IANA [Media types](https://www.iana.org/assignments/media-types/media-types.xhtml){:target=_blank .external-link} documentation for a full list of MIME content types.
* **Body**: Enter the raw body content to send.

Refer to your service's API documentation for detailed guidance.

#### Node options

Select **Add Option** to view and select these options. Options are available to all parameters unless otherwise noted.

##### Array Format in Query Parameters

/// note | Option availability
This option is only available when you turn on **Send Query Parameters**.
///

Use this option to control the format for arrays included in query parameters. Choose from these options:

* **No Brackets**: Arrays will format as the name=value for each item in the array, for example: `foo=bar&foo=qux`.
* **Brackets Only**: The node adds square brackets after each array name, for example: `foo[]=bar&foo[]=qux`.
* **Brackets with Indices**: The node adds square brackets with an index value after each array name, for example: `foo[0]=bar&foo[1]=qux`.

Refer to your service's API documentation for guidance on which option to use.

##### Batching

Control how to batch large numbers of input items:

* **Items per Batch**: Enter the number of input items to include in each batch.
* **Batch Interval**: Enter the time to wait between each batch of requests in milliseconds. Enter 0 for no batch interval.

##### Ignore SSL Issues

By default, n8n only downloads the response if SSL certificate validation succeeds. If you'd like to download the response even if SSL certificate validation fails, turn this option on.

##### Lowercase Headers

Choose whether to lowercase header names (turned on, default) or not (turned off).

##### Redirects

Choose whether to follow redirects (turned on by default) or not (turned off). If turned on, enter the maximum number of redirects the request should follow in **Max Redirects**.

##### Response

Use this option to set some details about the expected API response, including:

* **Include Response Headers and Status**: By default, the node returns only the body. Turn this option on to return the full response (headers and response status code) as well as the body.
* **Never Error**: By default, the node returns success only when the response returns with a 2xx code. Turn this option on to return success regardless of the code returned.
* **Response Format**: Select the format in which the data gets returned. Choose from:
    * **Autodetect** (default): The node detects and formats the response based on the data returned.
    * **File**: Select this option to put the response into a file. Enter the field name where you want the file returned in **Put Output in Field**.
    * **JSON**: Select this option to format the response as JSON.
    * **Text**: Select this option to format the response as plain text. Enter the field name where you want the file returned in **Put Output in Field**.

##### Pagination

Use this option to paginate results, useful for handling query results that are too big for the API to return in a single call.

/// note | Inspect the API data first
Some options for pagination require knowledge of the data returned by the API you're using. Before setting up pagination, either check the API documentation, or do an API call without pagination, to see the data it returns.
///
??? Details "Understand pagination"
    Pagination means splitting a large set of data into multiple pages. The amount of data on each page depends on the limit you set.
  
    For example, you make an API call to an endpoint called `/users`. The API wants to send back information on 300 users, but this is too much data for the API to send in one response. 
  
    If the API supports pagination, you can incrementally fetch the data. To do this, you call `/users` with a pagination limit, and a page number or URL to tell the API which page to send. In this example, say you use a limit of 10, and start from page 0. The API sends the first 10 users in its response. You then call the API again, increasing the page number by 1, to get the next 10 results.

Configure the pagination settings:

* **Pagination Mode**:
    * **Off**: Turn off pagination.
    * **Update a Parameter in Each Request**: Use this when you need to dynamically set parameters for each request.
    * **Response Contains Next URL**: Use this when the API response includes the URL of the next page. Use an expression to set **Next URL**.

For example setups, refer to [HTTP Request node cookbook | Pagination](/code/cookbook/http-node/pagination.md).

n8n provides built-in variables for working with HTTP node requests and responses when using pagination:

--8<-- "_snippets/integrations/builtin/core-nodes/http/pagination-variables.md"

--8<-- "_snippets/integrations/builtin/core-nodes/http/pagination-api-differences.md"

##### Proxy

Use this option if you need to specify an HTTP proxy.

Enter the **Proxy** the request should use.

##### Timeout

Use this option to set how long the node should wait for the server to send response headers (and start the response body). The node aborts requests that exceed this value for the initial response.

Enter the **Timeout** time to wait in milliseconds.

#### Tool-only options

The following options are only available when attached to an [AI agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md) as a [tool](/advanced-ai/examples/understand-tools.md){ data-preview }.

##### Optimize Response

Whether to optimize the tool response to reduce the amount of data passed to the LLM. Optimizing the response can reduce costs and can help the LLM ignore unimportant details, often leading to better results.

When optimizing responses, you select an expected response type, which determines other options you can configure. The supported response types are:

#### JSON

When expecting a **JSON** response, you can configure which parts of the JSON data to use as a response with the following choices:

* **Field Containing Data**: This field identifies a specific part of the JSON object that contains your relevant data. You can leave this blank to use the entire response.
* **Include Fields**: This is how you choose which fields you want in your response object. There are three choices:
	* **All**: Include all fields in the response object.
	* **Selected**: Include only the fields specified below.
		* **Fields**: A comma-separated list of fields to include in the response. You can use dot notation to specify nested fields. You can drag fields from the Input panel to add them to the field list.
	* **Exclude**: Include all fields *except* the fields specified below.
		* **Fields**: A comma-separated list of fields to exclude from the response. You can use dot notation to specify nested fields. You can drag fields from the Input panel to add them to the field list.

#### HTML

When expecting **HTML**, you can identify the part of an HTML document relevant to the LLM and optimize the response with the following options:

* **Selector (CSS)**: A specific element or element type to include in the response HTML. Uses the `body` element by default.
* **Return Only Content**: Whether to strip HTML tags and attributes from the response, leaving only the actual content. This uses fewer tokens and may be easier for the model to understand.
	* **Elements To Omit**: A comma-separated list of CSS selectors to exclude when extracting content.
* **Truncate Response**: Whether to limit the response size to save tokens.
	* **Max Response Characters**: The maximum number of characters to include in the HTML response. The default value is 1000.

#### Text

When expecting a generic **Text** response, you can optimize the results with the following options:

* **Truncate Response**: Whether to limit the response size to save tokens.
	* **Max Response Characters**: The maximum number of characters to include in the HTML response. The default value is 1000.

#### Import curl command

[curl](https://curl.se/){:target=_blank .external-link} is a command line tool and library for transferring data with URLs.

You can use curl to call REST APIs. If the API documentation of the service you want to use provides curl examples, you can copy them out of the documentation and into n8n to configure the HTTP Request node.

Import a curl command:

1. From the HTTP Request node's **Parameters** tab, select **Import cURL**. The **Import cURL command** modal opens.
2. Paste your curl command into the text box.
3. Select **Import**. n8n loads the request configuration into the node fields. This overwrites any existing configuration.

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'http-request') ]]

#### Common issues

For common questions or issues and suggested solutions, refer to [Common Issues](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/index.md*


##### Remove Duplicates node

Use the Remove Duplicates node to identify and delete items that are:

* identical across all fields or a subset of fields in a single execution
* identical to or surpassed by items seen in previous executions

This is helpful in situations where you can end up with duplicate data, such as a user creating multiple accounts, or a customer submitting the same order multiple times. When working with large datasets it becomes more difficult to spot and remove these items.

By comparing against data from previous executions, the Remove Duplicates node can  delete items seen in earlier executions. It can also ensure that new items have a later date or a higher value than previous values.

/// note | Major changes in 1.64.0
The n8n team overhauled this node in n8n 1.64.0. This document reflects the latest version of the node. If you're using an older version of n8n, you can find the previous version of this document [here](https://github.com/n8n-io/n8n-docs/blob/7a66308290e6e5b104fcb82a3beafa0d6987df36/docs/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates.md){:target=_blank .external-link}.
///

#### Operation modes

The remove duplication node works differently depending on the value of the **operation** parameter:

* **[Remove Items Repeated Within Current Input](#remove-items-repeated-within-current-input)**: Identify and remove duplicate items in the current input across all fields or a subset of fields.
* **[Remove Items Processed in Previous Executions](#remove-items-processed-in-previous-executions)**: Compare items in the current input to items from previous executions and remove duplicates.
* **[Clear Deduplication History](#clear-deduplication-history)**: Wipe the memory of items from previous executions.

##### Remove Items Repeated Within Current Input

When you set the "Operations" field to **Remove Items Repeated Within Current Input**, the Remove Duplicate node identifies and removes duplicate items in the current input. It can do this across all fields, or within a subset of fields.

#### Remove Items Repeated Within Current Input parameters

When using the **Remove Items Repeated Within Current Input** operation, the following parameter is available:

* **Compare**: Select which fields of the input data n8n should compare to check if they're the same. The following options are available:
	* **All Fields**: Compares all fields of the input data.
	* **All Fields Except**: Enter which input data fields n8n should exclude from the comparison. You can provide multiple values separated by commas.
	* **Selected Fields**: Enter which input data fields n8n should include in the comparison. You can provide multiple values separated by commas.

#### Remove Items Repeated Within Current Input options

If you choose **All Fields Except** or **Selected Fields** as your compare type, you can add these options:

* **Disable Dot Notation**: Set whether to use dot notation to reference child fields in the format `parent.child` (turned off) or not (turn on).
* **Remove Other Fields**: Set whether to remove any fields that aren't used in the comparison (turned on) or not (turned off).

##### Remove Items Processed in Previous Executions

When you set the "Operation" field to **Remove Items Processed in Previous Executions**, the Remove Duplicate node compares items in the current input to items from previous executions.

#### Remove Items Processed in Previous Executions parameters

When using the **Remove Items Processed in Previous Executions** operation, the following parameters are available:

* **Keep Items Where**: Select how n8n decides which items to keep. The following options are available:
	* **Value Is New**: n8n removes items if their value matches items from earlier executions.
	* **Value Is Higher than Any Previous Value**: n8n removes items if the current value isn't higher than previous values.
	* **Value Is a Date Later than Any Previous Date**: n8n removes date items if the current date isn't later than previous dates.

* **Value to Dedupe On**: The input field or fields to compare. The option you select for the **Keep Items Where** parameter determines the exact format you need:
	* When using **Value Is New**, this must be an input field or combination of fields with a unique ID.
	* When using **Value Is Higher than Any Previous Value**, this must be an input field or combination of fields that has an incremental value.
	* When using **Value Is a Date Later than Any Previous Date**, this must be an input field that has a date value in ISO format.

#### Remove Items Processed in Previous Executions options

When using the **Remove Items Processed in Previous Executions** operation, the following option is available:

* **Scope**: Sets how n8n stores and uses the deduplication data for comparisons. The following options are available:
	* **Node**: (default) Stores the data for this node independently from other Remove Duplicates instances in the workflow. When you use this scope, you can [clear the duplication history](#clear-deduplication-history) for this node instance without affecting other nodes.
	* **Workflow**: Stores the duplication data at the workflow level. This shares duplication data with any other Remove Duplicate nodes set to use "workflow" scope.  n8n will still manage the duplication data for other Remove Duplicate nodes set to "node" scope independently.

When you select **Value Is New** as your **Keep Items Where** choice, this option is also available:

* **History Size**: The number of items for n8n to store to track duplicates across executions. The value of the **Scope** option determines whether this history size is specific to this individual Remove Duplicate node instance or shared with other instances in the workflow. By default, n8n stores 10,000 items.

##### Clear Deduplication History

When you set the "Operation" field to **Clear Deduplication History**, the Remove Duplicates node manages and clears the stored items from previous executions. This operation doesn't affect any items in the current input. Instead, it manages the database of items that the "Remove Items Processed in Previous Executions" operation uses.

#### Clear Deduplication History parameters

When using the **Clear Deduplication History** operation, the following parameter is available:

* **Mode**: How you want to manage the key / value items stored in the database. The following option is available:
	* **Clean Database**: Deletes all duplication data stored in the database. This resets the duplication database to its original state.

#### Clear Deduplication History options

When using the **Clear Deduplication History** operation, the following option is available:

* **Scope**: Sets the scope n8n uses when managing the duplication database.
	* **Node**: (default) Manages the duplication database specific to this Remove Duplicates node instance.
	* **Workflow**: Manages the duplication database shared by all Remove Duplicate node instances that use workflow scope.

#### Templates and examples

For templates using the Remove Duplicates node and examples of how to use it, refer to [Templates and examples](/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/templates-and-examples.md).

#### Related resources

--8<-- "_snippets/integrations/builtin/core-nodes/data-transformation-actions/data-section-link.md"


---



## Index {#index}

*Source: docs/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/index.md*


##### Schedule Trigger node

Use the Schedule Trigger node to run workflows at fixed intervals and times. This works in a similar way to the Cron software utility in Unix-like systems.

/// note | You must activate the workflow
If a workflow uses the Schedule node as a trigger, make sure that you save and activate the workflow. 
///

--8<-- "_snippets/integrations/builtin/core-nodes/schedule/timezone-settings.md"

#### Node parameters

Add **Trigger Rules** to determine when the trigger should run.

Use the **Trigger Interval** to select the time interval unit of measure to schedule the trigger for. All other parameters depend on the interval you select. Choose from:

- [Seconds trigger interval](#seconds-trigger-interval)
- [Minutes trigger interval](#minutes-trigger-interval)
- [Hours trigger interval](#hours-trigger-interval)
- [Days trigger interval](#days-trigger-interval)
- [Weeks trigger interval](#weeks-trigger-interval)
- [Months trigger interval](#months-trigger-interval)
- [Custom (Cron) interval](#custom-cron-interval)

You can add multiple **Trigger Rules** to run the node on different schedules.

Refer to the sections below for more detail on configuring each **Trigger Interval**. Refer to [Templates and examples](#templates-and-examples) for further examples.

##### Seconds trigger interval

* **Seconds Between Triggers**: Enter the number of seconds between each workflow trigger. For example, if you enter `30` here, the trigger will run every 30 seconds.

##### Minutes trigger interval

* **Minutes Between Triggers**: Enter the number of minutes between each workflow trigger. For example, if you enter `5` here, the trigger will run every 5 minutes.

##### Hours trigger interval

* **Hours Between Triggers**: Enter the number of hours between each workflow trigger.
* **Trigger at Minute**: Enter the minute past the hour to trigger the node when it runs, from `0` to `59`.

For example, if you enter `6` **Hours Between Triggers** and `30` **Trigger at Minute**, the node will run every six hours at 30 minutes past the hour.

##### Days trigger interval

* **Days Between Triggers**: Enter the number of days between each workflow trigger.
* **Trigger at Hour**: Select the hour of the day to trigger the node.
* **Trigger at Minute**: Enter the minute past the hour to trigger the node when it runs, from `0` to `59`.

<!-- vale from-microsoft.AMPM = NO -->
For example, if you enter `2` **Days Between Triggers**, **9am** for **Trigger at Hour**, and `15` **Trigger at Minute**, the node will run every two days at 9:15am.
<!-- vale from-microsoft.AMPM = YES -->

##### Weeks trigger interval

* **Weeks Between Triggers**: Enter the number of weeks between each workflow trigger.
* **Trigger on Weekdays**: Select the day(s) of the week you want to trigger the node.
* **Trigger at Hour**: Select the hour of the day to trigger the node.
* **Trigger at Minute**: Enter the minute past the hour to trigger the node when it runs, from `0` to `59`.

For example, if you enter `2` **Weeks Between Triggers**, **Monday** for **Trigger on Weekdays**, **3pm** for **Trigger at Hour**, and `30` **Trigger at Minute**, the node will run every two weeks on Monday at 3:30 PM.

##### Months trigger interval

* **Months Between Triggers**: Enter the number of months between each workflow trigger.
* **Trigger at Day of Month**: Enter the day of the month the day should trigger at, from `1` to `31`. If a month doesn't have this day, the node won't trigger. For example, if you enter `30` here, the node won't trigger in February.
* **Trigger at Hour**: Select the hour of the day to trigger the node.
* **Trigger at Minute**: Enter the minute past the hour to trigger the node when it runs, from `0` to `59`.

For example, if you enter `3` **Months Between Triggers**, `28` **Trigger at Day of Month**, **9am** for **Trigger at Hour**, and `0` **Trigger at Minute**, the node will run each quarter on the 28th day of the month at 9:00 AM.

##### Custom (Cron) interval

Enter a custom cron **Expression** to set the schedule for the trigger.

To generate a Cron expression, you can use [crontab guru](https://crontab.guru){:target=_blank .external-link}. Paste the Cron expression that you generated using crontab guru in the **Expression** field in n8n.

#### Examples

<!-- vale from-write-good.Weasel = NO -->
|Type|Cron Expression|Description|
|---|---|---|
|Every X Seconds|`*/10 * * * * *`|Every 10 seconds.|
|Every X Minutes|`*/5 * * * *`|Every 5 minutes.|
|Hourly|`0 * * * *`|Every hour on the hour.|
|Daily|`0 6 * * *`|At 6:00 AM every day.|
|Weekly|`0 12 * * 1`|At noon every Monday.|
|Monthly|`0 0 1 * *`|At midnight on the 1st of every month.|
|Every X Days|`0 0 */3 * *`|At midnight every 3rd day.|
|Only Weekdays|`0 9 * * 1-5`|At 9:00 AM Monday through Friday.|
|Custom Hourly Range|`0 9-17 * * *`|Every hour from 9:00 AM to 5:00 PM every day.|
|Quarterly|`0 0 1 1,4,7,10 *`|At midnight on the 1st of January, April, July, and October.|
<!-- vale from-write-good.Weasel = YES -->

/// warning | Using variables in the Cron expression
While variables can be used in the scheduled trigger, their values only get evaluated when the workflow is activated. If you alter a variable's value in the settings after a workflow is activated, the changes won't alter the cron schedule. To re-evaluate the variable, set the workflow to **Inactive** and then back to **Active** again
/// 

#### Why there are six asterisks in the Cron expression

The sixth asterisk in the Cron expression represents seconds. Setting this is optional. The node will execute even if you don't set the value for seconds.

|  (*)  |  *  |  *  |  *  |  *  |  *  |
|:--:|:--:|:--:|:--:|:--:|:--:|
|(second)|minute|hour|day of month|month|day of week(Sun-Sat)|

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'schedule-trigger') ]]

#### Common issues

For common questions or issues and suggested solutions, refer to [Common Issues](/integrations/builtin/core-nodes/n8n-nodes-base.scheduletrigger/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/builtin/core-nodes/n8n-nodes-base.webhook/index.md*


##### Webhook node

Use the Webhook node to create [webhooks](https://en.wikipedia.org/wiki/Webhook){:target=_blank .external-link}, which can receive data from apps and services when an event occurs. It's a trigger node, which means it can start an n8n workflow. This allows services to connect to n8n and run a workflow.

You can use the Webhook node as a trigger for a workflow when you want to receive data and run a workflow based on the data. The Webhook node also supports returning the data generated at the end of a workflow. This makes it useful for building a workflow to process data and return the results, like an API endpoint.

The webhook allows you to trigger workflows from services that don't have a dedicated app trigger node.

#### Workflow development process

n8n provides different **Webhook URL**s for testing and production. The testing URL includes an option to **Listen for test event**. Refer to [Workflow development](/integrations/builtin/core-nodes/n8n-nodes-base.webhook/workflow-development.md) for more information on building, testing, and shifting your Webhook node to production.

#### Node parameters

Use these parameters to configure your node.

##### Webhook URLs

The Webhook node has two **Webhook URLs**: test and production. n8n displays the URLs at the top of the node panel.

Select **Test URL** or **Production URL** to toggle which URL n8n displays.

<figure markdown="span">
![Sample Webhook URLs in the Webhook node's Parameters tab display a Test URL and Production URL](/_images/integrations/builtin/core-nodes/webhook/webhook-urls.png)
<figcaption>Sample Webhook URLs in the Webhook node's Parameters tab</figcaption>
</figure>

* **Test**: n8n registers a test webhook when you select **Listen for Test Event** or **Execute workflow**, if the workflow isn't active. When you call the webhook URL, n8n displays the data in the workflow.
* **Production**: n8n registers a production webhook when you activate the workflow. When using the production URL, n8n doesn't display the data in the workflow. You can still view workflow data for a production execution: select the **Executions** tab in the workflow, then select the workflow execution you want to view.

##### HTTP Method

The Webhook node supports standard [HTTP Request Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods){:target=_blank .external-link}:

* DELETE
* GET
* HEAD
* PATCH
* POST
* PUT

    /// note | Webhook max payload
	The webhook maximum payload size is 16MB.
  If you're self-hosting n8n, you can change this using the [endpoint environment variable](/hosting/configuration/environment-variables/endpoints.md) `N8N_PAYLOAD_SIZE_MAX`.
	///	

##### Path

By default, this field contains a randomly generated webhook URL path, to avoid conflicts with other webhook nodes. 

You can manually specify a URL path, including adding route parameters. For example, you may need to do this if you use n8n to prototype an API and want consistent endpoint URLs.

The **Path** field can take the following formats:

- `/:variable`
- `/path/:variable`
- `/:variable/path`
- `/:variable1/path/:variable2`
- `/:variable1/:variable2`

##### Supported authentication methods

You can require authentication for any service calling your webhook URL. Choose from these authentication methods:

- Basic auth
- Header auth
- JWT auth
- None

Refer to [Webhook credentials](/integrations/builtin/credentials/webhook.md) for more information on setting up each credential type.

##### Respond

* **Immediately**: The Webhook node returns the response code and the message **Workflow got started**.
* **When Last Node Finishes**: The Webhook node returns the response code and the data output from the last node executed in the workflow.
* **Using 'Respond to Webhook' Node**: The Webhook node responds as defined in the [Respond to Webhook](/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook.md) node.

##### Response Code

Customize the [HTTP response code](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status){:target=_blank .external-link} that the Webhook node returns upon successful execution. Select from common response codes or create a custom code.

##### Response Data

Choose what data to include in the response body:

* **All Entries**: The Webhook returns all the entries of the last node in an array.
* **First Entry JSON**: The Webhook returns the JSON data of the first entry of the last node in a JSON object.
* **First Entry Binary**: The Webhook returns the binary data of the first entry of the last node in a binary file.
* **No Response Body**: The Webhook returns without a body.

Applies only to **Respond > When Last Node Finishes**.

#### Node options

Select **Add Option** to view more configuration options. The available options depend on your node parameters. Refer to the table for option availability.

* **Allowed Origins (CORS)**: Set the permitted cross-origin domains. Enter a comma-separated list of URLs allowed for cross-origin non-preflight requests. Use `*` (default) to allow all origins.
* **Binary Property**: Enabling this setting allows the Webhook node to receive binary data, such as an image or audio file. Enter the name of the binary property to write the data of the received file to.
* **Ignore Bots**: Ignore requests from bots like link previewers and web crawlers.
* **IP(s) Whitelist**: Enable this to limit who (or what) can invoke a Webhook trigger URL. Enter a comma-separated list of allowed IP addresses. Access from IP addresses outside the whitelist throws a 403 error. If left blank, all IP addresses can invoke the webhook trigger URL.
* **No Response Body**: Enable this to prevent n8n sending a body with the response.
* **Raw Body**: Specify that the Webhook node will receive data in a raw format, such as JSON or XML.
* **Response Content-Type**: Choose the format for the webhook body.
* **Response Data**: Send custom data with the response.
* **Response Headers**: Send extra headers in the Webhook response. Refer to [MDN Web Docs | Response header](https://developer.mozilla.org/en-US/docs/Glossary/Response_header){:target=_blank .external-link} to learn more about response headers.
* **Property Name**: by default, n8n returns all available data. You can choose to return a specific JSON key, so that n8n returns the value.

| Option | Required node configuration |
| ------ | --------------------------- | 
| Allowed Origins (CORS) | Any |
| Binary Property | Either: <br />HTTP Method > POST <br /> HTTP Method > PATCH <br /> HTTP Method > PUT |
| Ignore Bots | Any |
| IP(s) Whitelist | Any |
| Property Name | Both: <br /> Respond > When Last Node Finishes <br /> Response Data > First Entry JSON |
| No Response Body | Respond > Immediately |
| Raw Body | Any |
| Response Code | Any except Respond > Using 'Respond to Webhook' Node |
| Response Content-Type | Both: <br /> Respond > When Last Node Finishes <br /> Response Data > First Entry JSON |
| Response Data | Respond > Immediately |
| Response Headers | Any |

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'webhook') ]]

#### Common issues

For common questions or issues and suggested solutions, refer to [Common issues](/integrations/builtin/core-nodes/n8n-nodes-base.webhook/common-issues.md).


---



## Workflow Development {#workflow-development}

*Source: docs/integrations/builtin/core-nodes/n8n-nodes-base.webhook/workflow-development.md*


##### Workflow development

The [Webhook node](/integrations/builtin/core-nodes/n8n-nodes-base.webhook/index.md) works a bit differently from other core nodes. n8n recommends following these processes for building, testing, and using your Webhook node in production.

n8n generates two **Webhook URLs** for each Webhook node: a **Test URL** and a **Production URL**.

#### Build and test workflows

While building or testing a workflow, use the **Test** webhook URL.

Using a test webhook ensures that you can view the incoming data in the editor UI, which is useful for debugging. Select **Listen for test event** to register the webhook before sending the data to the test webhook. The test webhook stays active for 120 seconds.

When using the Webhook node on localhost on a [self-hosted](/hosting/index.md) n8n instance, run n8n in tunnel mode:

* [npm with tunnel](/hosting/installation/npm.md#n8n-with-tunnel)
* [Docker with tunnel](/hosting/installation/docker.md#n8n-with-tunnel)

<video src="/_video/integrations/builtin/core-nodes/webhook/webhook-node-intro.mp4" controls width="100%"></video>

#### Production workflows

When your workflow is ready, switch to using the **Production** webhook URL. You can then activate your workflow, and n8n runs it automatically when an external service calls the webhook URL.

When working with a Production webhook, ensure that you have saved and activated the workflow. Data flowing through the webhook isn't visible in the editor UI with the production webhook.

Refer to [Create a workflow](/workflows/create.md) for more information on activating workflows.


---



## Index {#index}

*Source: docs/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/index.md*


##### Chat Trigger node

Use the Chat Trigger node when building AI workflows for chatbots and other chat interfaces. You can configure how users access the chat, using one of n8n's provided interfaces, or your own. You can add authentication.

You must connect either an agent or chain [root node](/integrations/builtin/cluster-nodes/root-nodes/index.md).

/// warning | Workflow execution usage
Every message to the Chat Trigger executes your workflow. This means that one conversation where a user sends 10 messages uses 10 executions from your execution allowance. Check your payment plan for details of your allowance.
///

/// note | Manual Chat trigger
This node replaces the Manual Chat Trigger node from version 1.24.0.
///

#### Node parameters

##### Make Chat Publicly Available

Set whether the chat should be publicly available (turned on) or only available through the manual chat interface (turned off).

Leave this turned off while you're building the workflow. Turn it on when you're ready to activate the workflow and allow users to access the chat.

##### Mode

Choose how users access the chat. Select from:

* **Hosted Chat**: Use n8n's hosted chat interface. Recommended for most users because you can configure the interface using the [node options](#node-options) and don't have to do any other setup.
* **Embedded Chat**: This option requires you to create your own chat interface. You can use n8n's [chat widget](https://www.npmjs.com/package/@n8n/chat){:target=_blank .external-link} or build your own. Your chat interface must call the webhook URL shown in **Chat URL** in the node.

##### Authentication

Choose whether and how to restrict access to the chat. Select from:

* **None**: The chat doesn't use authentication. Anyone can use the chat.
* **Basic Auth**: The chat uses basic authentication.
	* Select or create a **Credential for Basic Auth** with a username and password. All users must use the same username and password.
* **n8n User Auth**: Only users logged in to an n8n account can use the chat.

##### Initial Message(s)

This parameter's only available if you're using **Hosted Chat**. Use it to configure the message the n8n chat interface displays when the user arrives on the page.

#### Node options

Available options depend on the chat mode.

##### Hosted chat options

#### Allowed Origin (CORS)

Set the origins that can access the chat URL. Enter a comma-separated list of URLs allowed for cross-origin non-preflight requests.

Use `*` (default) to allow all origins.

#### Input Placeholder, Title, and Subtitle

Enter the text for these elements in the chat interface.

??? Details "View screenshot"
	![Customizable text elements](/_images/integrations/builtin/core-nodes/chat-trigger/hosted-text-elements.png)

#### Load Previous Session

Select whether to load chat messages from a previous chat session.

If you select any option other than **Off**, you must connect the Chat trigger and the Agent you're using to a memory sub-node. The memory connector on the Chat trigger appears when you set **Load Previous Session** to **From Memory**. n8n recommends connecting both the Chat trigger and Agent to the same memory sub-node, as this ensures a single source of truth for both nodes.

??? Details "View screenshot"
	![Connect nodes to memory](/_images/integrations/builtin/core-nodes/chat-trigger/connect-memory.png)

#### Response Mode

Use this option when building a workflow with steps after the agent or chain that's handling the chat. Choose from:

* **When Last Node Finishes**: The Chat Trigger node returns the response code and the data output from the last node executed in the workflow.
* **Using 'Respond to Webhook' Node**: The Chat Trigger node responds as defined in the [Respond to Webhook](/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook.md) node.

#### Require Button Click to Start Chat

Set whether to display a **New Conversation** button on the chat interface (turned on) or not (turned off).

??? Details "View screenshot"
	![New Conversation button](/_images/integrations/builtin/core-nodes/chat-trigger/new-conversation-button.png)


##### Embedded chat options

#### Allowed Origin (CORS)

Set the origins that can access the chat URL. Enter a comma-separated list of URLs allowed for cross-origin non-preflight requests.

Use `*` (default) to allow all origins.

#### Load Previous Session

Select whether to load chat messages from a previous chat session.

If you select any option other than **Off**, you must connect the Chat trigger and the Agent you're using to a memory sub-node. The memory connector on the Chat trigger appears when you set **Load Previous Session** to **From Memory**. n8n recommends connecting both the Chat trigger and Agent to the same memory sub-node, as this ensures a single source of truth for both nodes.

??? Details "View screenshot"
	![Connect nodes to memory](/_images/integrations/builtin/core-nodes/chat-trigger/connect-memory.png)

#### Response Mode

Use this option when building a workflow with steps after the agent or chain that's handling the chat. Choose from:

* **When Last Node Finishes**: The Chat Trigger node returns the response code and the data output from the last node executed in the workflow.
* **Using 'Respond to Webhook' Node**: The Chat Trigger node responds as defined in the [Respond to Webhook](/integrations/builtin/core-nodes/n8n-nodes-base.respondtowebhook.md) node.

#### Templates and examples

<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget(page.title, 'chat-trigger') ]]

#### Related resources

--8<-- "_snippets/integrations/builtin/cluster-nodes/langchain-overview-link.md"

#### Set the chat response manually

You need to manually set the chat response when you don't want to directly send the output of an Agent or Chain node to the user. Instead, you want to take the output of an Agent or Chain node and modify it or do something else with it before sending it back to the user.

In a basic workflow, the Agent and Chain nodes output a parameter named either `output` or `text`, and the Chat trigger sends the value of this parameter to the user as the chat response. 

If you need to manually create the response sent to the user, you must create a parameter named either `text` or `output`. If you use a different parameter name, the Chat trigger sends the entire object as its response, not just the value.

#### Common issues

For common questions or issues and suggested solutions, refer to [Common Issues](/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/builtin/credentials/google/index.md*


##### Google credentials

This section contains:

* [OAuth2 single service](/integrations/builtin/credentials/google/oauth-single-service.md): Create an OAuth2 credential for a specific service node, such as the Gmail node.
* [OAuth2 generic](/integrations/builtin/credentials/google/oauth-generic.md): Create an OAuth2 credential for use with [custom operations](/integrations/custom-operations.md).
* [Service Account](/integrations/builtin/credentials/google/service-account.md): Create a [Service Account](https://cloud.google.com/iam/docs/service-account-overview){:target=_blank .external-link} credential for some specific service nodes.
* [Google PaLM and Gemini](/integrations/builtin/credentials/googleai.md): Get a Google Gemini/Google PaLM API key.


#### OAuth2 and Service Account

There are two authentication methods available for Google services nodes:

* [OAuth2](https://developers.google.com/identity/protocols/oauth2){:target=_blank .external-link}: Recommended because it's more widely available and easier to set up.
* [Service Account](https://cloud.google.com/iam/docs/understanding-service-accounts){:target=_blank .external-link}: Refer to the [Google documentation: Understanding service accounts](https://cloud.google.com/iam/docs/understanding-service-accounts){:target=_blank .external-link} for guidance on when you need a service account.

--8<-- "_snippets/integrations/managed-google-oauth.md"

#### Compatible nodes

Once configured, you can use your credentials to authenticate the following nodes. Most nodes are compatible with OAuth2 authentication. Support for Service Account authentication is limited.


| Node | OAuth | Service Account |
| :--- | :---: | :-------------: |
| [Google Ads](/integrations/builtin/app-nodes/n8n-nodes-base.googleads.md) | :white_check_mark: | :x: |
| [Gmail](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/index.md) | :white_check_mark: | :warning: |
| [Google Analytics](/integrations/builtin/app-nodes/n8n-nodes-base.googleanalytics.md) | :white_check_mark: | :x: |
| [Google BigQuery](/integrations/builtin/app-nodes/n8n-nodes-base.googlebigquery.md) | :white_check_mark: | :white_check_mark: |
| [Google Books](/integrations/builtin/app-nodes/n8n-nodes-base.googlebooks.md) | :white_check_mark: | :white_check_mark: |
| [Google Calendar](/integrations/builtin/app-nodes/n8n-nodes-base.googlecalendar/index.md) | :white_check_mark: | :x: |
| [Google Chat](/integrations/builtin/app-nodes/n8n-nodes-base.googlechat.md) | :x: | :white_check_mark: |
| [Google Cloud Storage](/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudstorage.md) | :white_check_mark: | :x: |
| [Google Contacts](/integrations/builtin/app-nodes/n8n-nodes-base.googlecontacts.md) | :white_check_mark: | :x: |
| [Google Cloud Firestore](/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudfirestore.md) | :white_check_mark: | :white_check_mark: |
| [Google Cloud Natural Language](/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudnaturallanguage.md) | :white_check_mark: | :x: |
| [Google Cloud Realtime Database](/integrations/builtin/app-nodes/n8n-nodes-base.googlecloudrealtimedatabase.md) | :white_check_mark: | :x: |
| [Google Docs](/integrations/builtin/app-nodes/n8n-nodes-base.googledocs.md) | :white_check_mark: | :white_check_mark: |
| [Google Drive](/integrations/builtin/app-nodes/n8n-nodes-base.googledrive/index.md) | :white_check_mark: | :white_check_mark: |
| [Google Drive Trigger](/integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger/index.md) | :white_check_mark: | :white_check_mark: |
| [Google Perspective](/integrations/builtin/app-nodes/n8n-nodes-base.googleperspective.md) | :white_check_mark: | :x: |
| [Google Sheets](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/index.md) | :white_check_mark: | :white_check_mark: |
| [Google Slides](/integrations/builtin/app-nodes/n8n-nodes-base.googleslides.md) | :white_check_mark: | :white_check_mark: |
| [Google Tasks](/integrations/builtin/app-nodes/n8n-nodes-base.googletasks.md) | :white_check_mark: | :x: |
| [Google Translate](/integrations/builtin/app-nodes/n8n-nodes-base.googletranslate.md) | :white_check_mark: | :white_check_mark: |
| [Google Workspace Admin](/integrations/builtin/app-nodes/n8n-nodes-base.gsuiteadmin.md) | :white_check_mark: | :x: |
| [YouTube](/integrations/builtin/app-nodes/n8n-nodes-base.youtube.md) | :white_check_mark: | :x: |

/// warning | Gmail and Service Accounts
Google technically supports Service Accounts for use with Gmail, but it requires enabling domain-wide delegation, which Google discourages, and its behavior can be inconsistent.

n8n recommends using OAuth2 with the Gmail node.
///


---



## Index {#index}

*Source: docs/integrations/builtin/credentials/imap/index.md*


##### IMAP credentials

You can use these credentials to authenticate the following nodes:

- [IMAP Email](/integrations/builtin/core-nodes/n8n-nodes-base.emailimap.md)

#### Prerequisites

Create an email account on a service with IMAP support.

#### Supported authentication methods

- User account

#### Related resources

Internet Message Access Protocol (IMAP) is a standard protocol for receiving email. Most email providers offer instructions on setting up their service with IMAP; refer to your provider's IMAP instructions.

#### Using user account

To configure this credential, you'll need:

- A **User** name: The email address you're retrieving email for.
- A **Password**: Either the password you use to check email or an app password. Your provider will tell you whether to use your own password or to generate an app password.
- A **Host**: The IMAP host address for your email provider, often formatted as `imap.<provider>.com`. Check with your provider.
- A **Port** number: The default is port `993`. Use this port unless your provider or email administrator tells you to use something different.

Choose whether to use **SSL/TLS** and whether to **Allow Self-Signed Certificates**.

##### Provider instructions

Refer to the quickstart guides for these common email providers.

#### Gmail

Refer to [Gmail](/integrations/builtin/credentials/imap/gmail.md).

#### Outlook.com

Refer to [Outlook.com](/integrations/builtin/credentials/imap/outlook.md).

#### Yahoo

Refer to [Yahoo](/integrations/builtin/credentials/imap/yahoo.md).

##### My provider isn't listed

If your email provider isn't listed here, search for their `IMAP settings` or `IMAP instructions`.


---



## Index {#index}

*Source: docs/integrations/builtin/credentials/index.md*


##### Credentials library

This section contains step-by-step information about authenticating the different nodes in n8n.

To learn more about creating, managing, and sharing credentials, refer to [Manage credentials](/credentials/index.md).




---



## Index {#index}

*Source: docs/integrations/builtin/credentials/sendemail/index.md*


##### Send Email credentials

You can use these credentials to authenticate the following nodes:

- [Send Email](/integrations/builtin/core-nodes/n8n-nodes-base.sendemail.md)

#### Prerequisites

- Create an email account on a service that supports SMTP.
- Some email providers require that you enable or set up outgoing SMTP or generate an app password. Refer to your provider's documentation to see if there are other required steps.

#### Supported authentication methods

- SMTP account

#### Related resources

Simple Message Transfer Protocol (SMTP) is a standard protocol for sending and receiving email. Most email providers offer instructions on setting up their service with SMTP. Refer to your provider's SMTP instructions.

#### Using SMTP account

To configure this credential, you'll need:

- A **User** email address
- A **Password**: This may be the user's password or an app password. Refer to the documentation for your email provider.
- The **Host**: The SMTP host address for your email provider, often formatted as `smtp.<provider>.com`. Check with your provider.
- A **Port** number: The default is port `465`, commonly used for SSL. Other common ports are `587` for TLS or `25` for no encryption. Check with your provider.
- **SSL/TLS**: When turned on, SMTP will use SSL/TLS.
- **Disable STARTTLS**: When SSL/TLS is disabled, the SMTP server can still try to [upgrade the TCP connection using STARTTLS](https://en.wikipedia.org/wiki/Opportunistic_TLS){:target=_blank .external-link}. Turning this on prevents that behaviour.
- **Client Host Name**: If needed by your provider, add a client host name. This name identifies the client to the server.

##### Provider instructions

Refer to the quickstart guides for these common email providers.

#### Gmail

Refer to [Gmail](/integrations/builtin/credentials/sendemail/gmail.md).

#### Outlook.com

Refer to [Outlook.com](/integrations/builtin/credentials/sendemail/outlook.md).

#### Yahoo

Refer to [Yahoo](/integrations/builtin/credentials/sendemail/yahoo.md).

##### My provider isn't listed

If your email provider isn't listed here, search for `SMTP settings` to find their instructions. (These instructions may also be included with `IMAP settings` or `POP settings`.)


---



## Index {#index}

*Source: docs/integrations/builtin/trigger-nodes/index.md*


##### Triggers library

This section provides information about [n8n's Triggers](/glossary.md#trigger-node-n8n).



---



## Index {#index}

*Source: docs/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/index.md*


##### Facebook Trigger node

[Facebook](https://www.facebook.com/){:target=_blank .external-link} is a social networking site to connect and share with family and friends online.

Use the Facebook Trigger node to trigger a workflow when events occur in Facebook.

/// note | Credentials
You can find authentication information for this node [here](/integrations/builtin/credentials/facebookapp.md).
///

///  note  | Examples and templates
For usage examples and templates to help you get started, refer to n8n's [Facebook Trigger integrations](https://n8n.io/integrations/facebook-trigger/){:target=_blank .external-link} page.
///

#### Objects

- [**Ad Account**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/ad-account.md): Get updates for certain ads changes.
- [**Application**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/application.md): Get updates sent to the application.
- [**Certificate Transparency**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/certificate-transparency.md): Get updates when new security certificates are generated for your subscribed domains, including new certificates and potential phishing attempts.
- Activity and events in a [**Group**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/group.md)
- [**Instagram**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/instagram.md): Get updates when someone comments on the Media objects of your app users; @mentions your app users; or when Stories of your app users expire.
- [**Link**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/link.md): Get updates about the links for rich previews by an external provider
- [**Page**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/page.md) updates
- [**Permissions**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/permissions.md): Updates when granting or revoking permissions
- [**User**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/user.md) profile updates
- [**WhatsApp Business Account**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/whatsapp.md)
    
    /// note | Use WhatsApp Trigger
    n8n recommends using the [WhatsApp Trigger node](/integrations/builtin/trigger-nodes/n8n-nodes-base.whatsapptrigger.md) with the [WhatsApp credentials](/integrations/builtin/credentials/whatsapp.md) instead of the Facebook Trigger node for these events. The WhatsApp Trigger node has more events to listen to.
    ///

- [**Workplace Security**](/integrations/builtin/trigger-nodes/n8n-nodes-base.facebooktrigger/workplace-security.md)

For each **Object**, use the **Field Names or IDs** dropdown to select more details on what data to receive. Refer to the linked pages for more details.

#### Related resources

View [example workflows and related content](https://n8n.io/integrations/facebook-trigger/){:target=_blank .external-link} on n8n's website.

Refer to Meta's [Graph API documentation](https://developers.facebook.com/docs/graph-api/webhooks/reference){:target=_blank .external-link} for details about their API.


---



## Index {#index}

*Source: docs/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/index.md*


##### Gmail Trigger node

[Gmail](https://www.gmail.com){:target=_blank .external-link} is an email service developed by Google. The Gmail Trigger node can start a workflow based on events in Gmail.

/// note | Credentials
You can find authentication information for this node [here](/integrations/builtin/credentials/google/index.md).
///

///  note  | Examples and templates
For usage examples and templates to help you get started, refer to n8n's [Gmail Trigger integrations](https://n8n.io/integrations/gmail-trigger/){:target=_blank .external-link} page.
///

#### Events

* **Message Received**: The node triggers for new messages at the selected **Poll Time**.

#### Node parameters

Configure the node with these parameters:

* **Credential to connect with**: Select or create a new Google credential to use for the trigger. Refer to [Google credentials](/integrations/builtin/credentials/google/index.md) for more information on setting up a new credential.
* **Poll Times**: Select a poll **Mode** to set how often to trigger the poll. Your **Mode** selection will add or remove relevant fields. Refer to [Poll Mode options](/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/poll-mode-options.md) to configure the parameters for each mode type.
* **Simplify**: Choose whether to return a simplified version of the response (turned on, default) or the raw data (turned off).
    * The simplified version returns email message IDs, labels, and email headers, including: From, To, CC, BCC, and Subject.

#### Node filters

Use these filters to further refine the node's behavior:

* **Include Spam and Trash**: Select whether the node should trigger on new messages in the Spam and Trash folders (turned on) or not (turned off).
* **Label Names or IDs**: Only trigger on messages with the selected labels added to them. Select the Label names you want to apply or enter an expression to specify IDs. The dropdown populates based on the **Credential** you selected.
* **Search**: Enter Gmail search refine filters, like `from:`, to trigger the node on the filtered conditions only. Refer to [Refine searches in Gmail](https://support.google.com/mail/answer/7190?hl=en){:target=_blank .external-link} for more information.
* **Read Status**: Choose whether to receive **Unread and read emails**, **Unread emails only** (default), or **Read emails only**.
* **Sender**: Enter an email or a part of a sender name to trigger only on messages from that sender.

#### Related resources

n8n provides an app node for Gmail. You can find the node docs [here](/integrations/builtin/app-nodes/n8n-nodes-base.gmail/index.md).

View [example workflows and related content](https://n8n.io/integrations/gmail-trigger/){:target=_blank .external-link} on n8n's website.

Refer to [Google's Gmail API documentation](https://developers.google.com/gmail/api/guides){:target=_blank .external-link} for details about their API.

#### Common issues

For common questions or issues and suggested solutions, refer to [Common issues](/integrations/builtin/trigger-nodes/n8n-nodes-base.gmailtrigger/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger/index.md*


##### Google Drive Trigger node

[Google Drive](https://drive.google.com){:target=_blank .external-link} is a file storage and synchronization service developed by Google. It allows users to store files on their servers, synchronize files across devices, and share files.

/// note | Credentials
You can find authentication information for this node [here](/integrations/builtin/credentials/google/index.md).
///

///  note  | Examples and templates
For usage examples and templates to help you get started, refer to n8n's [Google Drive Trigger integrations](https://n8n.io/integrations/google-drive-trigger/){:target=_blank .external-link} page.
///

/// note | Manual Executions vs. Activation
On manual executions this node will return the last event matching its search criteria. If no event matches the criteria (for example because you are watching for files to be created but no files have been created so far), an error is thrown. Once saved and activated, the node will regularly check for any matching events and will trigger your workflow for each event found.
///

#### Common issues

For common questions or issues and suggested solutions, refer to [Common issues](/integrations/builtin/trigger-nodes/n8n-nodes-base.googledrivetrigger/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/index.md*


##### Google Sheets Trigger node

[Google Sheets](https://www.google.com/sheets){:target=_blank} is a web-based spreadsheet program that's part of Google's office software suite within its Google Drive service.

/// note | Credentials
You can find authentication information for this node [here](/integrations/builtin/credentials/google/index.md).
///

///  note  | Examples and templates
For usage examples and templates to help you get started, refer to n8n's [Google Sheets Trigger integrations](https://n8n.io/integrations/google-sheets-trigger/){:target=_blank .external-link} page.
///

#### Events

* Row added
* Row updated
* Row added or updated

#### Related resources

Refer to [Google Sheet's API documentation](https://developers.google.com/sheets/api){:target=_blank .external-link} for more information about the service.

n8n provides an app node for Google Sheets. You can find the node docs [here](/integrations/builtin/app-nodes/n8n-nodes-base.googlesheets/index.md).

View [example workflows and related content](https://n8n.io/integrations/google-sheets-trigger/){:target=_blank .external-link} on n8n's website.

#### Common issues

For common questions or issues and suggested solutions, refer to [Common issues](/integrations/builtin/trigger-nodes/n8n-nodes-base.googlesheetstrigger/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/index.md*


##### Telegram Trigger node

[Telegram](https://telegram.org/){:target=_blank .external-link} is a cloud-based instant messaging and voice over IP service. Users can send messages and exchange photos, videos, stickers, audio, and files of any type. On this page, you'll find a list of events the Telegram Trigger node can respond to and links to more resources.

/// note | Credentials
You can find authentication information for this node [here](/integrations/builtin/credentials/telegram.md).
///

///  note  | Examples and templates
For usage examples and templates to help you get started, refer to n8n's [Telegram Trigger integrations](https://n8n.io/integrations/telegram-trigger/){:target=_blank .external-link} page.
///

#### Events

- **`*`**: All updates except "Chat Member", "Message Reaction", and "Message Reaction Count" (default behavior of Telegram API as they produces a lot of calls of updates).
- **Business Connection**: Trigger when the bot is connected to or disconnected from a business account, or a user edited an existing connection with the bot.
- **Business Message**: Trigger on a new message from a connected business account.
- **Callback Query**: Trigger on new incoming callback query.
- **Channel Post**: Trigger on new incoming channel post of any kind — including text, photo, sticker, and so on.
- **Chat Boost**: Trigger when a chat boost is added or changed. The bot must be an administrator in the chat to receive these updates.
- **Chat Join Request**: Trigger when a request to join the chat is sent. The bot must have the `can_invite_users` administrator right in the chat to receive these updates.
- **Chat Member**: Trigger when a chat member's status is updated. The bot must be an administrator in the chat.
- **Chosen Inline Result**: Trigger when the result of an inline query chosen by a user is sent. Please see Telegram's API documentation on [feedback collection](https://core.telegram.org/bots/inline#collecting-feedback) for details on how to enable these updates for your bot.
- **Deleted Business Messages**: Trigger when messages are deleted from a connected business account.
- **Edited Business Message**: Trigger on new version of a message from a connected business account.
- **Edited Channel Post**: Trigger on new version of a channel post that is known to the bot is edited.
- **Edited Message**: Trigger on new version of a channel post that is known to the bot is edited.
- **Inline Query**: Trigger on new incoming inline query.
- **Message**: Trigger on new incoming message of any kind — text, photo, sticker, and so on.
- **Message Reaction**: Trigger when a reaction to a message is changed by a user. The bot must be an administrator in the chat. The update isn't received for reactions set by bots.
- **Message Reaction Count**: Trigger when reactions to a message with anonymous reactions are changed. The bot must be an administrator in the chat. The updates are grouped and can be sent with delay up to a few minutes.
- **My Chat Member**: Trigger when the bot's chat member status is updated in a chat. For private chats, this update is received only when the bot is blocked or unblocked by the user.
- **Poll**: Trigger on new poll state. Bots only receive updates about stopped polls and polls which are sent by the bot.
- **Poll Answer**: Trigger when user changes their answer in a non-anonymous poll. Bots only receive new votes in polls that were sent by the bot itself.
- **Pre-Checkout Query**: Trigger on new incoming pre-checkout query. Contains full information about checkout.
- **Purchased Paid Media**: Trigger when a user purchases paid media with a non-empty payload sent by the bot in a non-channel chat.
- **Removed Chat Boost**: Trigger when a boost is removed from a chat. The bot must be an administrator in the chat to receive these updates.
- **Shipping Query**: Trigger on new incoming shipping query. Only for invoices with flexible price.

Some **events may require additional permissions**, see [Telegram's API documentation](https://core.telegram.org/bots/api#getting-updates) for more information.

#### Options

- **Download Images/Files**: Whether to download attached images or files to include in the output data.
	- **Image Size**: When you enable **Download Images/Files**, this configures the size of image to download. Downloads large images by default.
- **Restrict to Chat IDs**: Only trigger for events with the listed chat IDs. You can include multiple chat IDs separated by commas.
- **Restrict to User IDs**: Only trigger for events with the listed user IDs. You can include multiple user IDs separated by commas.

#### Related resources

n8n provides an app node for Telegram. You can find the node docs [here](/integrations/builtin/credentials/telegram.md).

View [example workflows and related content](https://n8n.io/integrations/telegram-trigger/){:target=_blank .external-link} on n8n's website.

Refer to [Telegram's API documentation](https://core.telegram.org/bots/api){:target=_blank .external-link} for details about their API.

#### Common issues

For common questions or issues and suggested solutions, refer to [Common issues](/integrations/builtin/trigger-nodes/n8n-nodes-base.telegramtrigger/common-issues.md).


---



## Index {#index}

*Source: docs/integrations/community-nodes/installation/index.md*


##### Install and manage community nodes

There are three ways to install community nodes:

* Within n8n using the [nodes panel](/integrations/community-nodes/installation/verified-install.md) (for verified community nodes only).
* Within n8n [using the GUI](/integrations/community-nodes/installation/gui-install.md): Use this method to install community nodes from the npm registry.
* [Manually from the command line](/integrations/community-nodes/installation/manual-install.md): use this method to install community nodes from npm if your n8n instance doesn't support installation through the in-app GUI.

/// note | Installing from npm only available on self-hosted instances
Unverified community nodes aren't available on n8n cloud and require [self-hosting](/hosting/index.md) n8n.
///


---



## Index {#index}

*Source: docs/integrations/creating-nodes/build/index.md*


##### Build a node

This section provides tutorials on building nodes. It covers:

* [Tutorial: Build a declarative-style node](/integrations/creating-nodes/build/declarative-style-node.md)
* [Reference](/integrations/creating-nodes/build/reference/index.md) material on [file structure](/integrations/creating-nodes/build/reference/node-file-structure.md), parameter definitions for [base](/integrations/creating-nodes/build/reference/node-base-files/index.md), [codex](/integrations/creating-nodes/build/reference/node-codex-files.md), and [credentials](/integrations/creating-nodes/build/reference/credentials-files.md) files, [node UI elements](/integrations/creating-nodes/build/reference/ui-elements.md), and more.

Coming soon:

* More tutorials
* Revised guidance on standards

<!--
* [Build a programmatic-style node](/integrations/creating-nodes/build/programmatic-style-node.md)
* [Build a trigger node](/integrations/creating-nodes/build/create-trigger-node/)


If you are unsure which tutorial to use, refer to [Choose your node building approach](/integrations/creating-nodes/plan/choose-node-method.md) to understand the different styles of node building.

-->




---



## Index {#index}

*Source: docs/integrations/creating-nodes/build/reference/index.md*


##### Node building reference

This section contains reference information, including details about:

* [Node UI elements](/integrations/creating-nodes/build/reference/ui-elements.md)
* [Organizing your node files](/integrations/creating-nodes/build/reference/node-file-structure.md)
* Key parameters in your node's [base file](/integrations/creating-nodes/build/reference/node-base-files/index.md) and [credentials file](/integrations/creating-nodes/build/reference/credentials-files.md).
* [UX guidelines](/integrations/creating-nodes/build/reference/ux-guidelines.md) and [verification guidelines](/integrations/creating-nodes/build/reference/verification-guidelines.md) for submitting your node for [verification by n8n](/integrations/community-nodes/installation/verified-install.md).


---



## Index {#index}

*Source: docs/integrations/creating-nodes/build/reference/node-base-files/index.md*


##### Node base file

The node base file contains the core code of your node. All nodes must have a base file. The contents of this file are different depending on whether you're building a declarative-style or programmatic-style node. For guidance on which style to use, refer to [Choose your node building approach](/integrations/creating-nodes/plan/choose-node-method.md).

These documents give short code snippets to help understand the code structure and concepts. For full walk-throughs of building a node, including real-world code examples, refer to [Build a declarative-style node](/integrations/creating-nodes/build/declarative-style-node.md) or [Build a programmatic-style node](/integrations/creating-nodes/build/programmatic-style-node.md).

You can also explore the [n8n-nodes-starter](https://github.com/n8n-io/n8n-nodes-starter){:target=_blank .external-link} and n8n's own [nodes](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes){:target=_blank .external-link} for a wider range of examples. The starter contains basic examples that you can build on. The n8n [Mattermost node](https://github.com/n8n-io/n8n/tree/master/packages/nodes-base/nodes/Mattermost) is a good example of a more complex programmatic-style node, including versioning.

For all nodes, refer to the:

* [Structure of the node base file](/integrations/creating-nodes/build/reference/node-base-files/structure.md)
* [Standard parameters](/integrations/creating-nodes/build/reference/node-base-files/standard-parameters.md)

For declarative-style nodes, refer to the:

* [Declarative-style parameters](/integrations/creating-nodes/build/reference/node-base-files/declarative-style-parameters.md)

For programmatic-style nodes, refer to the:

* [Programmatic-style parameters](/integrations/creating-nodes/build/reference/node-base-files/programmatic-style-parameters.md)
* [Programmatic-style execute() method](/integrations/creating-nodes/build/reference/node-base-files/programmatic-style-execute-method.md)

---



## Index {#index}

*Source: docs/integrations/creating-nodes/deploy/index.md*


##### Deploy a node

This section contains details on how to deploy and share your node.

You can choose to:

* [Submit your node to the community node repository](/integrations/creating-nodes/deploy/submit-community-nodes.md). This makes it available for everyone to use, and allows you to [install and use it](/integrations/community-nodes/installation/index.md) like any other community node. This is the only way to use custom nodes on cloud.
* Install the node into your n8n instance as a [private node](/integrations/creating-nodes/deploy/install-private-nodes.md).


---



## Index {#index}

*Source: docs/integrations/creating-nodes/plan/index.md*


##### Plan a node

This section provides guidance on designing your node, including key technical decisions such as choosing your node building style.

When building a node, there are design choices you need to make before you start:

* Which [node type](/integrations/creating-nodes/plan/node-types.md) you need to build.
* Which [node building style](/integrations/creating-nodes/plan/choose-node-method.md) to use.
* Your [UI design and UX principles](/integrations/creating-nodes/plan/node-ui-design.md)
* Your node's [file structure](/integrations/creating-nodes/build/reference/node-file-structure.md).


---



## Index {#index}

*Source: docs/integrations/creating-nodes/test/index.md*


##### Test a node

This section contains information about testing your node.

There are two ways to test your node:

* Manually, by [running it on your own machine](/integrations/creating-nodes/test/run-node-locally.md) within a local n8n instance.
* Automatically, using the [linter](/integrations/creating-nodes/test/node-linter.md).

You should use both methods before publishing your node.


---



## Index {#index}

*Source: docs/integrations/index.md*


##### Integrations

n8n calls integrations nodes.

Nodes are the building blocks of workflows in n8n. They're an entry point for retrieving data, a function to process data, or an exit for sending data. The data process includes filtering, recomposing, and changing data. There can be one or several nodes for your API, service or app. You can connect multiple nodes, which allows you to create complex workflows.

#### Built-in nodes

n8n includes a collection of built-in integrations. Refer to [Built-in nodes](/integrations/builtin/node-types.md) for documentation on all n8n's built-in nodes.

#### Community nodes

As well as using the built-in nodes, you can also install community-built nodes. Refer to [Community nodes](/integrations/community-nodes/installation/index.md) for more information.

#### Credential-only nodes and custom operations

--8<-- "_snippets/integrations/credential-only-intro.md"

Refer to [Custom operations](/integrations/custom-operations.md) for more information.

#### Generic integrations

If you need to connect to a service where n8n doesn't have a node, or a credential-only node, you can still use the [HTTP Request](/integrations/builtin/core-nodes/n8n-nodes-base.httprequest/index.md) node. Refer to the node page for details on how to set up authentication and create your API call.

#### Where to go next

* If you want to create your own node, head over to the [Creating Nodes](/integrations/creating-nodes/overview.md) section.
* Check out [Community nodes](/integrations/community-nodes/usage.md) to learn about installing and managing community-built nodes.
* If you'd like to learn more about the different nodes in n8n, their functionalities and example usage, check out n8n's node libraries: [Core nodes](/integrations/builtin/core-nodes/index.md), [Actions](/integrations/builtin/app-nodes/index.md), and [Triggers](/integrations/builtin/trigger-nodes/index.md).
* If you'd like to learn how to add the credentials for the different nodes, head over to the [Credentials](/integrations/builtin/credentials/index.md) section.


---



## Index {#index}

*Source: docs/privacy-security/index.md*

<!-- vale off -->
##### Privacy and security at n8n

n8n is committed to the privacy and security of your data. This section outlines how n8n handles and secures data. This isn't an exhaustive list of practices, but an overview of key policies and procedures.

If you have any questions related to data privacy, email privacy@n8n.io. 

If you have any security-related questions, or if you want to report a suspected vulnerability, email security@n8n.io.

[[% import "_macros/section-toc.html" as sectionToc %]]

[[ sectionToc.sectionToc(page) ]]

<!-- vale on -->


---



## Index {#index}

*Source: docs/source-control-environments/index.md*


##### Source control and environments

--8<-- "_snippets/source-control-environments/feature-availability.md"

n8n uses Git-based source control to support environments. Linking your n8n instances to a Git repository lets you create multiple n8n environments, backed by Git branches.

In this section:

* [Understand](/source-control-environments/understand/index.md):
	* [Environments in n8n](/source-control-environments/understand/environments.md): The purpose of environments, and how they work in n8n.
	* [Git and n8n](/source-control-environments/understand/git.md): How n8n uses Git. 
	* [Branch patterns](/source-control-environments/understand/patterns.md): The possible relationships between n8n instances and Git branches.
* [Set up source control for environments](/source-control-environments/setup.md): How to connect your n8n instance to Git.
* [Using](/source-control-environments/using/index.md):
	* [Push and pull](/source-control-environments/using/push-pull.md): Send work to Git, and fetch work from Git to your instance.
	* [Copy work between environments](/source-control-environments/using/copy-work.md): How to copy work between different n8n instances.
* [Tutorial: Create environments with source control](/source-control-environments/create-environments.md): An end-to-end tutorial, setting up environments using n8n's recommended configurations.

Related sections:

* [Variables](/code/variables.md): reusable values.
* [External secrets](/external-secrets.md): manage [credentials](/glossary.md#credential-n8n) with an external secrets vault.


---



## Index {#index}

*Source: docs/source-control-environments/understand/index.md*


##### Understand source control and environments

--8<-- "_snippets/source-control-environments/feature-availability.md"

* [Environments in n8n](/source-control-environments/understand/environments.md): The purpose of environments, and how they work in n8n.
* [Git in n8n](/source-control-environments/understand/git.md): How n8n uses Git. 
* [Branch patterns](/source-control-environments/understand/patterns.md): The possible relationships between n8n instances and Git branches.


---



## Index {#index}

*Source: docs/source-control-environments/using/index.md*


##### Using source control and environments

--8<-- "_snippets/source-control-environments/feature-availability.md"

* [Push and pull](/source-control-environments/using/push-pull.md): Send work to Git, and fetch work from Git to your instance. Understand what gets committed, and how n8n handles merge conflicts.
* [Copy work between environments](/source-control-environments/using/copy-work.md): How to copy work between different n8n instances.


---



## Index {#index}

*Source: docs/try-it-out/index.md*


##### Try it out

The best way to learn n8n is by using our tutorials to get familiar with the user interface and the many different types of nodes and integrations available. Here is a selection of material to get you started:

- Looking for a quick introduction? Check out the ["First Workflow" tutorial](/try-it-out/tutorial-first-workflow.md).
- Interested in what you could do with AI? Find out [how to build an AI chat agent with n8n](/advanced-ai/intro-tutorial.md).
- Prefer to work through extensive examples? Maybe the [courses](/courses/index.md) are for you.


---



## Quickstart {#quickstart}

*Source: docs/try-it-out/quickstart.md*


##### The very quick quickstart

This quickstart gets you started using n8n as quickly as possible. Its allows you to try out the UI and introduces two key features: [workflow templates](/glossary.md#template-n8n) and [expressions](/glossary.md#expression-n8n). It doesn't include detailed explanations or explore concepts in-depth.

In this tutorial, you will:

* Load a [workflow](/glossary.md#workflow-n8n) from the workflow templates library
* Add a node and configure it using expressions
* Run your first workflow

#### Step one: Sign up for n8n

This quickstart uses [n8n Cloud](/manage-cloud/overview.md). A free trial is available for new users. If you haven't already done so, [sign up](https://app.n8n.cloud/register) for an account now.

#### Step two: Open a workflow template

n8n provides a quickstart template using training nodes. You can use this to work with fake data and avoid setting up [credentials](/glossary.md#credential-n8n).

1. Go to [Templates | Very quick quickstart](https://n8n.io/workflows/1700-very-quick-quickstart/).
1. Select **Use workflow** to view the options for using the template.
1. Select **Import template to <name> cloud workspace** to load the template into your Cloud instance.

This workflow:

1. Gets example data from the [Customer Datastore](/integrations/builtin/app-nodes/n8n-nodes-base.n8ntrainingcustomerdatastore.md) node.
2. Uses the [Edit Fields](/integrations/builtin/core-nodes/n8n-nodes-base.set.md) node to extract only the desired data and assigns that data to variables. In this example, you map the customer name, ID, and description.

The individual pieces in an n8n workflow are called [nodes](/glossary.md#node-n8n). Double click a node to explore its settings and how it processes data.

#### Step three: Run the workflow

Select **Test Workflow**. This runs the workflow, loading the data from the Customer Datastore node, then transforming it with Edit Fields. You need this data available in the workflow so that you can work with it in the next step.

#### Step four: Add a node

Add a third node to message each customer and tell them their description. Use the Customer Messenger node to send a message to fake recipients.

1. Select the **Add node** <span class="inline-image">![Add node icon](/_images/try-it-out/add-node-small.png){.off-glb}</span> connector on the Edit Fields node.
2. Search for **Customer Messenger**. n8n shows a list of nodes that match the search.
3. Select **Customer Messenger (n8n training)** to add the node to the [canvas](/glossary.md#canvas-n8n). n8n opens the node automatically.
4. Use [expressions](/code/expressions.md) to map in the **Customer ID** and create the **Message**:
	1. In the **INPUT** panel select the **Schema** tab.
	2. Drag **Edit Fields1** > **customer_id** into the **Customer ID** field in the node settings.
    2. Hover over **Message**. Select the **Expression** tab, then select the expand button <span class="inline-image">![Add node icon](/_images/common-icons/open-expression-editor.png){.off-glb}</span> to open the full expressions editor.
    3. Copy this expression into the editor:
        ```
        Hi {{ $json.customer_name }}. Your description is: {{ $json.customer_description }}
        ```
5. Close the expressions editor, then close the **Customer Messenger** node by clicking outside the node or selecting **Back to canvas**.
6. Select **Test Workflow**. n8n runs the workflow.

The complete workflow should look like this:

[[ workflowDemo("file:///try-it-out/quickstart/very-quick-quickstart-workflow.json") ]]


#### Next steps

* Read n8n's [longer try it out tutorial](/try-it-out/tutorial-first-workflow.md) for a more complex workflow, and an introduction to more features and n8n concepts.
* Take the [text courses](/courses/index.md) or [video courses](/video-courses.md).




---



## Index {#index}

*Source: docs/user-management/index.md*


##### User management

User management in n8n allows you to invite people to work in your n8n instance. It includes:

* Login and password management
* Adding and removing users
* Three [account types](/user-management/account-types.md): **Owner** and **Member** (and **Admin** for Pro & Enterprise plans)

/// note | Privacy
The user management feature doesn't send personal information, such as email or username, to n8n.
///
#### Setup guides
<!-- vale off -->
This section contains most usage information for user management, and the [Cloud setup guide](/user-management/cloud-setup.md). If you self-host n8n, there are extra steps to configure your n8n instance. Refer to the [Self-hosted guide](/hosting/configuration/user-management-self-hosted.md).
<!-- vale on -->
This section includes guides to configuring [LDAP](/user-management/ldap.md) and [SAML](/user-management/saml/index.md) in n8n.


---



## Index {#index}

*Source: docs/user-management/rbac/index.md*


##### Role-based access control (RBAC)

/// info | Feature availability
RBAC is available on all plans except the Community edition. Different plans have different numbers of projects and roles. Refer to n8n's [pricing page](https://n8n.io/pricing/){:target=_blank .external-link} for plan details.
///

/// note | Role types and account types
Role types and [account types](/user-management/account-types.md) are different things. Every account has one type. The account can have different role types for different [projects](/user-management/rbac/projects.md).
///

RBAC is a way of managing access to workflows and [credentials](/glossary.md#credential-n8n) based on user roles and projects. You group workflows into projects, and user access depends on the user's project role. This section provides guidance on using RBAC in n8n.

[[% import "_macros/section-toc.html" as sectionToc %]]

[[ sectionToc.sectionToc(page) ]]







---



## Index {#index}

*Source: docs/user-management/saml/index.md*


##### Security Assertion Markup Language (SAML)

--8<-- "_snippets/user-management/saml-overview.md"


---



## Connections {#connections}

*Source: docs/workflows/components/connections.md*


##### Connections

A connection establishes a link between nodes to route data through the workflow. A connection between two nodes passes data from one node's output to another node's input.

![Example of creating and deleting a connection](/_images/workflows/components/connections/example.gif)

#### Create a connection

To create a connection between two nodes, select the grey dot or **Add node** <span class="inline-image">![Add node icon](/_images/try-it-out/add-node-small.png){.off-glb}</span> on the right side of a node and slide the arrow to the grey rectangle on the left side of the following node.

#### Delete a connection

Hover over the connection, then select **Delete** <span class="inline-image">![Delete connector icon](/_images/common-icons/delete-connector.png){.off-glb}</span>.




---



## Index {#index}

*Source: docs/workflows/components/index.md*


##### Workflow components

This section contains:

* [Nodes](/workflows/components/nodes.md): integrations and operations.
* [Connections](/workflows/components/connections.md): node connectors.
* [Sticky notes](/workflows/components/sticky-notes.md): document your workflows.


---



## Nodes {#nodes}

*Source: docs/workflows/components/nodes.md*


##### Nodes

[Nodes](/glossary.md#node-n8n) are the key building blocks of a [workflow](/glossary.md#workflow-n8n). They perform a range of actions, including:

* Starting the workflow.
* Fetching and sending data.
* Processing and manipulating data.

n8n provides a collection of built-in nodes, as well as the ability to create your own nodes. Refer to:

* [Built-in integrations](/integrations/builtin/node-types.md) to browse the node library.
* [Community nodes](/integrations/community-nodes/installation/index.md) for guidance on finding and installing community-created nodes.
* [Creating nodes](/integrations/creating-nodes/overview.md) to start building your own nodes.


#### Add a node to your workflow

##### Add a node to an empty workflow

1. Select **Add first step**. n8n opens the nodes panel, where you can search or browse [trigger nodes](/glossary.md#trigger-node-n8n).
2. Select the trigger you want to use.

    /// note | Choose the correct app event
	If you select **On App Event**, n8n shows a list of all the supported services. Use this list to browse n8n's integrations and trigger a workflow in response to an event in your chosen service. Not all integrations have triggers. To see which ones you can use as a trigger, select the node. If a trigger is available, you'll see it at the top of the available operations list.

	For example, this is the trigger for Asana:

	![Screenshot of the Asana node operations list, showing the Recommended section at the top of the list](/_images/workflows/components/nodes/recommended-trigger.png)
	///

##### Add a node to an existing workflow

Select the **Add node** <span class="inline-image">![Add node icon](/_images/try-it-out/add-node-small.png){.off-glb}</span> connector. n8n opens the nodes panel, where you can search or browse all nodes.

--8<-- "_snippets/integrations/builtin/node-operations.md"

#### Node controls

To view node controls, hover over the node on the canvas:

* **Execute step** <span class="inline-image">![Execute step icon](/_images/common-icons/play-node.png){.off-glb}</span>: Run the node.
* **Deactivate** <span class="inline-image">![Deactivate node icon](/_images/common-icons/power-off.png){.off-glb}</span>: Deactivate the node.
* **Delete** <span class="inline-image">![Delete node icon](/_images/common-icons/delete-node.png){.off-glb}</span>: Delete the node.
* **Node context menu** <span class="inline-image">![Node context menu icon](/_images/common-icons/node-context-menu.png){.off-glb}</span>: Select node actions. Available actions:
	* Open node
	* Execute step
	* Rename node
	* Deactivate node
	* Pin node
	* Copy node
	* Duplicate node
	* Select all
	* Clear selection
	* Delete node

#### Node settings

The node settings under the **Settings** tab allow you to control node behaviors and add node notes.

When active or set, they do the following:

* **Request Options**: Select **Add Option** to view and select these options. 
	- **Batching**: Control how to batch large numbers of input items.
	- **Ignore SSL Issues**: Download the response even if SSL validation isn't possible.
	- **Proxy**: Use this if you need to specify an HTTP proxy.
	- **Timeout**: Set a timeout for the request in ms. 
* **Always Output Data**: The node returns an empty item even if the node returns no data during execution. Be careful setting this on IF nodes, as it could cause an infinite loop.
* **Execute Once**: The node executes once, with data from the first item it receives. It doesn't process any extra items.
* **Retry On Fail**: When an execution fails, the node reruns until it succeeds. 
* **On Error**: 
    - **Stop Workflow**: Halts the entire workflow when an error occurs, preventing further node execution.
    - **Continue**: Proceeds to the next node despite the error, using the last valid data.
    - **Continue (using error output)**: Continues workflow execution, passing error information to the next node for potential handling.

You can document your workflow using node notes:

* **Notes**: Note to save with the node.
* **Display note in flow**: If active, n8n displays the note in the workflow as a subtitle.


---



## Sticky Notes {#sticky-notes}

*Source: docs/workflows/components/sticky-notes.md*


##### Sticky Notes

Sticky Notes allow you to annotate and comment on your workflows.

n8n recommends using Sticky Notes heavily, especially on [template workflows](/glossary.md#template-n8n), to help other users understand your workflow.

![Screenshot of a basic workflow with an example sticky note](/_images/workflows/components/stickies/example-sticky-note.png)

#### Create a Sticky Note

Sticky Notes are a core node. To add a new Sticky Note:

1. Open the nodes panel.
2. Search for `note`.
3. Click the **Sticky Note** node. n8n adds a new Sticky Note to the canvas.

#### Edit a Sticky Note

1. Double click the Sticky Note you want to edit.
2. Write your note. [This guide](https://commonmark.org/help/) explains how to format your text with Markdown. n8n uses [markdown-it](https://github.com/markdown-it/markdown-it), which implements the CommonMark specification. 
3. Click away from the note, or press `Esc`, to stop editing.

#### Change the color

To change the Sticky Note color:

1. Hover over the Sticky Note
1. Select **Change color** <span class="inline-image">![Change Sticky Note color icon](/_images/common-icons/change-color.png){.off-glb}</span>

#### Sticky Note positioning

You can:

* Drag a Sticky Note anywhere on the canvas.
* Drag Sticky Notes behind nodes. You can use this to visually group nodes.
* Resize Sticky Notes by hovering over the edge of the note and dragging to resize.
* Change the color: select **Options** <span class="inline-image">![Options icon](/_images/common-icons/three-dot-options-menu.png){.off-glb}</span> to open the color selector.

#### Writing in Markdown

Sticky Notes support Markdown formatting. This section describes some common options.

```
The text in double asterisks will be **bold**

The text in single asterisks will be *italic*

Use # to indicate headings:
##### This is a top-level heading
#### This is a sub-heading
##### This is a smaller sub-heading

You can add links:
[Example](https://example.com/)

Create lists with asterisks:

* Item one
* Item two

Or created ordered lists with numbers:

1. Item one
2. Item two
```

For a more detailed guide, refer to [CommonMark's help](https://commonmark.org/help/). n8n uses [markdown-it](https://github.com/markdown-it/markdown-it), which implements the CommonMark specification.

#### Make images full width

You can force images to be 100% width of the sticky note by appending `#full-width` to the filename:

```markdown
![Source example](https://<IMAGE-URL>/<IMAGE-NAME>.png#full-width)
```


---



## All Executions {#all-executions}

*Source: docs/workflows/executions/all-executions.md*


##### All executions

To view **all executions** from an n8n instance, navigate to the **Overview** page and then click into the Executions tab. This will show you all executions from the workflows you have access to.

If your n8n instance supports **projects**, you'll also be able to view the executions tab within projects you have access to. This will show you executions only from the workflows within the specified project.

/// note | Deleted workflows
When you delete a workflow, n8n deletes its execution history as well. This means you can't view executions for deleted workflows.
///

#### Filter executions

You can filter the executions list:

1. Select the **Executions** tab either from within the **Overview** page or a specific **project** to open the list.
2. Select **Filters**.
3. Enter your filters. You can filter by:
	* **Workflows**: choose all workflows, or a specific workflow name.
	* **Status**: choose from **Failed**, **Running**, **Success**, or **Waiting**.
	* **Execution start**: see executions that started in the given time.
	* **Saved custom data**: this is data you create within the workflow using the Code node. Enter the key and value to filter. Refer to [Custom executions data](/workflows/executions/custom-executions-data.md) for information on adding custom data.

--8<-- "_snippets/workflows/executions/custom-execution-data-availability.md"

#### Retry failed workflows

If your workflow execution fails, you can retry the execution. To retry a failed workflow:

1. Select the **Executions** tab from within either the **Overview** page or a specific **project** to open the list. 
2. On the execution you want to retry, select **Retry execution** <span class="inline-image">![Options menu icon](/_images/common-icons/three-dot-options-menu.png){.off-glb}</span>.
--8<-- "_snippets/workflows/executions/retry-options.md"

#### Load data from previous executions into your current workflow

You can load data from a previous workflow back into the canvas. Refer to [Debug executions](/workflows/executions/debug.md) for more information.


---



## Custom Executions Data {#custom-executions-data}

*Source: docs/workflows/executions/custom-executions-data.md*


##### Custom executions data

You can set custom data on your workflow using the Code node or the [Execution Data node](/integrations/builtin/core-nodes/n8n-nodes-base.executiondata.md). n8n records this with each execution. You can then use this data when filtering the executions list, or fetch it in your workflows using the Code node.

--8<-- "_snippets/workflows/executions/custom-execution-data-availability.md"

#### Set and access custom data using the Code node

This section describes how to set and access data using the Code node. Refer to [Execution Data node](/integrations/builtin/core-nodes/n8n-nodes-base.executiondata.md) for information on using the Execution Data node to set data. You can't retrieve custom data using the Execution Data node.

##### Set custom executions data

Set a single piece of extra data:

=== "JavaScript"
	```js
	$execution.customData.set("key", "value");
	```
=== "Python"
	```python
	_execution.customData.set("key", "value");
	```

Set all extra data. This overwrites the whole custom data object for this execution:

=== "JavaScript"
	```js
	$execution.customData.setAll({"key1": "value1", "key2": "value2"})
	```
=== "Python"
	```python
	_execution.customData.setAll({"key1": "value1", "key2": "value2"})
	```

There are limitations:

* They must be strings
* `key` has a maximum length of 50 characters
* `value` has a maximum length of 255 characters
* n8n supports a maximum of 10 items of custom data

##### Access the custom data object during execution

You can retrieve the custom data object, or a specific value in it, during an execution:

<!-- vale off -->
=== "JavaScript"
	```js
	// Access the current state of the object during the execution
	const customData = $execution.customData.getAll();

	// Access a specific value set during this execution
	const customData = $execution.customData.get("key");
	```
=== "Python"
	```python
	# Access the current state of the object during the execution
	customData = _execution.customData.getAll();

	# Access a specific value set during this execution
	customData = _execution.customData.get("key");
	```
<!-- vale on -->


---



## Debug {#debug}

*Source: docs/workflows/executions/debug.md*


##### Debug and re-run past executions

/// info | Feature availability
Available on n8n Cloud and registered Community plans.
///

You can load data from a previous execution into your current workflow. This is useful for debugging data from failed production executions: you can see a failed execution, make changes to your workflow to fix it, then re-run it with the previous execution data.

#### Load data

To load data from a previous execution:

1. In your workflow, select the **Executions** tab to view the **Executions** list.
1. Select the execution you want to debug. n8n displays options depending on whether the workflow was successful or failed:
	* For failed executions: select **Debug in editor**.
	* For successful executions: select **Copy to editor**.
1. n8n copies the execution data into your current workflow, and [pins the data](/data/data-pinning.md) in the first node in the workflow.

/// note | Check which executions you save
The executions available on the **Executions** list depends on your [Workflow settings](/workflows/settings.md).
///


---



## Index {#index}

*Source: docs/workflows/executions/index.md*


##### Executions

An execution is a single run of a workflow.

#### Execution modes

There are two execution modes:

* Manual: run workflows manually when testing. Select **Test Workflow** to start a manual execution. You can do manual executions of active workflows, but n8n recommends keeping your workflow set to **Inactive** while developing and testing.
* Production: a production workflow is one that runs automatically. To enable this, set the workflow to **Active**.


#### Execution lists

n8n provides two execution lists:

* [Workflow-level executions](/workflows/executions/single-workflow-executions.md): this execution list shows the executions for a single workflow.
* [All executions](/workflows/executions/all-executions.md): this list shows all executions for all your workflows.

n8n supports [adding custom data to executions](/workflows/executions/custom-executions-data.md).


---



## Manual Partial And Production Executions {#manual-partial-and-production-executions}

*Source: docs/workflows/executions/manual-partial-and-production-executions.md*


##### Manual, partial, and production executions

There are some important differences in how n8n executes workflows manually (by clicking the **Test Workflow** button) and automatically (when the workflow is **Active** and triggered by an event or schedule).

#### Manual executions

Manual executions allow you to run workflows directly from the [canvas](/glossary.md#canvas-n8n) to test your workflow logic. These executions are "ad-hoc": they run only when you manually select the **Execute workflow** button.

Manual executions make building workflows easier by allowing you to iteratively test as you go, following the flow logic and seeing data transformations. You can test conditional branching, data formatting changes, and loop behavior by providing different input items and modifying node options.

/// note | Pinning execution data
When performing manual executions, you can use [data pinning](/data/data-pinning.md) to "pin" or "freeze" the output data of a node. You can optionally [edit the pinned data](https://docs.n8n.io/data/data-editing/) as well.

On future runs, instead of executing the pinned node, n8n will substitute the pinned data and continue following the flow logic. This allows you to iterate without operating on variable data or repeating queries to external services. Production executions ignore all pinned data.
///

#### Partial executions

Clicking the **Execute workflow** button at the bottom of the workflow in the **Editor** tab manually runs the entire workflow. You can also perform partial executions to run specific steps in your workflow. Partial executions are manual executions that only run a subset of your workflow nodes.

To perform a partial execution, select a node, open its detail view, and select **Execute step**. This executes the specific node and any preceding nodes required to fill in its input data. You can also temporarily disable specific nodes in the workflow chain to avoid interacting with those services while building.

In particular, partial executions are useful when updating the logic of a specific node since they allow you to re-execute the node with the same input data.

##### Troubleshooting partial executions

Some common issues you might come across when running partial executions include the following:

<!-- vale from-microsoft.Contractions = NO -->
> The destination node is not connected to any trigger. Partial executions need a trigger.
<!-- vale from-microsoft.Contractions = YES -->

This error message appears when you try to perform a partial execution without connecting the workflow to a trigger. Manual executions, including partial executions, attempt to mimic production executions when possible. Part of this includes requiring a trigger node to describe when the workflow logic should execute.

To work around this, connect a trigger node to the workflow with the node you're trying to execute. Most often, a [manual trigger](/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger.md) is the simplest option.

> Please execute the whole workflow, rather than just the node. (Existing execution data is too large.)

This error can appear when performing partial executions on workflows with large numbers of branches. Partial executions involve sending data and workflow logic to the n8n backend in a way that isn't required for full executions. This error occurs when your workflow exceeds the maximum size allowed for these messages.

To work around this, consider using the [limit node](/integrations/builtin/core-nodes/n8n-nodes-base.limit.md) to limit node output while running partial executions. Once the workflow is running as intended, you can disable or delete the limit node before enabling production execution.

#### Production executions

Production executions occur when a triggering event or schedule automatically runs a workflow.

To configure production executions, you must attach a [trigger node](/glossary.md#trigger-node-n8n) (any trigger other than the [manual trigger](/integrations/builtin/core-nodes/n8n-nodes-base.manualworkflowtrigger.md) works) and switch workflow's toggle to **Active**. Once activated, the workflow automatically executes whenever the trigger condition occurs.

The execution flow for production executions doesn't display in the Editor tab of the workflow as with manual executions. Instead, you can see executions in the workflow's **Executions** tab according to your [workflow settings](/workflows/settings.md). From there, you can explore and troubleshoot problems using the [debug in editor feature](/workflows/executions/debug.md).


---



## Single Workflow Executions {#single-workflow-executions}

*Source: docs/workflows/executions/single-workflow-executions.md*


##### Workflow-level executions list

The **Executions** list in a workflow shows all executions for that workflow.

/// note | Deleted workflows
When you delete a workflow, n8n deletes its execution history as well. This means you can't view executions for deleted workflows.
///

/// note | Execution history and workflow history
Don't confuse the execution list with [Workflow history](/workflows/history.md).

Executions are workflow runs. With the executions list, you can see previous runs of the current version of the workflow. You can copy previous executions into the editor to [Debug and re-run past executions](/workflows/executions/debug.md) in your current workflow.

Workflow history is previous versions of the workflow: for example, a version with a different node, or different parameters set.
///


#### View executions for a single workflow

In the workflow, select the **Executions** tab in the top menu. You can preview all executions of that workflow.

#### Filter executions

You can filter the executions list.

1. In your workflow, select **Executions**.	
2. Select **Filters**.
3. Enter your filters. You can filter by:
	* **Status**: choose from **Failed**, **Running**, **Success**, or **Waiting**.
	* **Execution start**: see executions that started in the given time.
	* **Saved custom data**: this is data you create within the workflow using the Code node. Enter the key and value to filter. Refer to [Custom executions data](/workflows/executions/custom-executions-data.md) for information on adding custom data.

		--8<-- "_snippets/workflows/executions/custom-execution-data-availability.md"


#### Retry failed workflows

If your workflow execution fails, you can retry the execution. To retry a failed workflow:

1. Open the **Executions** list.
2. For the workflow execution you want to retry, select **Refresh** <span class="inline-image">![Refresh icon](/_images/common-icons/refresh.png){.off-glb}</span>.
--8<-- "_snippets/workflows/executions/retry-options.md"


---



## Index {#index}

*Source: docs/workflows/index.md*


##### Workflows

A [workflow](/glossary.md#workflow-n8n) is a collection of nodes connected together to automate a process.


* [Create](/workflows/create.md) a workflow.
* Use [Workflow templates](/workflows/templates.md) to help you get started.
* Learn about the key [components](/workflows/components/index.md) of an automation in n8n.
* Debug using the [Executions](/workflows/executions/index.md) list.
* [Share](/workflows/sharing.md) workflows between users.

If it's your first time building a workflow, you may want to use the [quickstart guides](/try-it-out/index.md) to quickly try out n8n features.


---



## Workflow Id {#workflow-id}

*Source: docs/workflows/workflow-id.md*


##### Find your workflow ID

Your workflow ID is available in:

* The URL of the open workflow.
* The workflow settings title.


---



## Index {#index}

*Source: docs-site-feature-tests/index.md*

##### Feature tests

Use this section to quickly check all docs site features are working when upgrading the theme.

For theme upgrade instructions, refer to Notion.

#### Snippets

You should see an info box about the embed license:

--8<-- "_snippets/embed-license.md"

#### Admonitions

/// note | This is a note
This is some note contents.
///

/// info | This is an info box
This is some info contents.
///

/// warning | This is a warning
This is some warning contents.
///

/// tip | This is a tip
This is some tip contents.
///

/// danger | This is a danger box
This is some danger box contents.
///

??? Details "This is an expanding details box"
	This is some expanding details contents.

#### Images

##### Inline images

Inline images like this should **not** expand on click: <span class="inline-image">![Add node icon](/_images/try-it-out/add-node-small.png){.off-glb}</span>

If it expands on click, first check that the `off-glb` class has been applied. Refer to [MkDocs GLightbox | Disable by image](https://blueswen.github.io/mkdocs-glightbox/disable/image/){:target=_blank .external-link} for more information.

##### Other images

Other images like this should expand on click:

![Screenshot of completed quickstart workflow](/_images/try-it-out/tutorial-first.png)

#### Links

[This link should open in a new tab](https://example.com/)

[This link should open in the same tab](/try-it-out/quickstart.md)

#### Instant previews

[This link should show a preview of the quickstart on hover](/try-it-out/quickstart.md){ data-preview }

[This link should NOT show a preview on hover](/try-it-out/quickstart.md)

#### Embed Workflow

You should see an interactive workflow, similar to the templates pages or forum.
[[ workflowDemo("https://api.n8n.io/workflows/templates/655") ]]

#### Templates Widget

You should see a list of three Wait node templates, followed by links to the integrations page on the website, and the templates search.
<!-- see https://www.notion.so/n8n/Pull-in-templates-for-the-integrations-pages-37c716837b804d30a33b47475f6e3780 -->
[[ templatesWidget('wait', 'wait') ]]

#### Templates Widget Extra Items

You should see a list of 5 HTTP Request templates
[[ templatesWidget('HTTP Request', 'http-request', 5) ]]

#### Glossary

You should see the AI Glossary below

--8<-- "_glossary/ai-glossary.md"

Link to [workflows](/glossary.md#workflow-n8n) glossary definition with preview.


---



## Readme {#readme}

*Source: styles/from-write-good/README.md*

Based on [write-good](https://github.com/btford/write-good).

> Naive linter for English prose for developers who can't write good and wanna learn to do other stuff good too.

```
The MIT License (MIT)

Copyright (c) 2014 Brian Ford

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```


---

