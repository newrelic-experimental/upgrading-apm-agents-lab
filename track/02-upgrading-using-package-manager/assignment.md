---
slug: upgrading-using-package-manager
id: omokgpv13tne
type: challenge
title: Upgrading using a package manager
teaser: Upgrade using nodejs package manager
notes:
- type: text
  contents: |
    # Learn about Docker

    Docker is an open platform for developing, shipping, and running applications.
    Docker enables you to separate your applications from your infrastructure so
    you can deliver software quickly. Containers run anywhere!

    In this first challenge, you'll create a container image. Please wait while we
    boot a virtual machine for you.
tabs:
- title: Terminal
  type: terminal
  hostname: docker-vm
- title: Editor
  type: code
  hostname: docker-vm
  path: /root/labsrc/apps
difficulty: basic
timelimit: 600
---

🧪 Build a Docker image
=======================

Use this command to build a Docker image using the Dockerfile in
this directory:

```
docker build -t my-service .
```

💡 Source editor
================

Did you notice the tab with the source code editor, next to
the terminal?

🏁 Finish
=========

To complete the
challenge, press **Check**."
