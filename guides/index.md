---
layout: default
title: Guides
---

I'm a collector. I collect step-by-step instructions for doing 'makey' things. For example: step by step instructions for installing Python 2.7 and writing your first script. Instructions on how to download a schematic capture tool and capture your first circuit.

# Schematic Capture#

[TinyCad Installation and Schematic Capture Tutorial]({{ site.baseurl }}/guides/tinycad.html)

# Miscellaneous How-To's#

<ul class="post-list">
    {% for post in site.posts %}
	{% if post.categories contains 'how-to' %}
	<li>
		<a href="{{ post.url }}">{{ post.title }}</a>
	</li>
	{% endif %}
    {% endfor %}
  </ul>