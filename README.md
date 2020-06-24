## This project is to using docker
This isn't running for me due to a few errors. I was able to get the server going by replacing the content of your Dockerfile with the Dockerfile from the class demo. Right now, Docker doesn't really care that you're using poetry as your package manager.

Once the Dockerfile lets you run the server, you're going to have to modify the date time aspects of your models. They were causing issues for me when I got the server running.

I see that you have permissions in the file, but it's not preventing me from seeing the API as an unauthenticated user.

For full credit, get it all working. You may resubmit.