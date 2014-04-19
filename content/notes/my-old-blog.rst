Migrating Tech Blog
###################

:date: 2014-02-15 06:10:00

There are 2 reasons why I decided to migrate my blog from django to pelican.
Firstly, my old blog engine has too many feature
such as comments, pingback, trackback, rss & feed, archives, widget, API, etc.
However as time goes by I realize some of these features 
are less valuable in my blog. Although, it is good to have them, 
but I find they can also become a barrier to achieve the main goal.
Rather than having these extra features, 
I would rather put more focus on the content.
Another stupid reason why I start a new blog is because 
I host my old blog at my EC2 server which cost a lot of money. 
The server cost me about $20 monthly.
For these reason, I decided to migrate from django to pelican, 
which is cheaper and focus on the content 

My old blogs own a domain eugene-yeo.me. 
However I have migrated the blog to eugene-yeo.in.
Thus, all request will be redirected to the new blog.

With this new blog, I communicate to other developer easily. 
All I need to worry is the content, and I wrote this in plain text.
Writing content in plaintext allows me to focus on the content 
without distraction from the aesthetic elements.
Now the idea of share and transfer my knowledge to others become easier. 

Using pelican is relatively cheap. 
Because of the nature of static site (just bunch of html,css,js file), 
it is possible for it to be hosted on almost any file server or 
any file hosting, such as amazon s3, github, etc...  and 
the cost for hosting this files are relatively valuable. 
For example, hosting in S3, I just need to pay
less then a dollar monthly for less than a megabyte. 
I could also host it on github, which probably free as of now.
So, for a cheaper blog hosting, you may want to host your blog with pelican
or any other static file site..

If you're curious about this technology, then checkout Pelican. 
It is a static site generator written in python. 
It is relatively easy to use at least for me.
Happy Reading.
