---
slug: deploy-a-set-of-microservices
type: challenge
title: Deploy a Set of Microservices
teaser: Using Docker Compose, we'll deploy several services at once.
notes:
- type: text
  contents: Using Docker Compose, we'll deploy several services at once.
tabs:
- title: Source Code Editor
  type: code
  hostname: docker-vm
  path: /root/labsrc/apps/multi-service
- title: Terminal
  type: terminal
  hostname: docker-vm
  workdir: /root/labsrc/apps/multi-service
difficulty: basic
timelimit: 600
---


Configure
=========

In the Source Code Editor, you'll set that this time, we're working with THREE services, named Serivce A, Service B, and Service C, respectively.

Open up the `docker-compose.yml` file.  You should recognize the convention here.  Although, this time, we have to add our license key to three services instead of one.

Remember to save your changes by clicking the icon next to the filename in the tab.

Build
=====
Now, build the apps by running the following command in the Terminal tab:
```
./build.sh
```
It may take a few minutes the first time your run it as all the dependencies are downloaded.

Deploy
======
Once the apps are done building, deploy them by running the following command in the terminal:
```
deploy.sh
```

After a few moments, you should see three service in New Relic One named Service A", "Service B", and "Service C"

Takeaways:
==========
 - In this challenge, we configured and deployed 3 services using Docker Compose
🏁 Finish
=========

To complete the
challenge, press **Check**."
