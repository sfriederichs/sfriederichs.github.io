---
layout: default
permalink: /blog/
title: Blog
---

<div class="home">

 
  <ul class="post-list">
    {% assign blogposts = site.posts | sort: 'updated' | reverse %}
    {% for post in site.posts %}
      <li>
        <span class="post-meta">
		Dated: {{ post.date | date: "%b %-d, %Y" }}
		</span> 
        <h2>
          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        </h2>
      </li>
    {% endfor %}
  
  </ul>

  <p class="rss-subscribe">subscribe <a href="{{ "/feed.xml" | prepend: site.baseurl }}">via RSS</a></p>

</div>
