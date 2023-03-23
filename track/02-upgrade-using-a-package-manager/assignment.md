---
slug: upgrade-using-a-package-manager
type: challenge
title: Upgrade Using a Package Manager
teaser: Upgrade the New Relic agent using npm
notes:
- type: text
  contents: |
    # Upgrade Using a Package manager

    Now, we'll upgrade the New Relic agent by changing the version in the package manager.
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

Verify
=======
Your Hello New Relic app should appear in New Relic One by now.  Open up Agent Groundskeeper and see what it says.  It should be telling you that the agent is outdated, and will recommend a more recent version for you.  Remember this version number (or copy it to your clipboard).

Upgrade
=======
Open up the `package.json` file in the Source Code Editor.  Each library is specified in the `dependencies` section, where each library name is listed, followed by a colon (:) and then the version of the library, in quotes.

You should see that the version of the `newrelic` library matches what Agent Groundskeeper detected.   Replace this version with the one recommended by Agent Groundskeeper.

Build
=====
Now, build the app by running the following command in the Terminal tab:
```
build.sh
```

Deploy
======
Once the app is done building, deploy it by running the following command in the terminal:
```
deploy.sh
```

After a few minutes, return to Agent Groundskeeper to see if the new version is detected. (You may see BOTH versions reporting at first, since the old version was just recently replaced)

Takeaways:
==========
- In this challenge, we upgraded the New Relic APM agent by updating the version in the `package.json` file, which is the specification for NPM, the default *package manager* for NodeJS.

🏁 Finish
=========

To complete the
challenge, press **Check**."