---
layout: default
permalink: /blog/
title: Blog
---

<div class="home">

 
  <ul class="post-list">
    {% assign blogposts = site.posts | sort: 'updated' | reverse %}
    {% for post in blogposts %}
      <li>

        <span class="post-meta">
		{% if post.update-abstract == nil %}
		Dated: 
		{% else %}
		Updated: 
		{% endif %}
		{{ post.updated | date: "%b %-d, %Y" }}</span> 
        <h2>
          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>

        </h2>
        {% if post.update-abstract %}
        <span class="post-abstract">{{ post.update-abstract }}</span>
        {% endif %}

      </li>
    {% endfor %}
  
  </ul>

  <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>

</div>
