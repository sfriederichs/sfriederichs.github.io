---
layout: default
title: Best-Practices
---

I make lots of mistakes - but so does everyone right? The first step to learning from your mistakes is to document the mistake and the solution. The next step is figuring out how to remind yourself that you've solved this problem before the next time it rears its ugly head. I don't have a solution to that one yet. Baby steps....

So, this is a collection of mistakes I've made and the solutions: I call it my 'Best Practices'. You might also call it 'Lessons Learned' or 'Hey Idiot Don't Do This Dumb Thing Again' but I prefer to stay positive.

# Miscellaneous Best-Practices #

<ul class="post-list">
    {% for post in site.posts %}
	{% if post.categories contains 'best-practices' %}
	<li>
		<a href="{{ post.url }}">{{ post.title }}</a>
	</li>
	{% endif %}
    {% endfor %}
  </ul>