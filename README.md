# 2. TerminoloGit Hackathon - TermX Workshop

This document deals with the installation of [TermX](https://termx.org/), an open-source knowledge development, management and sharing platform that also includes a terminology server, model designer, transformation editor and other authoring and publishing tools.

## Before You Start

1. Make sure that you have installed [Docker](https://www.docker.com/). In case you are not allowed to use [Docker Desktop](https://www.docker.com/products/docker-desktop/) you can use one of the following free alternatives:
    - [Rancher Desktop](https://rancherdesktop.io/)
    - [Podman](https://podman.io/)
2. Open `server.env` and adapt the `SNOWSTORM_*` properties to match the TerminoloGit Hackathon settings.
3. Open `web.env` and adapt the `SNOWSTORM_URL` property to match the TerminoloGit Hackathon settings
4. Run `docker-compose up -d` to startup `TermX`
5. Run `docker-compose logs --follow` to monitor the startup logs.
6. Access [localhost:4200](http://localhost:4200) on the browser of your choice
7. Continue as `Guest` since you have all the privileges anyway!
8. **Important:** Do not use the `login` button because User Authentication is not enabled!
