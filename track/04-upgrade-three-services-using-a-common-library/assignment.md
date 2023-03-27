---
slug: upgrade-three-services-using-a-common-library
id: 7mlgxpwzzha1
type: challenge
title: Upgrade Three Services Using a Common Library
teaser: Follow some common patterns and best practices to streamline agent upgrades.
notes:
- type: text
  contents: Many organizations will use the intrinsic properties of _transitive dependencies_
    to simplify their deployments.  This allows them to standardize on versions of
    software like web servers and tools like New Relic.  By including a shared library
    in their code, individual teams are guaranteed to be running approved and/or supported
    versions of all of their external dependencies.
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

Verify
=======
 Open up Agent Groundskeeper and view the status of your new serviceas.  Again, remember or copy the recommended version for them.

Upgrade
=======
Open up the `package.json` file for each service in the Source Code Editor.  Notice that none of the services specifies a dependency on New Relic.  Instead, they all share a single dependency and _that_ library, in turn, depends on New Relic.  Can you find it?  You should be able to update all three services at once with a single edit.

Remember to save your changes by clicking the icon next to the filename in the tab.

Build
=====
Now, build the app by running the following command in the Terminal tab:
```
./build.sh
```

Deploy
======
Once the app is done building, deploy it by running the following command in the terminal:
```
./deploy.sh
```

Note:  sometimes resources are not destroyed and re-created in the correct order when redeploying and you may see the following error:

```
Recreating simple-example_web_1 ... error

ERROR: for simple-example_web_1  Cannot start service web: network simple-example_default not found

ERROR: for web  Cannot start service web: network simple-example_default not found
ERROR: Encountered errors while bringing up the project.
```

In that case, just re-run the deploy command and it should work.

After a few minutes, refresh Agent Groundskeeper to see if the new version is detected. (You may see BOTH versions reporting at first, since the old version was just recently replaced)

Takeaways:
==========
- In this challenge, we upgraded the New Relic APM agent across *multiple* services by updating a single line of code in a *shared library*.
- Think about how you could help you customer navigate to the right spot to perform a similar upgrade
- Similarly, think about how you could advise a customer to optimize their dependency on New Relic to make future upgrades easier.
- Although this example uses NodeJS, the principle applies to all of the other supported language agents as well.

🏁 Finish
=========

To complete the
challenge, press **Check**."
