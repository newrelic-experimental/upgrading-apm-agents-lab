---
slug: deploy-your-first-app
id: omokgpv13tne
type: challenge
title: Deploy Your First App
teaser: Deploy an app instrumented with APM.
notes:
- type: text
  contents: |
    # Deploy your first app

    Please wait while all of the resources for the course are created.
    This might be a good time to get your New Relic License Key ready.
tabs:
- title: Terminal
  type: terminal
  hostname: docker-vm
  workdir: /root/labsrc/apps/simple-example
- title: Source Code Editor
  type: code
  hostname: docker-vm
  path: /root/labsrc/apps/simple-example
difficulty: basic
timelimit: 600
---

Deploy Your First App
=======================

In this challenge, you'll be configuring an application with your New Relic license key, building it, and deploying it.



Configure
=========

To the left, you'll see a tab named "Source Code Editor".  You can see all of the files that are part of a simple web service named "Hello New Relic" Feel free to examine the code to get and understanding of how the application works

Take a look at the `package.json` file.  You can see that the New Relic agent has already been installed for you.

Next, open up the `docker-compose.yml` file.  This is the specification for how the application will be deployed.  Docker Compose provides the functionality to set environment variables in the environment where containers are run.  In this case, the app name is set by an environment variable.

Knowing what you do about using [environment variables](https://docs.newrelic.com/docs/apm/agents/nodejs-agent/installation-configuration/nodejs-agent-configuration/#environment) to configure the agent, use one here to set the license key for the agent.

Build
=====
Now, build the app by running the following command in the Terminal tab:
```
build.sh
```
It may take a few minutes the first time your run it as all the dependencies are downloaded.

Deploy
======
Once the app is done building, deploy it by running the following command in the terminal:
```
deploy.sh
```

After a few moments, you should see a service in New Relic One named "Hello New Relic"

Takeaways:
==========
 - In this challenge, we configured and deployed a service instrumented with APM *using only environment variables*, we did not have to edit any source code in the application.  Think about how you could advise your customers to do the same.

🏁 Finish
=========

To complete the
challenge, press **Check**."
