# n8n Core Reference (Ultra-Condensed)

## Quick Reference

- **Expressions**: Use `{{ }}` for JavaScript expressions
- **Variables**: `$json` (current node data), `$node['NodeName'].json` (other node data)
- **Code Node**: Write JavaScript or Python in workflows
- **HTTP Request**: Make API calls with built-in auth
- **Webhook**: Create endpoints to trigger workflows

---


---

## Expressions cookbook

This section contains examples and recipes for tasks you can do with [expressions](/glossary.md#expression-n8n).

/// note | Python support
You can use Python in the Code node. It isn't available in expressions.
///
[[% import "_macros/section-toc.html" as sectionToc %]]

[[ sectionToc.sectionToc(page) ]]


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

---

## Workflow Values {#workflow-values}

*Source: _snippets/integrations/builtin/cluster-nodes/langchain-sub-nodes/workflow-values.md*

Set values to pass to the workflow you're calling.

These values appear in the output data of the trigger node in the workflow you call. You can access these values in expressions in the workflow. For example, if you have:

* **Workflow Values** with a **Name** of `myCustomValue`
* A workflow with an Execute Sub-workflow Trigger node as its trigger

The expression to access the value of `myCustomValue` is `{{ $('Execute Sub-workflow Trigger').item.json.myCustomValue }}`.


---




---

## HTTP Request node

The HTTP Request node is one of the most versatile nodes in n8n. It allows you to make HTTP requests to query data from any app or service with a REST API. You can use the HTTP Request node a regular node or attached to an [AI agent](/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent.md) to use as a [tool](/advanced-ai/examples/understand-tools.md){ data-preview }.

When using this node, you're creating a REST API call. You need some understanding of basic API terminology and concepts.

There are two ways to create an HTTP request: configure the [node parameters](#node-parameters) or [import a curl command](#import-curl-command).

/// note | Credentials
Refer to [HTTP Request credentials](/integrations/builtin/credentials/httprequest.md) for guidance on setting up authentication. 
///


---

## Webhook node

Use the Webhook node to create [webhooks](https://en.wikipedia.org/wiki/Webhook){:target=_blank .external-link}, which can receive data from apps and services when an event occurs. It's a trigger node, which means it can start an n8n workflow. This allows services to connect to n8n and run a workflow.

You can use the Webhook node as a trigger for a workflow when you want to receive data and run a workflow based on the data. The Webhook node also supports returning the data generated at the end of a workflow. This makes it useful for building a workflow to process data and return the results, like an API endpoint.

The webhook allows you to trigger workflows from services that don't have a dedicated app trigger node.


---

