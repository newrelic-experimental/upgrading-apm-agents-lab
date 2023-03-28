---
slug: using-a-build-tool
id: pyuxa3x8rczc
type: challenge
title: Using a Build Tool
teaser: Use gradle to download and install the New Relic Agent.
notes:
- type: text
  contents: With languages like Java, the New Relic agent is not part of the application
    itself.  This provides nearly unlimited options to install and configure it.
tabs:
- title: Application Editor
  type: code
  hostname: docker-vm
  path: /root/labsrc/apps/build-tool-example
- title: Agent Editor
  type: code
  hostname: docker-vm
  path: /tmp/newrelic
- title: Terminal
  type: terminal
  hostname: docker-vm
  workdir: /root/labsrc/apps/build-tool-example
difficulty: basic
timelimit: 600
---

Background
==========
In this challenge, we're going to use the same tool we use to build our application, gradle, to download and install the New Relic Agent.

Use the Application Editor tab to open up the file `build.gradle`.  This is the specification for how gradle will build, configure, and run our application.

Notice line `5`: we are including a plugin that will allows us to download any file and save it to the filesystem.  Line `30` is where we use that plugin to download the New Relic agent.  Notice that we are always downloading the most current version, and saving it to the same place: `/tmp/newrelic`, which exists outside of our application.  This means that _installing and upgrading the agent follow the exact same process_.

Finally, on line `40`, notice how we are passing an argument `-javaagent` to our application when we run it.  The value will always be set to `/tmp/newrelic/newrelic.jar`.  As long as our agent can be found there, the application will use it.  This also means that we can distribute and configure the agent independenty of the application.

Build
=====
Build the application by running the following command in the Terminal tab:
```
./gradlew build
```

Download the Agent
==================
Before downloading the agent, open up the "Agent Editor" tab.  It is showing us the contents of `/tmp/newrelic` which should be empty.

Now run this command to install the agent:
```
./gradlew downloadNewrelic
```
When it finishes downloading, run this command to extract it:
```
./gradlew unzipNewrelic
```

Take a look in the "Agent Editor" tab again.  You should see the contents of the New Relic agent.

Configure the Agent
===================
Since the agent lives separately from our application, we're going to use the traditional method of editing `newrelic.yml` to configure the agent.  We can make this edits without hacing to alter the source code or distribution asset of the application.

Go ahead and edit `newrelic.yml`, adding your license key and application name.

Run the Application
===================
Start the application by running the following command:
```
./gradlew bootRun
```

Takeaways
=========
- Think about the options you have for distributing the New Relic agent, such as tools like Ansible, Chef, or Puppet.  As long as every host has the New Relic agent available in `/tmp/newrelic`, our application will be fully instrumented.
